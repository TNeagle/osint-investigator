#!/usr/bin/env python3
"""
OSINT Network Analysis Tool v2 — Intelligence Engine

Goes beyond static graph analysis to detect temporal anomalies,
obfuscation patterns, behavioral signals, and auto-prioritize
investigation targets.

Usage:
    python network_analysis.py --input data.json --output-dir ./output

Input JSON format (v2):
{
  "title": "Investigation Title",
  "entities": [
    {
      "id": "entity1",
      "label": "John Smith",
      "type": "person",
      "notes": "CEO of Acme Corp",
      "first_seen": "2020-03-15",
      "last_seen": "2024-01-10",
      "investigation_depth": "shallow",
      "tags": ["nominee_suspect", "offshore"],
      "behavioral": {
        "posting_frequency": "daily",
        "timezone_hint": "UTC+8",
        "persona_consistency": "low",
        "notes": "LinkedIn says Taipei, but posts at 3am TPE time consistently"
      }
    }
  ],
  "edges": [
    {
      "source": "entity1",
      "target": "entity2",
      "relation": "CEO of",
      "weight": 1.0,
      "evidence": "Company registry 2023",
      "date": "2023-06-01",
      "edge_type": "ownership"
    }
  ],
  "events": [
    {
      "id": "evt1",
      "description": "Company A registered",
      "date": "2022-01-15",
      "entities_involved": ["entity1", "entity2"],
      "significance": "high"
    }
  ]
}

Entity types: person, organization, address, domain, account, event, financial,
              wallet, vessel, aircraft, vehicle, property, species, media_outlet,
              bot_account, satellite_target, legal_case, unknown
Edge types: ownership, directorship, financial, social, legal, location, employment,
            family, digital, transaction, trades_in, ships_via, amplifies, cites,
            litigates, operates, tracks, publishes, unknown
investigation_depth: "none" | "shallow" | "medium" | "deep"
Tags: nominee_suspect, offshore, shell_company, scrubbed_content, privacy_shielded,
      circular_ownership, fabricated_persona, jurisdiction_shopping,
      bot_suspect, state_affiliated, content_farm, coordinated_cluster,
      cites_appendix_i, protected_species, repeat_offender, transit_hub,
      ais_gap, flag_change, mixer_interaction, sanctioned, peeling_chain,
      rapid_flipping, price_anomaly, greenwashing, forced_labor, etc.
"""

import json
import argparse
import sys
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter, defaultdict

try:
    import networkx as nx
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import matplotlib.font_manager as fm
except ImportError:
    print("ERROR: Required packages not installed. Run: pip install networkx matplotlib --break-system-packages")
    sys.exit(1)

# ── CJK font fallback ───────────────────────────────────────────
def _setup_cjk_font():
    """Try to find and set a CJK-capable font for matplotlib."""
    cjk_candidates = [
        "Noto Sans CJK TC", "Noto Sans CJK SC", "Noto Sans CJK",
        "WenQuanYi Micro Hei", "WenQuanYi Zen Hei",
        "AR PL UMing TW", "AR PL UKai TW",
        "Microsoft JhengHei", "SimHei", "PingFang TC",
        "Hiragino Sans GB", "Source Han Sans TC",
    ]
    available = {f.name for f in fm.fontManager.ttflist}
    for candidate in cjk_candidates:
        if candidate in available:
            matplotlib.rcParams['font.sans-serif'] = [candidate] + matplotlib.rcParams.get('font.sans-serif', [])
            matplotlib.rcParams['axes.unicode_minus'] = False
            return candidate
    return None

_cjk_font = _setup_cjk_font()


# ── Visual theme ─────────────────────────────────────────────────────

ENTITY_COLORS = {
    "person": "#E74C3C",
    "organization": "#3498DB",
    "address": "#2ECC71",
    "domain": "#9B59B6",
    "account": "#F39C12",
    "event": "#1ABC9C",
    "financial": "#E67E22",
    "wallet": "#F1C40F",
    "vessel": "#2980B9",
    "aircraft": "#8E44AD",
    "vehicle": "#D35400",
    "property": "#27AE60",
    "species": "#16A085",
    "media_outlet": "#C0392B",
    "bot_account": "#7F8C8D",
    "satellite_target": "#2C3E50",
    "legal_case": "#BDC3C7",
    "unknown": "#95A5A6",
}

ENTITY_SHAPES = {
    "person": "o", "organization": "s", "address": "^",
    "domain": "D", "account": "p", "event": "h",
    "financial": "8", "wallet": "8", "vessel": "D",
    "aircraft": "^", "vehicle": "v", "property": "s",
    "species": "h", "media_outlet": "p", "bot_account": "p",
    "satellite_target": "D", "legal_case": "s", "unknown": "o",
}

# Tags that signal obfuscation / counter-intelligence concern
OBFUSCATION_TAGS = {
    "nominee_suspect", "offshore", "shell_company", "scrubbed_content",
    "privacy_shielded", "circular_ownership", "fabricated_persona",
    "jurisdiction_shopping", "rapid_creation", "same_address_cluster",
    "bot_suspect", "state_affiliated", "content_farm", "coordinated_cluster",
    "mixer_interaction", "sanctioned", "peeling_chain", "ais_gap", "flag_change",
    "rapid_flipping", "price_anomaly", "greenwashing", "forced_labor",
}

# Tags that signal info-ops / influence campaign concern
INFOPS_TAGS = {
    "bot_suspect", "state_affiliated", "content_farm", "coordinated_cluster",
}

# Tags for wildlife/environmental crime
ENVIRONMENTAL_TAGS = {
    "cites_appendix_i", "protected_species", "repeat_offender", "transit_hub",
    "greenwashing", "forced_labor",
}


# ── Data loading ─────────────────────────────────────────────────────

def load_data(input_path: str) -> dict:
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for key in ["entities", "edges"]:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
    # Ensure events list exists
    if "events" not in data:
        data["events"] = []
    return data


def build_graph(data: dict) -> nx.Graph:
    G = nx.Graph()
    for entity in data["entities"]:
        G.add_node(
            entity["id"],
            label=entity.get("label", entity["id"]),
            entity_type=entity.get("type", "unknown"),
            notes=entity.get("notes", ""),
            first_seen=entity.get("first_seen", ""),
            last_seen=entity.get("last_seen", ""),
            investigation_depth=entity.get("investigation_depth", "none"),
            tags=entity.get("tags", []),
            behavioral=entity.get("behavioral", {}),
        )
    for edge in data["edges"]:
        G.add_edge(
            edge["source"], edge["target"],
            relation=edge.get("relation", "related to"),
            weight=edge.get("weight", 1.0),
            evidence=edge.get("evidence", ""),
            date=edge.get("date", ""),
            edge_type=edge.get("edge_type", "unknown"),
        )
    return G


# ── Core metrics (unchanged from v1) ────────────────────────────────

