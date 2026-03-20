# Supply Chain & Value Chain Investigation Playbook

**Core principle:** A supply chain investigation is not about listing companies that do X. It is about tracing how money flows when X happens — who earns more, who earns less, and where the bottlenecks concentrate profit. The investigation starts from a topic but must expand outward until you've mapped every stakeholder whose economics change because of that topic.

**Source priority:** Start with customs/trade databases and company filings. Import/export records, shipping data, and regulatory filings are primary evidence of actual supply chain relationships. News articles about "partnerships" are announcements — verify them in trade data before citing.

**Product/Material layer:** The graph uses a 4-layer hierarchy (L0 Resource → L1 Material → L2 Device → L3 Module) to represent products and raw materials as independent nodes. See `playbook-investment-graph.md` → "Product & Material Layer" for the full schema. When tracing chains, create product/material nodes for items that are bottlenecks, monopolized, or under export control.

---

## The Chain-Tracing Method

The fundamental analytical operation is: **for every node you discover, ask three questions before moving on:**

1. **Upstream**: Who are their top 3 suppliers? What do they supply? What % of cost?
2. **Downstream**: Who are their top 3 customers? What do they buy? What % of revenue?
3. **Lateral**: Who else does the same thing? (competitors) Who does the adjacent thing? (substitutes)

Each answer produces new nodes. Apply the same three questions to each new node. Continue until:
- You reach raw material extraction (upstream terminus)
- You reach end consumers or final deployment (downstream terminus)
- The marginal information from one more layer is negligible

This is not optional — it is the core loop. An investigation that stops after one layer has mapped a list, not a supply chain.

### Expansion Depth Guide

