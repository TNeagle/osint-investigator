# Supply Chain Graph Integration — 供應鏈圖譜整合指南

**Parent playbook**: `playbook-investment.md` (core Three Questions framework)
**Companion**: `playbook-investment-events.md` (geopolitical event assessment)

This file covers how to use the supply chain knowledge graph (`supply_chain_mcp/data/supply_chain.json`) during investment analysis.

---

## Graph Pre-extraction Workflow

Before starting any investment analysis, run the graph intelligence extraction:

1. Generate `graph_intel_{stock_id}.json` using the supply chain MCP tools
2. This gives you pre-computed: bc (betweenness centrality), degree, customers, suppliers, competitors, upstream chain

**Use VENV Python** (`supply_chain_mcp/.venv/Scripts/python.exe`, NX 3.6.1), NOT system Python.

---

## What to Query from the Graph

| Query | Why | Investment relevance |
|-------|-----|---------------------|
| **Customer concentration** | Is >30% of revenue from one customer? | Single-customer dependency = high risk |
| **Supply chain position** | Confirm OSINT-claimed relationships against graph edges | Validates or contradicts company claims |
| **Cross-company linkages** | Shared customers, shared suppliers, cross-holdings | Reveals hidden correlation in portfolio |
| **Competitive mapping** | Who else serves the same customers? | Identifies substitution risk |
| **Anonymous customer de-anonymization** | Graph adjacency + revenue triangulation | Fills gaps in annual report data |
| **Upstream chain depth** | Tier 2/3 suppliers and geographic origins | Geopolitical vulnerability mapping |

Graph data provides **structure**; web search provides **dynamics**. Neither alone is sufficient.

---

## Betweenness Centrality (BC) Interpretation Guide

When using graph betweenness centrality, distinguish two types:

| Type | Characteristics | Example | Investment implication |
|------|----------------|---------|----------------------|
| **Infrastructure type** | High bc + high out-degree + low margin | 中鋼 (bc=0.042, 416 edges) | Breadth = many customers but NO pricing power. bc does not equal moat |
| **Bottleneck type** | High bc + moderate degree + high margin | 台積電 (bc=0.036, high margin 60%+) | Depth = irreplaceable position. bc = moat |

**Rule: NEVER cite high bc alone as evidence of investment value. Always check whether it reflects breadth (infrastructure) or depth (bottleneck).**

Key metrics to cross-reference with bc:
- **Out-degree**: High out-degree + high bc = infrastructure (many customers, commodity pricing)
- **Margin**: High margin + high bc = bottleneck (few alternatives, pricing power)
- **In-degree**: High in-degree = many suppliers = replaceable inputs (good for buyer)

---

## Event Node Schema — 事件圖譜

The supply chain graph contains **event nodes** (type="event") representing major external forces that impact companies. These are NOT static — they must be refreshed via WebSearch and updated when status changes.

**Event node schema:**
```json
{
  "id": "EVT_AI_DATACENTER",
  "type": "event",
  "category": "tech_shift",
  "name": "AI 資料中心建設潮",
  "status": "accelerating|stable|de-escalating|emerging|resolved",
  "severity": "extreme|high|medium|low",
  "start_date": "2023-01",
  "last_updated": "2026-03-20",
  "description": "Latest status summary"
}
```

**Event -> Company edges:**
```json
{
  "type": "impacts",
  "impact": "beneficiary|victim|neutral",
  "magnitude": "extreme|high|medium|low",
  "description": "How this event affects this company"
}
```

For the 9 event categories (geopolitical, tech_shift, industry_cycle, regulation, supply_disruption, macro, corporate, demographic, esg), see `playbook-investment-events.md`.

---

## How to Query Event Nodes During Analysis

**Step 1: Find events connected to the target company:**
```python
for u, v, d in G.in_edges(stock_id, data=True):
    if G.nodes[u].get('type') == 'event':
        print(f"Event: {G.nodes[u]['name']} -> impact: {d['relations'][0]['impact']}")
```

**Step 2: Check event status** — is it escalating or de-escalating? This changes the risk weight.

**Step 3: Cross-reference events across companies** — if two companies in the same portfolio are both victims of the same event, that is concentrated event risk.

**Step 4: Update events when status changes** — after each WebSearch round, update `status` and `last_updated` on relevant event nodes. If an event resolves, set status="resolved" but keep the node for history.

**Step 5: Create new event nodes** when the Fresh Event Scan (Step 0 of `playbook-investment-events.md`) discovers events not yet in the graph. Use the schema above and connect to all affected companies.

---

## Post-analysis: Write Back to Graph (MANDATORY)

After completing the analysis and writing the report, **write the structured findings into the supply chain graph node**:

```python
node["investment_analysis"] = {
    "analysis_date": "YYYY-MM-DD",
    "current_price": X,
    "role_transformed": true/false/"partial",
    "pricing_power": {"green": N, "yellow": N, "red": N},
    "structural_valuation": {"bull": X, "base": X, "bear": X, "weighted_midpoint": X},
    "price_position": "below_bear / bear_to_base / base / base_to_bull / above_bull",
    "verdict": "one-line summary"
}
node["geopolitical_assessment"] = {
    "overall_classification": "direct_beneficiary / indirect_beneficiary / neutral / indirect_victim / direct_victim",
    "china_exposure": "high / medium / low",
    "overseas_production": true/false,
    "key_risk": "one-line",
    "key_opportunity": "one-line"
}
```

This ensures the graph accumulates intelligence over time, and future analyses can build on prior findings.

---

## Graph Data Quality Notes

- **Noise nodes**: Some nodes may be shell companies, duplicates, or misidentified entities. Cross-check with MOPS data before relying on graph edges.
- **Duplicate detection**: Known issue — e.g., 福懋科技 (FATC) has nodes under both 5225 and 8131. When you encounter duplicate stock_ids for the same company, use the correct TSE code and flag the duplicate for cleanup.
- **Edge confidence**: Edges have `confirmed` vs `likely` status. Weight confirmed edges much higher in analysis. Likely edges should be validated via WebSearch before using in investment conclusions.
- **Stale data**: Check `last_updated` on nodes. If a node's data is >6 months old, re-verify key relationships before relying on them.