def compute_core_metrics(G: nx.Graph) -> dict:
    metrics = {
        "summary": {
            "total_entities": G.number_of_nodes(),
            "total_relationships": G.number_of_edges(),
            "density": round(nx.density(G), 4),
            "is_connected": nx.is_connected(G) if G.number_of_nodes() > 0 else False,
            "connected_components": nx.number_connected_components(G) if G.number_of_nodes() > 0 else 0,
        },
        "centrality": {},
        "communities": [],
        "key_findings": [],
    }
    if G.number_of_nodes() == 0:
        return metrics

    degree_cent = nx.degree_centrality(G)
    metrics["centrality"]["degree"] = {
        node: {
            "label": G.nodes[node].get("label", node),
            "type": G.nodes[node].get("entity_type", "unknown"),
            "score": round(score, 4),
            "connections": G.degree(node),
        }
        for node, score in sorted(degree_cent.items(), key=lambda x: x[1], reverse=True)
    }

    if G.number_of_nodes() > 2:
        between_cent = nx.betweenness_centrality(G)
        metrics["centrality"]["betweenness"] = {
            node: {"label": G.nodes[node].get("label", node), "score": round(score, 4)}
            for node, score in sorted(between_cent.items(), key=lambda x: x[1], reverse=True)
            if score > 0
        }

    try:
        communities = list(nx.community.greedy_modularity_communities(G))
        for i, community in enumerate(communities):
            members = [
                {"id": n, "label": G.nodes[n].get("label", n), "type": G.nodes[n].get("entity_type", "")}
                for n in community
            ]
            metrics["communities"].append({"community_id": i, "size": len(community), "members": members})
    except Exception:
        pass

    return metrics


# ── NEW: Temporal anomaly detection ──────────────────────────────────

def parse_date(s: str):
    """Try to parse a date string, return None on failure."""
    if not s:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m", "%Y/%m/%d", "%Y"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None


def detect_temporal_anomalies(G: nx.Graph, events: list) -> dict:
    """Analyze temporal patterns for suspicious signals."""
    findings = []
    details = {}

    # ── 1. Event clustering: multiple events within a short window ──
    dated_events = []
    for evt in events:
        d = parse_date(evt.get("date", ""))
        if d:
            dated_events.append((d, evt))
    dated_events.sort(key=lambda x: x[0])

    clusters = []
    if len(dated_events) >= 2:
        cluster = [dated_events[0]]
        for i in range(1, len(dated_events)):
            gap = (dated_events[i][0] - dated_events[i-1][0]).days
            if gap <= 14:  # 2-week window
                cluster.append(dated_events[i])
            else:
                if len(cluster) >= 3:
                    clusters.append(cluster)
                cluster = [dated_events[i]]
        if len(cluster) >= 3:
            clusters.append(cluster)

    if clusters:
        for cl in clusters:
            start = cl[0][0].strftime("%Y-%m-%d")
            end = cl[-1][0].strftime("%Y-%m-%d")
            descs = [e[1].get("description", "?") for e in cl]
            findings.append(
                f"TEMPORAL CLUSTER: {len(cl)} events within {start} to {end} — "
                f"possible coordinated activity. Events: {'; '.join(descs[:5])}"
            )
    details["event_clusters"] = [
        {
            "window": f"{cl[0][0].strftime('%Y-%m-%d')} to {cl[-1][0].strftime('%Y-%m-%d')}",
            "count": len(cl),
            "events": [e[1].get("description", "") for e in cl],
        }
        for cl in clusters
    ]

    # ── 2. Edge timing: relationships created in suspicious bursts ──
    edge_dates = []
    for u, v, d in G.edges(data=True):
        ed = parse_date(d.get("date", ""))
        if ed:
            edge_dates.append((ed, u, v, d.get("relation", "")))
    edge_dates.sort(key=lambda x: x[0])

    edge_clusters = []
    if len(edge_dates) >= 3:
        cluster = [edge_dates[0]]
        for i in range(1, len(edge_dates)):
            gap = (edge_dates[i][0] - edge_dates[i-1][0]).days
            if gap <= 14:
                cluster.append(edge_dates[i])
            else:
                if len(cluster) >= 3:
                    edge_clusters.append(cluster)
                cluster = [edge_dates[i]]
        if len(cluster) >= 3:
            edge_clusters.append(cluster)

    if edge_clusters:
        for cl in edge_clusters:
            start = cl[0][0].strftime("%Y-%m-%d")
            end = cl[-1][0].strftime("%Y-%m-%d")
            findings.append(
                f"RELATIONSHIP BURST: {len(cl)} connections formed within {start} to {end} — "
                f"may indicate coordinated setup (e.g., batch company registration, rapid network building)"
            )
    details["edge_bursts"] = [
        {
            "window": f"{cl[0][0].strftime('%Y-%m-%d')} to {cl[-1][0].strftime('%Y-%m-%d')}",
            "count": len(cl),
            "relationships": [f"{G.nodes[e[1]].get('label', e[1])} → {G.nodes[e[2]].get('label', e[2])}: {e[3]}" for e in cl],
        }
        for cl in edge_clusters
    ]

    # ── 3. Entity lifespan anomalies ──
    short_lived = []
    for node in G.nodes():
        fs = parse_date(G.nodes[node].get("first_seen", ""))
        ls = parse_date(G.nodes[node].get("last_seen", ""))
        if fs and ls:
            lifespan = (ls - fs).days
            if lifespan < 90 and G.nodes[node].get("entity_type") == "organization":
                short_lived.append((G.nodes[node].get("label", node), lifespan))

    if short_lived:
        names = [f"{name} ({days}d)" for name, days in short_lived]
        findings.append(
            f"SHORT-LIVED ENTITIES: {len(short_lived)} organization(s) existed < 90 days — "
            f"possible shell companies or vehicles for single transactions: {', '.join(names[:5])}"
        )
    details["short_lived_entities"] = [{"label": n, "lifespan_days": d} for n, d in short_lived]

    return {"findings": findings, "details": details}


# ── NEW: Obfuscation pattern detection ───────────────────────────────