| Investigation type | Minimum upstream layers | Minimum downstream layers |
|---|---|---|
| Single company | 2 (to Tier 2 supplier) | 2 (to customer's customer) |
| Technology/theme investigation | 3-4 (to raw materials) | 3-4 (to end deployment) |
| Geopolitical supply chain risk | 4+ (to mineral/resource origin) | 2+ (to strategic end-use) |

### The Standard Node Investigation Checklist

Every node in the chain must answer these before you move to the next node. Unanswered items are recorded as known unknowns — not silently skipped.

| Question | Source priority | If unanswered |
|---|---|---|
| Top 3 suppliers (name, product, %) | Annual report → MOPS → earnings call → OSINT | Mark as gap, attempt de-anonymization |
| Top 3 customers (name, product, %) | Annual report → MOPS → earnings call → OSINT | Mark as gap, attempt de-anonymization |
| Main competitors (name, tech differentiation) | Patent citations → industry report → WebSearch | Mark as gap |
| Capacity: current vs. planned expansion | Earnings call → capex data → construction permits | Mark as gap |
| Technology route (e.g., MBE vs MOCVD) | Patents → conference papers → product specs | Mark as gap |
| Geographic concentration of facilities | Annual report → satellite → job postings | Mark as gap |
| Revenue from the topic under investigation | Segment data → earnings call guidance → analyst estimates | Required for profit flow analysis |

### De-anonymizing Coded Customers/Suppliers

Annual reports often use anonymous codes (e.g., "C06公司", "A01公司"). These are NOT dead ends — use cross-triangulation:

**Revenue triangulation**: If the annual report says "Customer C06 accounts for 33.25% of revenue, application is data center products" — calculate the absolute revenue amount, then search for downstream companies whose procurement from this supplier matches that amount.

**Product-application matching**: The annual report often states what the anonymous customer buys (e.g., "光通訊應用磊晶片"). Cross-reference with known companies in that application space and their procurement patterns.

**Geographic hints**: Revenue geographic breakdown (e.g., "73% China, 9% USA") combined with customer industry narrows candidates dramatically.

**Temporal correlation**: When monthly revenue spikes correlate with a known downstream customer's product launch, the correlation is evidence of a relationship.

**Conference/exhibition co-appearance**: Companies that exhibit together at the same trade shows and list compatible products are likely in a supply relationship.

**Earnings call language analysis**: Executives often drop hints — "a leading North American CSP", "our largest hyperscaler customer". Cross-reference with known CSP/hyperscaler procurement patterns.

If de-anonymization fails after exhausting these methods, record the anonymous code as a node with all known attributes (revenue %, product type, geography). It remains a valid investigation target for future rounds.

---

## Profit Flow Analysis

The purpose of mapping a supply chain is not the map itself — it's understanding **where profit concentrates and how it shifts**. For every node in the chain:

### The Five Economics Questions

1. **Revenue attribution**: How much of this company's revenue comes from the topic under investigation? (e.g., "CPO accounts for 15% of Company X's revenue in 2025, expected 40% by 2027")
2. **Margin structure**: What is the gross/operating margin on the relevant product line? Higher margins = pricing power or scarcity.
3. **Volume sensitivity**: If the topic's TAM doubles, does this company's relevant revenue double? Or is it capped by capacity?
4. **Substitutability**: If this company disappeared, how easily could the chain route around them? (1 = easy substitution, 5 = irreplaceable bottleneck)
5. **Direction of change**: Is this company gaining or losing share in the chain? Why?

### Bottleneck Identification

Bottlenecks are where profits concentrate. Structural signatures:

| Signal | What it means | Where to look |
|---|---|---|
| Few suppliers, many customers | Seller's market — pricing power | Count unique upstream vs downstream edges |
| Long lead times | Capacity-constrained | Earnings calls, industry reports |
| High switching cost | Lock-in effect | Technical specifications, certification requirements |
| Capacity expansion lag | Years to add supply | Fab construction timelines, equipment lead times |
| Geographic concentration | Single-region dependency | Node locations vs. geopolitical risk |

When you find a bottleneck, trace FURTHER upstream (what constrains the bottleneck?) and FURTHER downstream (who suffers most?).

### Profit Flow Map

After completing the chain trace, construct a profit flow summary:

```
Topic: [e.g., CPO]
Total addressable market (TAM): [estimate for target year]

Layer-by-layer profit distribution:
  Raw materials (Tier -3): ~X% of value captured
  Components (Tier -2): ~Y% of value captured
  Sub-assembly (Tier -1): ~Z% of value captured
  Core product (Tier 0): ~W% of value captured
  Integration (Tier +1): ~V% of value captured
  System (Tier +2): ~U% of value captured

Bottleneck nodes (pricing power holders):
  [Node A]: substitutability=5, expanding margin, capacity sold out through 2027
  [Node B]: sole source for [critical input], 18-month lead time for new capacity

Losers (displaced by this topic):
  [Node X]: loses $Y revenue as [old technology] is replaced
```

---

## Value Chain Expansion: Not Just the Keyword

When the user asks about a topic (e.g., "CPO"), resist the urge to only investigate companies that directly produce CPO. The correct scope is: **everyone whose economics change because CPO exists.**

### Expansion categories

**Direct participants** (Tier 0): Companies that manufacture the core technology. Often NOT the best investments because the market has already priced them in.

**Upstream chain** (Tier -1, -2, -3...): Each layer back toward raw materials.
- Example: CPO → CW Laser → InP epitaxy → InP substrate → high-purity indium → indium refining → zinc mine byproduct

**Downstream chain** (Tier +1, +2, +3...): Each layer forward toward end deployment.
- Example: CPO → optical module → switch/NIC → server rack → data center → cloud service

**Adjacent enablers**: Essential but non-obvious participants.
- Equipment makers, testing/metrology, specialty chemicals, design tools, packaging/interconnect

**Indirect beneficiaries**: Second-order effects.
- Complementary products, infrastructure providers, service providers

**Losers and displaced incumbents**: Companies that lose revenue or margin.
- Incumbent technology being replaced, geographic losers, weakened competitive moats

### Completeness self-check

After mapping, ask: "If I explained this topic to someone who knows nothing about it, would my map show them every company that makes money from it, loses money from it, or could make/lose money from it in the future?" If no, go back and expand.

---

## Physical Supply Chain Mapping

| Layer | What to Map | Sources |
|---|---|---|
| 1. Direct suppliers/customers | Who supplies raw materials? Who buys the end product? | Import/export records, annual reports, regulatory filings, industry databases |
| 2. Logistics infrastructure | Shipping routes, warehouses, distribution centers, ports | MarineTraffic, FlightRadar24, satellite imagery |
| 3. Critical dependencies | Single points of failure | Cross-reference supplier lists from multiple competitors |
| 4. Geographic concentration risk | Facility locations vs. political/disaster risks | Company filings, satellite imagery, risk maps |

## Trade Flow Anomaly Detection

- **Unusual trade routes**: Goods transiting through a third country unnecessarily — sanctions evasion or tariff circumvention indicator.
- **Volume-price mismatches**: Import volumes vs. declared values — money laundering or smuggling indicator.
- **Sudden trade partner switches**: Procurement shifting from Country A to Country B — investigate why.
- **Re-export patterns**: Products exported to Country B appearing in sanctioned Country C.

## Taiwan/Asia-Specific Supply Chain Intelligence

- **半導體供應鏈**: TSMC/UMC/ASE ecosystem — capacity allocations, fab construction, customer wins.
- **年報匿名客戶/供應商**: Use de-anonymization methods above for coded names.
- **中國供應鏈轉移**: Track through construction permits, job postings, customs data shifts.
- **經濟部貿易統計**: Taiwan import/export statistics by product code and country.
- **MOPS (公開資訊觀測站)**: Monthly revenue, material information, annual reports.
- **法說會逐字稿**: Earnings call transcripts reveal hints that annual reports anonymize.
- **專利引用分析**: Patent citations reveal technology dependency chains.

## Technology Supply Chain

- **Semiconductor dependency mapping**: Foundry relationships, IP block dependencies, EDA tools.
- **Equipment supply chain**: Multi-year lead times, itself a supply chain worth tracing.
- **Cloud infrastructure dependency**: Single-cloud vs multi-cloud concentration risk.
- **Open source dependency chains**: Critical OSS packages = systemic supply chain risk.

---

## Investigation Output: The Value Chain Map

The final deliverable is a **directed graph with profit attribution**:

Node attributes:
```
{
  company_name, stock_ticker,
  role_in_chain: "Tier -2 supplier / InP substrate",
  revenue_from_topic: "NT$ X (Y% of total revenue)",
  margin_on_topic: "gross margin ~Z%",
  substitutability: 1-5,
  bottleneck_score: 1-5,
  direction: "gaining / stable / losing share",
  key_risk: "concentrated in one Hsinchu facility"
}
```

Edge attributes:
```
{
  source -> target,
  relationship: "supplies InP epitaxy wafers",
  volume: "~X per year",
  dependency: "sole source" or "2 alternatives exist",
  price_trend: "rising due to capacity shortage"
}
```

This enables graph algorithms to identify bottlenecks, single points of failure, and profit concentration zones computationally.

---

## Event Nodes in the Supply Chain Graph

The graph contains event nodes (type="event") representing external forces.
When tracing supply chains, check if any node in the chain is connected to
active events — this reveals hidden vulnerabilities.

Query: for u, v, d in G.in_edges(node, data=True):
    if G.nodes[u].get('type') == 'event': ...

See `playbook-investment-graph.md` for full event node schema.
