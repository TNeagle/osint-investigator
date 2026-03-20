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

## Product & Material Layer — 產品/原材料層級體系

The graph contains not only companies and events, but also **products, materials, and resources** as independent nodes. This enables tracing risk from raw material origins all the way to end products.

### Four-Layer Hierarchy

| Layer | node_type | Definition | Risk Character | Examples |
|-------|-----------|-----------|---------------|----------|
| **L0 Resource** | `L0_resource` | Extracted from earth/atmosphere | Country monopoly + geopolitics | Silicon, indium, gallium, iron ore, crude oil, cotton, neon |
| **L1 Material** | `L1_material` | Refined/synthesized, used as manufacturing input | Refining concentration + export controls | Silicon wafer, photoresist, CCL, polyester fiber, steel billet |
| **L2 Device** | `L2_device` | Manufactured discrete item | Technology monopoly + capacity cycle | DDR4 DRAM, NOR Flash, ABF substrate, steel coil, fabric |
| **L3 Module** | `L3_module` | Assembled system-level product | Demand cycle + inventory dynamics | Memory module, optical transceiver, server, garment |

**Classification rule:** An item belongs to the layer where it is CONSUMED (not assembled) by the next layer. Silicon wafer is L1 (consumed by fab process), not L2. DRAM die is L2 (assembled into DIMM), not L1.

### Node Schema

```json
{
  "id": "DEV_DDR4_DRAM",
  "name": "DDR4 DRAM Die",
  "type": "L2_device",
  "category": "memory_ic",
  "industry_chain": "semiconductor",
  "supplier_count": 5,
  "active_supplier_count": 2,
  "hhi": 4500,
  "normal_supply": "adequate",
  "current_status": "critical_shortage",
  "strategic_classification": "critical",
  "last_updated": "2026-03-20"
}
```

Key fields:
- `supplier_count` / `active_supplier_count`: How many can make it vs how many are currently making it
- `hhi`: Herfindahl-Hirschman Index (>2500 = highly concentrated)
- `current_status`: `abundant | adequate | tight | shortage | critical_shortage` — this is DYNAMIC, changes with market conditions
- `strategic_classification`: `commodity | important | strategic | critical` — can upgrade when shortage hits (e.g., DDR4 was commodity, now critical)

### Category Reference (cross-industry)

**L0 Resource categories:** `semiconductor_metal`, `noble_gas`, `metal_ore`, `energy`, `petrochemical_feedstock`, `mineral`, `agricultural`, `forestry`, `rare_earth`

**L1 Material categories:** `wafer_substrate`, `chemical_process`, `pcb_material`, `steel_intermediate`, `petrochemical`, `polymer`, `textile_material`, `cement_material`, `food_intermediate`, `packaging_material`

**L2 Device categories:** `memory_ic`, `logic_ic`, `optoelectronic`, `substrate_board`, `passive`, `steel_product`, `plastic_product`, `textile_product`, `glass`, `paper`

**L3 Module categories:** `memory_module`, `optical_module`, `server_system`, `network_equipment`, `consumer_electronics`, `automotive`, `construction`, `food_product`, `textile_finished`

### Edge Types for Product/Material Layer

```
L0 --[raw_material_for]--> L1    (resource feeds material production)
L1 --[input_to]--> Company       (material is consumed by company's manufacturing)
Company --[produces]--> L2       (company manufactures this device/intermediate)
L2 --[component_of]--> L3       (device is assembled into module)
Company --[produces]--> L3       (company assembles this module/product)
```

### When to Build Product/Material Nodes

- **During investigation**: When you discover a supply chain bottleneck (single source, monopoly, shortage), create the product/material node
- **Priority**: Only build nodes that have analytical value — items with single source, export controls, concentration risk, or active shortage
- **Don't over-build**: No need to create nodes for commodity items with 10+ suppliers and no concentration risk

### Querying the Product/Material Layer