def detect_obfuscation(G: nx.Graph) -> dict:
    """Detect counter-intelligence signals: shell patterns, nominee usage, etc."""
    findings = []
    details = {}

    # ── 1. Shared address clusters ──
    address_nodes = [n for n in G.nodes() if G.nodes[n].get("entity_type") == "address"]
    suspicious_addresses = []
    for addr in address_nodes:
        neighbors = list(G.neighbors(addr))
        org_neighbors = [n for n in neighbors if G.nodes[n].get("entity_type") == "organization"]
        if len(org_neighbors) >= 3:
            suspicious_addresses.append({
                "address": G.nodes[addr].get("label", addr),
                "address_id": addr,
                "companies": [G.nodes[n].get("label", n) for n in org_neighbors],
                "count": len(org_neighbors),
            })
    if suspicious_addresses:
        for sa in suspicious_addresses:
            findings.append(
                f"SHELL COMPANY SIGNAL: Address \"{sa['address']}\" hosts {sa['count']} organizations — "
                f"possible virtual office / shell company farm: {', '.join(sa['companies'][:5])}"
            )
    details["shared_address_clusters"] = suspicious_addresses

    # ── 2. Nominee director pattern (one person, many directorships) ──
    nominee_suspects = []
    for node in G.nodes():
        if G.nodes[node].get("entity_type") != "person":
            continue
        org_connections = []
        for neighbor in G.neighbors(node):
            if G.nodes[neighbor].get("entity_type") == "organization":
                edge = G.edges[node, neighbor]
                rel = edge.get("relation", "").lower()
                if any(kw in rel for kw in ["director", "secretary", "officer", "董事", "負責人"]):
                    org_connections.append(G.nodes[neighbor].get("label", neighbor))
        if len(org_connections) >= 5:
            nominee_suspects.append({
                "person": G.nodes[node].get("label", node),
                "person_id": node,
                "directorships": len(org_connections),
                "companies": org_connections,
            })
    if nominee_suspects:
        for ns in nominee_suspects:
            findings.append(
                f"NOMINEE DIRECTOR SUSPECT: \"{ns['person']}\" holds {ns['directorships']} directorships — "
                f"likely professional nominee, not real operator. Investigate who they front for."
            )
    details["nominee_suspects"] = nominee_suspects

    # ── 3. Tag-based obfuscation signals ──
    tagged_entities = defaultdict(list)
    for node in G.nodes():
        tags = set(G.nodes[node].get("tags", []))
        obf_tags = tags & OBFUSCATION_TAGS
        for tag in obf_tags:
            tagged_entities[tag].append(G.nodes[node].get("label", node))

    if tagged_entities:
        for tag, entities in tagged_entities.items():
            findings.append(
                f"OBFUSCATION SIGNAL [{tag}]: Flagged on {len(entities)} entity(ies) — "
                f"{', '.join(entities[:5])}"
            )
    details["obfuscation_tags"] = {tag: entities for tag, entities in tagged_entities.items()}

    # ── 4. Circular ownership detection ──
    DG = nx.DiGraph()
    for u, v, d in G.edges(data=True):
        rel = d.get("relation", "").lower()
        etype = d.get("edge_type", "").lower()
        if any(kw in rel for kw in ["owns", "subsidiary", "parent", "shareholder", "持股", "控股"]) or etype == "ownership":
            DG.add_edge(u, v)
            # Also try reverse for undirected graph ambiguity
    cycles = []
    try:
        for cycle in nx.simple_cycles(DG):
            if len(cycle) >= 3:
                labels = [G.nodes[n].get("label", n) for n in cycle if n in G.nodes]
                cycles.append(labels)
                if len(cycles) >= 5:
                    break
    except Exception:
        pass

    if cycles:
        for cyc in cycles:
            findings.append(
                f"CIRCULAR OWNERSHIP: {' → '.join(cyc)} → {cyc[0]} — "
                f"designed to obscure true beneficial ownership"
            )
    details["circular_ownership"] = cycles

    # ── 5. Jurisdiction shopping ──
    offshore_jurisdictions = {"bvi", "cayman", "panama", "seychelles", "marshall islands",
                              "bermuda", "jersey", "guernsey", "isle of man", "mauritius",
                              "british virgin islands", "vanuatu", "samoa", "nevis",
                              "開曼", "英屬維京", "巴拿馬", "塞席爾", "模里西斯"}
    offshore_entities = []
    for node in G.nodes():
        label = G.nodes[node].get("label", "").lower()
        notes = G.nodes[node].get("notes", "").lower()
        combined = label + " " + notes
        for j in offshore_jurisdictions:
            if j in combined:
                offshore_entities.append({
                    "entity": G.nodes[node].get("label", node),
                    "jurisdiction": j,
                })
                break
    if offshore_entities:
        findings.append(
            f"JURISDICTION SHOPPING: {len(offshore_entities)} entity(ies) in opacity jurisdictions — "
            f"{', '.join(e['entity'] + ' (' + e['jurisdiction'] + ')' for e in offshore_entities[:5])}"
        )
    details["offshore_entities"] = offshore_entities

    return {"findings": findings, "details": details}


# ── NEW: Financial flow analysis ─────────────────────────────────────

def analyze_financial_flows(G: nx.Graph) -> dict:
    """Detect financial flow patterns: layering, round-tripping, procurement cycles."""
    findings = []
    details = {}

    # ── 1. Financial chain tracing ──
    # Build directed graph of financial edges
    FG = nx.DiGraph()
    for u, v, d in G.edges(data=True):
        etype = d.get("edge_type", "").lower()
        rel = d.get("relation", "").lower()
        if etype == "financial" or any(kw in rel for kw in [
            "payment", "transfer", "donate", "fund", "invest", "轉帳", "支付",
            "捐款", "投資", "payment to", "funded by"
        ]):
            FG.add_edge(u, v, **d)

    if FG.number_of_edges() >= 2:
        # Find financial chains (paths of length 3+)
        financial_chains = []
        for node in FG.nodes():
            if FG.in_degree(node) == 0 and FG.out_degree(node) > 0:  # source nodes
                for target in FG.nodes():
                    if FG.out_degree(target) == 0 and FG.in_degree(target) > 0:  # sink nodes
                        try:
                            for path in nx.all_simple_paths(FG, node, target, cutoff=6):
                                if len(path) >= 3:
                                    labels = [G.nodes[n].get("label", n) for n in path if n in G.nodes]
                                    financial_chains.append({"path": labels, "ids": path, "length": len(path)})
                        except nx.NetworkXError:
                            pass

        if financial_chains:
            for fc in financial_chains[:5]:
                findings.append(
                    f"FINANCIAL CHAIN ({fc['length']} hops): {' → '.join(fc['path'])} — "
                    f"multi-hop flow may indicate layering or laundering structure"
                )
        details["financial_chains"] = financial_chains[:10]

        # ── 2. Financial round-tripping detection ──
        try:
            cycles = list(nx.simple_cycles(FG))
            round_trips = []
            for cycle in cycles:
                if len(cycle) >= 3:
                    labels = [G.nodes[n].get("label", n) for n in cycle if n in G.nodes]
                    round_trips.append(labels)
                    if len(round_trips) >= 3:
                        break
            if round_trips:
                for rt in round_trips:
                    findings.append(
                        f"FINANCIAL ROUND-TRIP: {' → '.join(rt)} → {rt[0]} — "
                        f"money returns to origin through intermediaries, possible round-tripping"
                    )
            details["financial_round_trips"] = round_trips
        except Exception:
            details["financial_round_trips"] = []

    else:
        details["financial_chains"] = []
        details["financial_round_trips"] = []

    # ── 3. Financial hub detection ──
    financial_nodes = set()
    for u, v, d in G.edges(data=True):
        etype = d.get("edge_type", "").lower()
        if etype == "financial":
            financial_nodes.add(u)
            financial_nodes.add(v)

    financial_hubs = []
    for node in financial_nodes:
        fin_connections = 0
        for neighbor in G.neighbors(node):
            edge = G.edges[node, neighbor]
            if edge.get("edge_type", "").lower() == "financial":
                fin_connections += 1
        if fin_connections >= 3:
            financial_hubs.append({
                "entity": G.nodes[node].get("label", node),
                "entity_id": node,
                "financial_connections": fin_connections,
                "type": G.nodes[node].get("entity_type", "unknown"),
            })

    if financial_hubs:
        for fh in financial_hubs:
            findings.append(
                f"FINANCIAL HUB: \"{fh['entity']}\" ({fh['type']}) has {fh['financial_connections']} "
                f"financial connections — central node in money flow network"
            )
    details["financial_hubs"] = financial_hubs

    # ── 4. Cross-type financial flows (person→org→financial→org pattern) ──
    suspicious_flows = []
    for u, v, d in G.edges(data=True):
        if d.get("edge_type", "").lower() == "financial":
            u_type = G.nodes[u].get("entity_type", "") if u in G.nodes else ""
            v_type = G.nodes[v].get("entity_type", "") if v in G.nodes else ""
            if u_type == "organization" and v_type == "financial":
                suspicious_flows.append({
                    "from": G.nodes[u].get("label", u),
                    "to": G.nodes[v].get("label", v),
                    "relation": d.get("relation", ""),
                    "evidence": d.get("evidence", ""),
                })
            elif u_type == "financial" and v_type == "organization":
                suspicious_flows.append({
                    "from": G.nodes[u].get("label", u),
                    "to": G.nodes[v].get("label", v),
                    "relation": d.get("relation", ""),
                    "evidence": d.get("evidence", ""),
                })

    if suspicious_flows:
        findings.append(
            f"CRYPTO/FINANCIAL BRIDGE: {len(suspicious_flows)} connection(s) between organizations and financial "
            f"entities (wallets, accounts) — investigate for off-books transactions"
        )
    details["org_financial_bridges"] = suspicious_flows

    return {"findings": findings, "details": details}


# ── NEW: Technology dependency detection ──────────────────────────────

def analyze_tech_dependencies(G: nx.Graph) -> dict:
    """Detect technology-related patterns: digital infrastructure sharing, domain clusters."""
    findings = []
    details = {}

    # ── 1. Digital infrastructure clusters ──
    domain_nodes = [n for n in G.nodes() if G.nodes[n].get("entity_type") == "domain"]
    shared_infra = []
    for domain in domain_nodes:
        connected_orgs = []
        for neighbor in G.neighbors(domain):
            if G.nodes[neighbor].get("entity_type") == "organization":
                connected_orgs.append(G.nodes[neighbor].get("label", neighbor))
        if len(connected_orgs) >= 2:
            shared_infra.append({
                "domain": G.nodes[domain].get("label", domain),
                "organizations": connected_orgs,
            })

    if shared_infra:
        for si in shared_infra:
            findings.append(
                f"SHARED DIGITAL INFRASTRUCTURE: Domain \"{si['domain']}\" connects to {len(si['organizations'])} "
                f"organizations — may indicate hidden common ownership: {', '.join(si['organizations'][:5])}"
            )
    details["shared_infrastructure"] = shared_infra

    # ── 2. Digital-to-financial bridges ──
    digital_financial = []
    for u, v, d in G.edges(data=True):
        u_type = G.nodes[u].get("entity_type", "") if u in G.nodes else ""
        v_type = G.nodes[v].get("entity_type", "") if v in G.nodes else ""
        if (u_type == "domain" and v_type == "financial") or (u_type == "financial" and v_type == "domain"):
            digital_financial.append({
                "domain": G.nodes[u].get("label", u) if u_type == "domain" else G.nodes[v].get("label", v),
                "financial": G.nodes[v].get("label", v) if v_type == "financial" else G.nodes[u].get("label", u),
                "relation": d.get("relation", ""),
            })

    if digital_financial:
        for df in digital_financial:
            findings.append(
                f"DIGITAL-FINANCIAL LINK: Domain \"{df['domain']}\" connected to financial entity "
                f"\"{df['financial']}\" — investigate for online fraud or crypto operations"
            )
    details["digital_financial_bridges"] = digital_financial

    # ── 3. Account/domain cluster analysis ──
    account_nodes = [n for n in G.nodes() if G.nodes[n].get("entity_type") in ("account", "domain")]
    person_digital_footprint = defaultdict(list)
    for acc in account_nodes:
        for neighbor in G.neighbors(acc):
            if G.nodes[neighbor].get("entity_type") == "person":
                person_digital_footprint[neighbor].append({
                    "account": G.nodes[acc].get("label", acc),
                    "type": G.nodes[acc].get("entity_type", ""),
                })

    large_footprints = []
    for person, accounts in person_digital_footprint.items():
        if len(accounts) >= 3:
            large_footprints.append({
                "person": G.nodes[person].get("label", person),
                "digital_assets": len(accounts),
                "accounts": [a["account"] for a in accounts],
            })
    if large_footprints:
        for lf in large_footprints:
            findings.append(
                f"LARGE DIGITAL FOOTPRINT: \"{lf['person']}\" has {lf['digital_assets']} digital assets — "
                f"cross-reference for identity correlation: {', '.join(lf['accounts'][:5])}"
            )
    details["large_digital_footprints"] = large_footprints

    return {"findings": findings, "details": details}


# ── NEW: Behavioral pattern analysis ─────────────────────────────────

def analyze_behavioral(G: nx.Graph) -> dict:
    """Analyze behavioral annotations on person nodes."""
    findings = []
    details = {}
    behavioral_nodes = []

    for node in G.nodes():
        beh = G.nodes[node].get("behavioral", {})
        if not beh:
            continue
        label = G.nodes[node].get("label", node)
        node_findings = []

        # Persona consistency
        consistency = beh.get("persona_consistency", "").lower()
        if consistency in ("low", "very_low"):
            node_findings.append(
                f"Low persona consistency — public image may not match actual behavior. "
                f"Notes: {beh.get('notes', 'N/A')}"
            )

        # Timezone mismatch
        tz_hint = beh.get("timezone_hint", "")
        tz_notes = beh.get("notes", "").lower()
        if tz_hint and ("different" in tz_notes or "mismatch" in tz_notes or "3am" in tz_notes):
            node_findings.append(
                f"Timezone anomaly detected — claimed location may not match actual activity times. "
                f"Hint: {tz_hint}"
            )

        # Any behavioral notes worth surfacing
        if beh.get("notes") and not node_findings:
            node_findings.append(f"Behavioral note: {beh['notes']}")

        if node_findings:
            behavioral_nodes.append({"entity": label, "entity_id": node, "signals": node_findings})
            for nf in node_findings:
                findings.append(f"BEHAVIORAL [{label}]: {nf}")

    details["behavioral_signals"] = behavioral_nodes
    return {"findings": findings, "details": details}


# ── NEW: Investigation priority scoring ──────────────────────────────