```python
# "What companies are affected if DDR4 supply is disrupted?"
ddr4_node = 'DEV_DDR4_DRAM'
users = [t for s, t, d in edges if s == ddr4_node and d['type'] == 'input_to']

# "What raw materials does TSMC ultimately depend on?"
# Trace: TSMC <- L1 materials <- L0 resources
tsmc_materials = [s for s, t, d in edges if t == '2330' and d['type'] == 'input_to']
for mat in tsmc_materials:
    resources = [s for s, t, d in edges if t == mat and d['type'] == 'raw_material_for']

# "Which items are currently in critical_shortage?"
critical = [n for n in nodes if n.get('current_status') == 'critical_shortage']
```

---

## 🔴 Deep Graph Analysis Protocol (MANDATORY)

The graph_intel JSON is a starting point, NOT the analysis. You MUST perform deep traversal:

### Step 1: Noise Filtering

Graph data contains noise nodes from OCR/extraction artifacts (e.g., "營收季減", "員工", "進货净额", "季增至", "的占比約為"). **Before any analysis, filter these out:**

```python
NOISE_PATTERNS = ['營收', '員工', '公司', '季增', '季減', '占比', '進货', '進貨', '年成長', '英語課']
def is_noise(node_name):
    return any(p in str(node_name) for p in NOISE_PATTERNS) or len(str(node_name)) < 2
```

### Step 2: Tier 2-3 Supply Chain Traversal

Do NOT stop at Tier 1. Trace at least 2 layers in both directions:

```
Target Company
  ├── Tier 1 Suppliers (direct)
  │     ├── Tier 2 Suppliers (suppliers' suppliers)
  │     └── Tier 2 Events (events affecting T1 suppliers)
  ├── Tier 1 Customers (direct)
  │     ├── Tier 2 Customers (customers' customers)
  │     └── Tier 2 Events (events affecting T1 customers)
  └── Direct Events (events → target company)
```

**Why this matters:** A company with no direct event exposure may be heavily affected through its supply chain. Example: 聯亞(3081) has no direct memory cycle exposure, but its customer 聯鈞(3450) connects to TSMC(2330) and ultimately to NVIDIA — revealing 聯亞's position in the NVIDIA silicon photonics ecosystem.

### Step 3: Event Cross-Referencing

For EACH event node in the graph (type="event"):
1. Check if the event directly connects to the target company
2. Check if the event connects to ANY Tier 1-2 supply chain partner
3. For indirect connections, assess the **transmission mechanism** — how does the event propagate through the supply chain to affect the target?

**Output format for report:**

| Event | Category | Impact | Transmission Path |
|-------|----------|--------|-------------------|
| [Direct events] | | 🟢/🔴/🟡 受益/受害/中性-高/中/低 | Direct connection |
| [Indirect events] | | 🟢/🔴/🟡 | Via [T1 partner] → [mechanism] |

### Step 4: Structural Pattern Recognition

After traversal, classify the company's supply chain structure:

| Pattern | Description | Investment Implication |
|---------|-------------|----------------------|
| **末端通路商** | Low bc, few customers, distributor role | No structural moat, pure cycle play |
| **兩端集中、中間壟斷** | Concentrated suppliers AND customers, but monopoly in middle | Strong pricing power but high concentration risk |
| **策略股東加分** | Major industry players as shareholders | Preferential access + strategic alignment |
| **分散平衡型** | Many suppliers, many customers, moderate bc | Stable but no pricing power premium |
| **瓶頸壟斷型** | High bc + high margin + few alternatives | Strongest investment position |

### Step 5: Comparative Event Impact

When analyzing multiple companies, the SAME event often affects them DIFFERENTLY based on their supply chain role:

Example: Samsung DDR5 expansion
- **Distributor** (青雲): 受害 — supply easing reduces Micron's pricing premium
- **Module maker** (宇瞻): 受益 — more DDR5 supply eases procurement constraints

**Always note these asymmetries in the report.** They reveal which companies are structurally advantaged vs. disadvantaged within the same industry.

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

## Logistics Risk Layer — 物流風險層

Supply chain risk isn't just about who makes what — it's about **whether it can physically get there**. A factory in Japan is useless to a fab in Taiwan if the shipping route is blocked.