def compute_investigation_priorities(G: nx.Graph, core_metrics: dict,
                                      temporal: dict, obfuscation: dict,
                                      behavioral: dict) -> list:
    """
    Score every node and recommend the top investigation targets.
    Combines: graph centrality + investigation depth gap + anomaly involvement + obfuscation tags.
    """
    if G.number_of_nodes() == 0:
        return []

    scores = {}
    degree_cent = nx.degree_centrality(G)
    between_cent = nx.betweenness_centrality(G) if G.number_of_nodes() > 2 else {}

    for node in G.nodes():
        score = 0.0
        reasons = []

        # ── Factor 1: Graph centrality (0-30 points) ──
        dc = degree_cent.get(node, 0)
        bc = between_cent.get(node, 0)
        centrality_score = (dc * 15) + (bc * 15)
        if centrality_score > 0:
            reasons.append(f"centrality={centrality_score:.1f}")
        score += centrality_score

        # ── Factor 2: Investigation depth gap (0-30 points) ──
        depth = G.nodes[node].get("investigation_depth", "none")
        depth_penalty = {"none": 30, "shallow": 20, "medium": 10, "deep": 0}
        gap = depth_penalty.get(depth, 30)
        if gap > 0 and dc > 0.1:  # Only penalize if the node matters
            reasons.append(f"depth_gap={gap} (current: {depth})")
        score += gap if dc > 0.05 else gap * 0.3  # Low-centrality unresearched nodes get less priority

        # ── Factor 3: Obfuscation tags (0-20 points) ──
        tags = set(G.nodes[node].get("tags", []))
        obf_count = len(tags & OBFUSCATION_TAGS)
        if obf_count > 0:
            obf_score = min(obf_count * 7, 20)
            score += obf_score
            reasons.append(f"obfuscation_tags={obf_count} (+{obf_score})")

        # ── Factor 4: Bridge node bonus (0-10 points) ──
        if bc > 0.2:
            score += 10
            reasons.append("bridge_node (+10)")
        elif bc > 0.1:
            score += 5
            reasons.append("bridge_node (+5)")

        # ── Factor 5: Behavioral anomaly (0-10 points) ──
        beh = G.nodes[node].get("behavioral", {})
        if beh.get("persona_consistency", "").lower() in ("low", "very_low"):
            score += 10
            reasons.append("behavioral_anomaly (+10)")
        elif beh:
            score += 3
            reasons.append("has_behavioral_data (+3)")

        scores[node] = {
            "entity": G.nodes[node].get("label", node),
            "entity_id": node,
            "type": G.nodes[node].get("entity_type", "unknown"),
            "score": round(score, 1),
            "current_depth": depth,
            "reasons": reasons,
        }

    # Sort by score descending, return top candidates
    ranked = sorted(scores.values(), key=lambda x: x["score"], reverse=True)

    # Only return nodes that actually need more investigation
    actionable = [r for r in ranked if r["current_depth"] != "deep" and r["score"] > 10]
    return actionable[:10]


# ── Visualization (enhanced) ─────────────────────────────────────────

def visualize_graph(G: nx.Graph, title: str, output_path: str, priorities: list = None):
    if G.number_of_nodes() == 0:
        return

    fig, ax = plt.subplots(1, 1, figsize=(18, 14))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#1a1a2e')

    if G.number_of_nodes() <= 20:
        pos = nx.spring_layout(G, k=2.5, iterations=100, seed=42)
    else:
        pos = nx.kamada_kawai_layout(G)

    # Edges
    edge_weights = [G.edges[e].get("weight", 1.0) for e in G.edges()]
    nx.draw_networkx_edges(G, pos, ax=ax, width=[w * 2 for w in edge_weights],
                           alpha=0.4, edge_color='#a0a0c0')

    edge_labels = {(u, v): G.edges[u, v].get("relation", "") for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax,
                                  font_size=7, font_color='#c0c0e0', alpha=0.8,
                                  bbox=dict(boxstyle="round,pad=0.1", facecolor='#1a1a2e',
                                            edgecolor='none', alpha=0.7))

    # Build set of high-priority node IDs for visual highlighting
    priority_ids = set()
    if priorities:
        priority_ids = {p["entity_id"] for p in priorities[:5]}

    # Nodes by type
    for entity_type, color in ENTITY_COLORS.items():
        nodes = [n for n in G.nodes() if G.nodes[n].get("entity_type", "unknown") == entity_type]
        if not nodes:
            continue

        sizes = [300 + G.degree(n) * 200 for n in nodes]
        marker = ENTITY_SHAPES.get(entity_type, "o")

        # Highlight priority targets with bright edge
        edge_colors_list = []
        linewidths_list = []
        for n in nodes:
            has_obf = bool(set(G.nodes[n].get("tags", [])) & OBFUSCATION_TAGS)
            if n in priority_ids:
                edge_colors_list.append('#FFD700')  # gold border for priority
                linewidths_list.append(3.0)
            elif has_obf:
                edge_colors_list.append('#FF4444')  # red border for obfuscation
                linewidths_list.append(2.5)
            else:
                edge_colors_list.append('white')
                linewidths_list.append(1.5)

        nx.draw_networkx_nodes(G, pos, nodelist=nodes, ax=ax, node_color=color,
                                node_size=sizes, node_shape=marker, alpha=0.9,
                                edgecolors=edge_colors_list, linewidths=linewidths_list)

    # Labels
    labels = {n: G.nodes[n].get("label", n) for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, font_size=9,
                             font_color='white', font_weight='bold',
                             bbox=dict(boxstyle="round,pad=0.2", facecolor='#1a1a2e',
                                       edgecolor='none', alpha=0.6))

    # Legend
    legend_patches = [
        mpatches.Patch(color=color, label=entity_type.capitalize())
        for entity_type, color in ENTITY_COLORS.items()
        if any(G.nodes[n].get("entity_type") == entity_type for n in G.nodes())
    ]
    legend_patches.append(mpatches.Patch(facecolor='none', edgecolor='#FFD700', linewidth=2,
                                          label='Priority Target'))
    legend_patches.append(mpatches.Patch(facecolor='none', edgecolor='#FF4444', linewidth=2,
                                          label='Obfuscation Signal'))
    ax.legend(handles=legend_patches, loc='upper left', fontsize=10,
              facecolor='#16213e', edgecolor='#a0a0c0', labelcolor='white', framealpha=0.9)

    ax.set_title(title, fontsize=16, fontweight='bold', color='white', pad=20)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Graph saved to: {output_path}")


# ── Report generation (enhanced) ─────────────────────────────────────