### Why this matters
- Red Sea disruption (Houthi attacks) → European chemical shipments delayed
- Taiwan Strait tension → ALL Taiwan imports/exports at risk
- China export licensing (indium/germanium) → delays even without a ban
- Factories aren't always in Taiwan — 南電 42% in Kunshan, 力成 in Malaysia, etc.

### Schema: Production Sites on Company Nodes

```json
{
  "id": "8046",
  "name": "南電",
  "production_sites": [
    {"location": "TW-桃園", "pct": 58, "products": ["ABF載板"]},
    {"location": "CN-昆山", "pct": 42, "products": ["ABF載板"]}
  ]
}
```

**Do NOT assume all production is in Taiwan.** Check the annual report for factory locations. Key fields:
- `location`: Country code + city (e.g., "TW-高雄", "CN-昆山", "MY-Penang")
- `pct`: Percentage of total capacity at this site
- `products`: What is made there

### Schema: Logistics on Supply Edges

```json
{
  "source": "Ajinomoto",
  "target": "8046",
  "relations": [{
    "product": "ABF Film",
    "routes": [
      {
        "from": "JP-川崎",
        "to": "TW-桃園",
        "mode": "air|sea|land",
        "chokepoints": ["East China Sea", "Taiwan Strait"],
        "alternative": "air freight viable",
        "route_risk": "medium"
      },
      {
        "from": "JP-川崎",
        "to": "CN-昆山",
        "mode": "sea",
        "chokepoints": ["East China Sea"],
        "alternative": "land via Korea-China ferry",
        "route_risk": "low"
      }
    ]
  }]
}
```

**Same supply edge can have MULTIPLE routes** to different factory sites, with different risk profiles.

### Key Chokepoints to Track

| Chokepoint | Affects | Current Risk | Event Node |
|-----------|---------|-------------|------------|
| **Taiwan Strait** | All TW imports/exports | 🟡 persistent tension | EVT_TAIWAN_STRAIT |
| **Red Sea / Suez** | EU chemicals → TW; TW exports → EU | 🔴 Houthi attacks ongoing | EVT_RED_SEA |
| **Malacca Strait** | ME petrochemicals → TW/CN; SE Asia packaging return | 🟢 stable | — |
| **East China Sea** | JP raw materials → TW/CN (wafers, substrates, gases) | 🟡 CN-JP tensions | — |
| **South China Sea** | CN raw materials → TW (indium, germanium); TW → CN customers | 🟡 territorial disputes | — |

### Transport Mode Risk

| Mode | Risk Profile | Typical Cargo |
|------|-------------|---------------|
| **Air freight** | Low route risk (avoids sea chokepoints), but expensive | High-value: InP wafers, ASML parts, IC samples |
| **Sea freight** | Exposed to chokepoints, 2-6 week transit | Bulk: chemicals, silicon wafers (large qty), finished modules |
| **Land (cross-border)** | Low chokepoint risk but customs/regulatory delays | CN↔TW not applicable; CN↔VN, CN↔KR possible |

**Rule of thumb:** If primary_mode = "air", sea chokepoint risk is low. Only flag sea-route chokepoints for edges where mode = "sea".

### When to Build Logistics Data

- **During investigation**: When analyzing a company, check its annual report for factory locations. Add `production_sites` to the node.
- **During Tier 1 supply edge review**: For key supply relationships (especially raw materials, chemicals, substrates), infer the shipping route from origin country → factory location. Add `routes` to the edge.
- **Priority**: Focus on edges where the product is heavy/bulky (chemicals, wafers) AND the route crosses a known chokepoint. High-value/low-volume items (IC designs, licensing) can be skipped.

### Integration with Event Impact Assessment

When evaluating a chokepoint event (e.g., EVT_RED_SEA), query all edges with that chokepoint in their `routes.chokepoints` array:

```python
for e in edges:
    for r in e.get('relations', []):
        for route in r.get('routes', []):
            if 'Red Sea' in route.get('chokepoints', []):
                print(f"{e['source']} → {e['target']}: {route['route_risk']}")
```

This directly links geopolitical events to specific supply relationships with quantifiable exposure.

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