def generate_report(data: dict, core: dict, temporal: dict,
                     obfuscation: dict, behavioral: dict,
                     financial: dict, tech: dict, priorities: list,
                     infops: dict = None, legal: dict = None,
                     property_data: dict = None) -> str:
    title = data.get("title", "Network Analysis")
    lines = [
        f"# {title} — Intelligence Analysis Report\n",
        "## Network Summary\n",
        f"- **Entities**: {core['summary']['total_entities']}",
        f"- **Relationships**: {core['summary']['total_relationships']}",
        f"- **Network Density**: {core['summary']['density']}",
        f"- **Connected Components**: {core['summary']['connected_components']}",
        "",
    ]

    # ── Priority investigation targets ──
    if priorities:
        lines.append("## 🎯 Priority Investigation Targets\n")
        lines.append("These entities need deeper investigation, ranked by intelligence value:\n")
        lines.append("| Rank | Entity | Type | Score | Current Depth | Key Reasons |")
        lines.append("|------|--------|------|-------|---------------|-------------|")
        for i, p in enumerate(priorities[:10], 1):
            reasons_short = "; ".join(p["reasons"][:3])
            lines.append(f"| {i} | {p['entity']} | {p['type']} | {p['score']} | {p['current_depth']} | {reasons_short} |")
        lines.append("")

    # ── Temporal anomalies ──
    if temporal["findings"]:
        lines.append("## ⏱ Temporal Anomalies\n")
        for f in temporal["findings"]:
            lines.append(f"- {f}")
        lines.append("")

    # ── Obfuscation signals ──
    if obfuscation["findings"]:
        lines.append("## 🔒 Obfuscation & Counter-Intelligence Signals\n")
        for f in obfuscation["findings"]:
            lines.append(f"- {f}")
        lines.append("")

    # ── Behavioral signals ──
    if behavioral["findings"]:
        lines.append("## 🧠 Behavioral Pattern Signals\n")
        for f in behavioral["findings"]:
            lines.append(f"- {f}")
        lines.append("")

    # ── Financial flow signals ──
    if financial["findings"]:
        lines.append("## 💰 Financial Flow Analysis\n")
        for f in financial["findings"]:
            lines.append(f"- {f}")
        lines.append("")

    # ── Technology signals ──
    if tech["findings"]:
        lines.append("## 🔧 Technology & Digital Infrastructure\n")
        for f in tech["findings"]:
            lines.append(f"- {f}")
        lines.append("")

    # ── Info-ops signals ──
    if infops and infops["findings"]:
        lines.append("## 📡 Information Operations & Influence\n")
        for f in infops["findings"]:
            lines.append(f"- {f}")
        lines.append("")

    # ── Legal signals ──
    if legal and legal["findings"]:
        lines.append("## ⚖️ Legal & Litigation Patterns\n")
        for f in legal["findings"]:
            lines.append(f"- {f}")
        lines.append("")

    # ── Property signals ──
    if property_data and property_data["findings"]:
        lines.append("## 🏠 Property & Real Estate Patterns\n")
        for f in property_data["findings"]:
            lines.append(f"- {f}")
        lines.append("")

    # ── Core graph findings ──
    if core["key_findings"]:
        lines.append("## Graph Structure Findings\n")
        for i, finding in enumerate(core["key_findings"], 1):
            lines.append(f"{i}. {finding}")
        lines.append("")

    # ── Top entities ──
    lines.append("## Most Connected Entities\n")
    lines.append("| Rank | Entity | Type | Connections | Centrality |")
    lines.append("|------|--------|------|-------------|------------|")
    for rank, (node, info) in enumerate(list(core["centrality"]["degree"].items())[:10], 1):
        lines.append(f"| {rank} | {info['label']} | {info['type']} | {info['connections']} | {info['score']:.3f} |")
    lines.append("")

    # ── Bridge entities ──
    if "betweenness" in core["centrality"] and core["centrality"]["betweenness"]:
        lines.append("## Bridge Entities\n")
        lines.append("| Entity | Betweenness Score |")
        lines.append("|--------|-------------------|")
        for node, info in list(core["centrality"]["betweenness"].items())[:10]:
            lines.append(f"| {info['label']} | {info['score']:.3f} |")
        lines.append("")

    # ── Communities ──
    if core["communities"]:
        lines.append("## Detected Communities\n")
        for comm in core["communities"]:
            member_labels = [m["label"] for m in comm["members"]]
            lines.append(f"### Cluster {comm['community_id'] + 1} ({comm['size']} members)\n")
            lines.append(f"Members: {', '.join(member_labels)}\n")
        lines.append("")

    return "\n".join(lines)


# ── Path finding (unchanged) ─────────────────────────────────────────

def find_shortest_paths(G: nx.Graph, source: str, target: str) -> list:
    try:
        paths = list(nx.all_shortest_paths(G, source, target))
        result = []
        for path in paths:
            path_detail = []
            for i, node in enumerate(path):
                entry = {"entity": G.nodes[node].get("label", node),
                         "type": G.nodes[node].get("entity_type", "")}
                if i < len(path) - 1:
                    edge_data = G.edges[path[i], path[i+1]]
                    entry["connects_via"] = edge_data.get("relation", "related to")
                path_detail.append(entry)
            result.append(path_detail)
        return result
    except nx.NetworkXNoPath:
        return []


# ── NEW: Info-ops / influence campaign detection ─────────────────

def analyze_info_ops(G: nx.Graph, events: list) -> dict:
    """Detect coordinated inauthentic behavior patterns."""
    findings = []
    details = {}

    # ── 1. Bot/coordinated account clusters ──
    bot_suspects = [n for n in G.nodes() if
                    G.nodes[n].get("entity_type") in ("account", "bot_account") and
                    bool(set(G.nodes[n].get("tags", [])) & INFOPS_TAGS)]

    if len(bot_suspects) >= 3:
        # Check if they form a connected cluster
        subgraph = G.subgraph(bot_suspects)
        if subgraph.number_of_edges() > 0:
            clusters = list(nx.connected_components(subgraph))
            coordinated_clusters = [c for c in clusters if len(c) >= 3]
            if coordinated_clusters:
                for cl in coordinated_clusters:
                    labels = [G.nodes[n].get("label", n) for n in cl]
                    findings.append(
                        f"COORDINATED CLUSTER: {len(cl)} suspicious accounts interconnected — "
                        f"possible bot network or coordinated operation: {', '.join(labels[:5])}"
                    )
            details["coordinated_clusters"] = [
                [G.nodes[n].get("label", n) for n in c] for c in coordinated_clusters
            ]
        else:
            details["coordinated_clusters"] = []
    else:
        details["coordinated_clusters"] = []

    # ── 2. Amplification network detection ──
    amplification_edges = []
    for u, v, d in G.edges(data=True):
        rel = d.get("relation", "").lower()
        etype = d.get("edge_type", "").lower()
        if etype == "amplifies" or any(kw in rel for kw in [
            "retweet", "share", "amplif", "forward", "轉發", "分享"
        ]):
            amplification_edges.append((u, v))

    if len(amplification_edges) >= 5:
        AG = nx.DiGraph(amplification_edges)
        # Find nodes that receive the most amplification
        in_degrees = sorted(AG.in_degree(), key=lambda x: x[1], reverse=True)
        top_amplified = [(n, d) for n, d in in_degrees if d >= 3]
        if top_amplified:
            for node, deg in top_amplified[:3]:
                label = G.nodes[node].get("label", node) if node in G.nodes else node
                findings.append(
                    f"AMPLIFICATION TARGET: \"{label}\" amplified by {deg} accounts — "
                    f"investigate if coordinated"
                )
        details["amplification_targets"] = [
            {"entity": G.nodes[n].get("label", n) if n in G.nodes else n,
             "amplified_by": d} for n, d in top_amplified[:10]
        ]
    else:
        details["amplification_targets"] = []

    # ── 3. Content farm / media outlet clustering ──
    media_nodes = [n for n in G.nodes() if
                   G.nodes[n].get("entity_type") in ("media_outlet", "domain") and
                   "content_farm" in G.nodes[n].get("tags", [])]
    if media_nodes:
        findings.append(
            f"CONTENT FARM NETWORK: {len(media_nodes)} suspected content farm(s) detected — "
            f"{', '.join(G.nodes[n].get('label', n) for n in media_nodes[:5])}"
        )
    details["content_farms"] = [G.nodes[n].get("label", n) for n in media_nodes]

    return {"findings": findings, "details": details}


# ── NEW: Legal / litigation network analysis ─────────────────────

def analyze_legal_patterns(G: nx.Graph) -> dict:
    """Detect litigation network patterns: repeat litigants, shared counsel."""
    findings = []
    details = {}

    # ── 1. Litigation network ──
    legal_edges = []
    for u, v, d in G.edges(data=True):
        etype = d.get("edge_type", "").lower()
        rel = d.get("relation", "").lower()
        if etype == "legal" or etype == "litigates" or any(kw in rel for kw in [
            "plaintiff", "defendant", "sues", "sued", "原告", "被告", "訴訟"
        ]):
            legal_edges.append((u, v, d))

    if len(legal_edges) >= 3:
        # Find repeat litigants
        litigant_counts = Counter()
        for u, v, d in legal_edges:
            litigant_counts[u] += 1
            litigant_counts[v] += 1

        repeat_litigants = [(n, c) for n, c in litigant_counts.items() if c >= 3]
        if repeat_litigants:
            for node, count in sorted(repeat_litigants, key=lambda x: x[1], reverse=True)[:5]:
                label = G.nodes[node].get("label", node) if node in G.nodes else node
                findings.append(
                    f"REPEAT LITIGANT: \"{label}\" involved in {count} legal relationships — "
                    f"investigate pattern (serial plaintiff? frequent defendant?)"
                )
        details["repeat_litigants"] = [
            {"entity": G.nodes[n].get("label", n) if n in G.nodes else n,
             "legal_connections": c} for n, c in repeat_litigants
        ]
    else:
        details["repeat_litigants"] = []

    # ── 2. Shared legal representation ──
    legal_rep_map = defaultdict(list)
    for u, v, d in G.edges(data=True):
        rel = d.get("relation", "").lower()
        if any(kw in rel for kw in ["represent", "lawyer", "counsel", "attorney", "律師", "代理"]):
            # The person/org providing legal representation
            if G.nodes.get(u, {}).get("entity_type") in ("person", "organization"):
                legal_rep_map[u].append(v)
            if G.nodes.get(v, {}).get("entity_type") in ("person", "organization"):
                legal_rep_map[v].append(u)

    shared_counsel = {k: v for k, v in legal_rep_map.items() if len(v) >= 2}
    if shared_counsel:
        for counsel, clients in shared_counsel.items():
            counsel_label = G.nodes[counsel].get("label", counsel) if counsel in G.nodes else counsel
            client_labels = [G.nodes[c].get("label", c) if c in G.nodes else c for c in clients]
            findings.append(
                f"SHARED COUNSEL: \"{counsel_label}\" represents {len(clients)} entities — "
                f"may indicate hidden connection: {', '.join(client_labels[:5])}"
            )
    details["shared_counsel"] = [
        {"counsel": G.nodes[k].get("label", k) if k in G.nodes else k,
         "clients": [G.nodes[c].get("label", c) if c in G.nodes else c for c in v]}
        for k, v in shared_counsel.items()
    ]

    # ── 3. Legal case nodes as connectors ──
    case_nodes = [n for n in G.nodes() if G.nodes[n].get("entity_type") == "legal_case"]
    case_connectors = []
    for case in case_nodes:
        parties = list(G.neighbors(case))
        if len(parties) >= 3:
            party_labels = [G.nodes[p].get("label", p) for p in parties]
            case_connectors.append({
                "case": G.nodes[case].get("label", case),
                "parties": party_labels,
                "count": len(parties),
            })
    if case_connectors:
        findings.append(
            f"LITIGATION HUB: {len(case_connectors)} case(s) connecting 3+ parties — "
            f"investigate for organized fraud or systemic disputes"
        )
    details["litigation_hubs"] = case_connectors

    return {"findings": findings, "details": details}


# ── NEW: Real estate / property pattern detection ────────────────

def analyze_property_patterns(G: nx.Graph) -> dict:
    """Detect suspicious property transaction patterns."""
    findings = []
    details = {}

    property_nodes = [n for n in G.nodes() if G.nodes[n].get("entity_type") == "property"]

    # ── 1. Rapid ownership changes ──
    rapid_transfers = []
    for prop in property_nodes:
        ownership_edges = []
        for neighbor in G.neighbors(prop):
            edge = G.edges[prop, neighbor]
            date = parse_date(edge.get("date", ""))
            rel = edge.get("relation", "")
            if date:
                ownership_edges.append((date, neighbor, rel))
        ownership_edges.sort(key=lambda x: x[0])

        if len(ownership_edges) >= 2:
            for i in range(1, len(ownership_edges)):
                gap = (ownership_edges[i][0] - ownership_edges[i-1][0]).days
                if 0 < gap < 180:  # transferred within 6 months
                    rapid_transfers.append({
                        "property": G.nodes[prop].get("label", prop),
                        "days_between_transfers": gap,
                        "from": G.nodes[ownership_edges[i-1][1]].get("label", "") if ownership_edges[i-1][1] in G.nodes else "",
                        "to": G.nodes[ownership_edges[i][1]].get("label", "") if ownership_edges[i][1] in G.nodes else "",
                    })

    if rapid_transfers:
        for rt in rapid_transfers[:5]:
            findings.append(
                f"RAPID PROPERTY TRANSFER: \"{rt['property']}\" changed hands within {rt['days_between_transfers']} days — "
                f"possible laundering or related-party layering"
            )
    details["rapid_transfers"] = rapid_transfers

    # ── 2. Property concentration ──
    owner_properties = defaultdict(list)
    for prop in property_nodes:
        for neighbor in G.neighbors(prop):
            if G.nodes.get(neighbor, {}).get("entity_type") in ("person", "organization"):
                owner_properties[neighbor].append(G.nodes[prop].get("label", prop))

    concentrated = {k: v for k, v in owner_properties.items() if len(v) >= 3}
    if concentrated:
        for owner, props in concentrated.items():
            owner_label = G.nodes[owner].get("label", owner) if owner in G.nodes else owner
            findings.append(
                f"PROPERTY CONCENTRATION: \"{owner_label}\" connected to {len(props)} properties — "
                f"investigate for strategic accumulation or nominal ownership"
            )
    details["property_concentration"] = [
        {"owner": G.nodes[k].get("label", k) if k in G.nodes else k,
         "properties": v, "count": len(v)} for k, v in concentrated.items()
    ]

    # ── 3. Tag-based property red flags ──
    flagged = []
    for prop in property_nodes:
        tags = set(G.nodes[prop].get("tags", []))
        red_flags = tags & {"rapid_flipping", "price_anomaly"}
        if red_flags:
            flagged.append({
                "property": G.nodes[prop].get("label", prop),
                "flags": list(red_flags),
            })
    if flagged:
        findings.append(
            f"PROPERTY RED FLAGS: {len(flagged)} property(ies) flagged — "
            f"{', '.join(f['property'] + ' (' + ','.join(f['flags']) + ')' for f in flagged[:5])}"
        )
    details["property_red_flags"] = flagged

    return {"findings": findings, "details": details}


# ── NEW: Graph merge utility ─────────────────────────────────────

def merge_graphs(base_path: str, *merge_paths: str, output_path: str = None) -> dict:
    """
    Merge multiple investigation JSON files into one unified graph.
    Handles deduplication by entity ID — later files override earlier ones.
    """
    base = load_data(base_path)

    for path in merge_paths:
        addition = load_data(path)

        # Merge entities (by ID, later wins)
        existing_ids = {e["id"] for e in base["entities"]}
        for entity in addition["entities"]:
            if entity["id"] in existing_ids:
                # Update existing: merge tags, keep deeper investigation_depth
                for i, existing in enumerate(base["entities"]):
                    if existing["id"] == entity["id"]:
                        # Merge tags
                        merged_tags = list(set(existing.get("tags", []) + entity.get("tags", [])))
                        base["entities"][i]["tags"] = merged_tags
                        # Keep deeper depth
                        depth_order = {"none": 0, "shallow": 1, "medium": 2, "deep": 3}
                        if depth_order.get(entity.get("investigation_depth", "none"), 0) > \
                           depth_order.get(existing.get("investigation_depth", "none"), 0):
                            base["entities"][i]["investigation_depth"] = entity["investigation_depth"]
                        # Merge notes
                        if entity.get("notes") and entity["notes"] != existing.get("notes", ""):
                            base["entities"][i]["notes"] = existing.get("notes", "") + "; " + entity["notes"]
                        # Merge behavioral
                        if entity.get("behavioral"):
                            base["entities"][i].setdefault("behavioral", {}).update(entity["behavioral"])
                        break
            else:
                base["entities"].append(entity)
                existing_ids.add(entity["id"])

        # Merge edges (deduplicate by source+target+relation)
        existing_edges = {(e["source"], e["target"], e.get("relation", "")) for e in base["edges"]}
        for edge in addition["edges"]:
            key = (edge["source"], edge["target"], edge.get("relation", ""))
            if key not in existing_edges:
                base["edges"].append(edge)
                existing_edges.add(key)

        # Merge events (by ID)
        existing_event_ids = {e["id"] for e in base.get("events", [])}
        for event in addition.get("events", []):
            if event["id"] not in existing_event_ids:
                base.setdefault("events", []).append(event)
                existing_event_ids.add(event["id"])

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(base, f, ensure_ascii=False, indent=2)
        print(f"Merged graph saved to: {output_path}")

    return base


# ── Main ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="OSINT Network Analysis Tool v2")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output-dir", required=True, help="Directory for output files")
    parser.add_argument("--find-path", nargs=2, metavar=("SOURCE", "TARGET"),
                        help="Find shortest path between two entity IDs")
    parser.add_argument("--merge", nargs="+", metavar="JSON_FILE",
                        help="Merge additional JSON files into the input graph before analysis")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    data = load_data(args.input)

    # Merge additional files if provided
    if args.merge:
        data = merge_graphs(args.input, *args.merge)

    G = build_graph(data)
    title = data.get("title", "OSINT Network Analysis")

    # Run all analysis layers
    core = compute_core_metrics(G)
    temporal = detect_temporal_anomalies(G, data.get("events", []))
    obfuscation_result = detect_obfuscation(G)
    behavioral_result = analyze_behavioral(G)
    financial_result = analyze_financial_flows(G)
    tech_result = analyze_tech_dependencies(G)
    infops_result = analyze_info_ops(G, data.get("events", []))
    legal_result = analyze_legal_patterns(G)
    property_result = analyze_property_patterns(G)
    priorities = compute_investigation_priorities(G, core, temporal, obfuscation_result, behavioral_result)

    # Each analysis layer now has its own report section, so we only merge
    # into key_findings for the console summary (not the report).
    all_findings = (temporal["findings"] + obfuscation_result["findings"] +
                    behavioral_result["findings"] + financial_result["findings"] +
                    tech_result["findings"] + infops_result["findings"] +
                    legal_result["findings"] + property_result["findings"])

    # Build comprehensive metrics output
    full_metrics = {
        "core": core,
        "temporal": temporal["details"],
        "obfuscation": obfuscation_result["details"],
        "behavioral": behavioral_result["details"],
        "financial": financial_result["details"],
        "technology": tech_result["details"],
        "info_ops": infops_result["details"],
        "legal": legal_result["details"],
        "property": property_result["details"],
        "investigation_priorities": priorities,
    }

    # Save metrics
    metrics_path = output_dir / "network_metrics.json"
    with open(metrics_path, 'w', encoding='utf-8') as f:
        json.dump(full_metrics, f, ensure_ascii=False, indent=2)
    print(f"Metrics saved to: {metrics_path}")

    # Visualization
    viz_path = output_dir / "network_graph.png"
    visualize_graph(G, title, str(viz_path), priorities)

    # Report
    report = generate_report(data, core, temporal, obfuscation_result, behavioral_result,
                              financial_result, tech_result, priorities,
                              infops_result, legal_result, property_result)
    report_path = output_dir / "network_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"Report saved to: {report_path}")

    # Optional path finding
    if args.find_path:
        source, target = args.find_path
        paths = find_shortest_paths(G, source, target)
        path_path = output_dir / "shortest_paths.json"
        with open(path_path, 'w', encoding='utf-8') as f:
            json.dump({"source": source, "target": target, "paths": paths}, f, ensure_ascii=False, indent=2)
        print(f"Paths saved to: {path_path}")

    # Console summary
    print(f"\n{'='*60}")
    print(f"  OSINT Intelligence Analysis Complete")
    print(f"{'='*60}")
    print(f"  Entities: {core['summary']['total_entities']}")
    print(f"  Relationships: {core['summary']['total_relationships']}")
    print(f"  Communities: {len(core['communities'])}")
    print(f"  Temporal anomalies: {len(temporal['findings'])}")
    print(f"  Obfuscation signals: {len(obfuscation_result['findings'])}")
    print(f"  Behavioral signals: {len(behavioral_result['findings'])}")
    print(f"  Financial flow signals: {len(financial_result['findings'])}")
    print(f"  Technology signals: {len(tech_result['findings'])}")
    print(f"  Info-ops signals: {len(infops_result['findings'])}")
    print(f"  Legal patterns: {len(legal_result['findings'])}")
    print(f"  Property patterns: {len(property_result['findings'])}")
    print(f"  Priority targets: {len(priorities)}")

    if priorities:
        print(f"\n  Top 3 investigation targets:")
        for i, p in enumerate(priorities[:3], 1):
            print(f"    {i}. {p['entity']} (score: {p['score']}, depth: {p['current_depth']})")

    if all_findings:
        print(f"\n  Key Findings ({len(all_findings)}):")
        for finding in all_findings[:5]:
            print(f"    • {finding[:120]}...")


if __name__ == "__main__":
    main()
