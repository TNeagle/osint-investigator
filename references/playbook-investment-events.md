# Geopolitical & Event Impact Assessment — 地緣政治與重大事件衝擊評估

**Parent playbook**: `playbook-investment.md` (core Three Questions framework)
**Companion**: `playbook-investment-graph.md` (graph integration, event node schema)

**Every investment analysis MUST include a supply chain stress test against current major global events.** This is not optional — a company analysis that ignores the geopolitical environment is like a ship navigation that ignores weather.

---

## How to use event nodes in the graph

Query graph for type="event" nodes connected to the company BEFORE doing WebSearch.
This gives you known events; WebSearch then catches NEW events not yet in graph.
After analysis, update event node status if changed, and create new event nodes for newly discovered events.

See `playbook-investment-graph.md` for full event node schema and query examples.

---

## Why this is mandatory

Taiwan sits at the intersection of multiple geopolitical fault lines. A company's structural position (Q1-Q3) can be invalidated overnight by:
- Trade policy changes (tariffs, export controls, entity lists)
- Supply chain disruptions (shipping routes, raw material embargoes)
- Geopolitical escalation (Taiwan Strait, Middle East, Russia-Ukraine)
- Regulatory shifts (carbon taxes, data sovereignty, forced localization)

---

## Step 0 (MANDATORY): Fresh Event Scan via WebSearch

**Do NOT rely on a static watchlist.** The geopolitical landscape changes weekly. Every time this playbook is invoked, run a MANDATORY WebSearch to capture the CURRENT state of global events:

```
WebSearch: "國際局勢 供應鏈 衝擊 {current month} {current year}"
WebSearch: "geopolitical risk supply chain {current month} {current year}"
```

From the results, build a **Fresh Event Registry** — a table of events that are ACTIVE RIGHT NOW:

| Event | Status (as of today) | Affected supply chains | Escalating or de-escalating? |
|-------|---------------------|----------------------|------------------------------|
| [From search results] | [Current status] | [Which industries] | [Direction of change] |

**Why fresh search instead of a static list:**
- A static watchlist becomes stale within weeks
- New events emerge constantly (trade deals, sanctions, military incidents, natural disasters)
- The DIRECTION of change matters more than the event itself (escalating = increase risk weight; de-escalating = decrease)
- Events interact with each other in ways a static list cannot capture

---

## Step 1: Scan current major events

After building the Fresh Event Registry, ALSO check these **structural themes** (these change slowly but must be verified):

1. US-China trade/tech war — tariffs, entity lists, export controls (current status?)
2. China resource export controls — rare earth, gallium, germanium, tungsten, antimony (any new additions?)
3. Taiwan Strait tensions — current military activity level, political signals
4. Semiconductor reshoring — CHIPS Act, EU Chips Act, Japan subsidies (any new announcements?)
5. Energy/shipping disruptions — Red Sea, Strait of Hormuz, oil prices (current status?)
6. Carbon regulation — EU CBAM, Taiwan carbon fee (implementation timeline?)
7. Regional manufacturing shifts — India, Vietnam, Mexico, Thailand (new incentives?)
8. Currency/monetary policy — Fed rate decisions, TWD/USD, JPY weakness (impact on exporters?)

**The combination of fresh WebSearch results + structural theme verification ensures the geopolitical assessment is CURRENT, not based on months-old assumptions.**

Build the **Current Event Registry**:

| Event | Status | Affected supply chains | Impact direction |
|-------|--------|----------------------|-----------------|
| US-China trade war / tariffs | [active/escalating/de-escalating] | Semiconductor, electronics, chemicals | [positive/negative for subject] |
| China export controls (rare earth, gallium, germanium, tungsten) | [active] | Semiconductor materials, LED substrates, sputtering targets | [risk level] |
| Taiwan Strait tensions | [current status] | ALL Taiwan companies | [probability x impact] |
| Red Sea / Middle East shipping | [current status] | Oil-dependent industries, shipping costs | [impact] |
| US CHIPS Act / reshoring | [current status] | Semiconductor, advanced packaging | [opportunity/threat] |
| EU CBAM / carbon regulation | [current status] | Steel, cement, chemicals | [compliance cost] |
| [Other current events] | | | |

---

## Step 2: Company-specific impact assessment

For the company under investigation, map EACH event to its specific supply chain:

**Template: Event Impact Matrix**

| Event | Category | Impact Direction | Magnitude | Timeframe | Transmission Path |
|-------|----------|-----------------|-----------|-----------|-------------------|
| [Event] | geopolitical/tech_shift/... | 🟢受益/🔴受害/🟡中性 | 高/中/低 | 即時/Q2-Q3/H2/2027+ | 直接 or 經[公司]→[機制] |

**Impact assessment rules:**
- **高(High)**: Event changes >15% of revenue, margins, or valuation. Examples: export control on 55% China revenue, memory price +90% QoQ
- **中(Medium)**: Event changes 5-15%. Examples: tariff rate changes, competitor capacity shift
- **低(Low)**: Event changes <5%. Examples: currency fluctuation, peripheral supply chain disruption

**Timeframe categories:**
- **即時(Immediate)**: Already priced in or actively affecting operations
- **Q2-Q3 2026**: Will materialize within 3-6 months
- **H2 2026**: Second half of year
- **2027+**: Long-term structural change

### 🔴 Event Net Assessment (MANDATORY)

After building the matrix, provide a **net assessment** summarizing:
1. How many high/medium/low events are positive vs. negative
2. What is the single biggest upside event and single biggest downside event
3. Whether the event environment overall supports or undermines the investment thesis
4. Any **asymmetric events** — where the same event affects the company differently than its competitors

Example:
> **事件淨評估：強正面（4個高度受益事件）。核心風險為Samsung擴產+YMTC NAND放量在H2可能緩解供需。**

---

## Step 3: Use the supply chain graph for geographic + logistics exposure

Query the knowledge graph (`supply_chain_mcp/data/supply_chain.json`) to identify:

1. **Upstream vulnerability**: Trace Tier 2/3 suppliers — are any in geopolitically sensitive regions?
   - China-sourced materials (rare earth 93%, tungsten 80%, polysilicon 80%)
   - Single-country dependencies (Japan for specialty chemicals, Korea for memory)

2. **Customer concentration by geography**: Use `revenue_by_geography` and `china_revenue_pct` fields
   - China revenue >30% = high geopolitical risk
   - China revenue 10-30% = moderate
   - China revenue <10% = low

3. **Cross-reference with graph edges**: Which of the company's confirmed customers/suppliers are themselves exposed to geopolitical events?
   - Example: If Company A supplies NVIDIA, and NVIDIA faces China export restrictions, Company A is indirectly affected

4. **🔴 Logistics risk (shipping route exposure)**

   See `playbook-investment-graph.md` → Logistics Risk Layer for full schema.

   **Do NOT assume all factories are in Taiwan.** Check `production_sites` on the company node. Then for each key supply edge:
   - Identify the actual origin → destination (which factory, not just "Taiwan")
   - Determine transport mode (air = low route risk; sea = check chokepoints)
   - Flag edges that cross known chokepoints (Taiwan Strait, Red Sea, East China Sea, South China Sea, Malacca)

   **When evaluating a chokepoint event** (e.g., Red Sea disruption):
   - Query all supply edges with that chokepoint in `routes.chokepoints`
   - For each match: is the product air-freightable as alternative? If yes, impact is cost increase not disruption. If no (bulk chemicals, large wafer shipments), impact is potential supply halt.
   - Companies with overseas factories may have DIFFERENT risk profiles for the same chokepoint — e.g., 南電 Kunshan factory does NOT depend on Taiwan Strait for Japan raw materials (ships via East China Sea to Shanghai directly)

---

## Step 4: Beneficiary vs. Victim classification

Every major event creates BOTH winners and losers. Classify the subject company:

| Classification | Description | Example |
|---------------|-------------|---------|
| **Direct beneficiary** | Event directly increases demand for company's products | US-China decoupling -> Taiwan OSAT gets orders diverted from China |
| **Indirect beneficiary** | Event removes a competitor or creates scarcity | China rare earth export ban -> non-China material suppliers gain pricing power |
| **Neutral** | Event has no material impact | Middle East tensions on a domestic-focused food company |
| **Indirect victim** | Event affects company's customers or suppliers | China AI chip ban -> reduces demand for packaging services |
| **Direct victim** | Event directly restricts company's operations | Export controls on company's products; tariffs on company's exports |

---

## Step 5: Integrate into valuation

Geopolitical events should adjust the Structural Valuation Range (see `playbook-investment.md`):

- If company is a **direct beneficiary**: Shift Bull case probability UP by 5-10%
- If company is a **direct victim**: Shift Bear case probability UP by 10-20%
- If company has **China revenue >40%**: Add a "Geopolitical Bear" scenario at 50% of current Bear
- If company's Tier 3 raw materials are **>80% from one geopolitically sensitive country**: Flag as red in monitoring dashboard

---

## 9 Event Categories

These categories are used for event nodes in the supply chain graph (see `playbook-investment-graph.md` for schema):

| Category | Description | Examples |
|----------|-------------|---------|
| `geopolitical` | Trade wars, sanctions, military tensions | US-China tariffs, Taiwan Strait, Russia-Ukraine |
| `tech_shift` | Technology paradigm changes | AI boom, CPO, HBM, EV penetration |
| `industry_cycle` | Sector-level supply/demand cycles | Memory supercycle, petrochemical trough, ABF shortage |
| `regulation` | Government policy changes | Carbon tax, housing curbs, IFRS17 |
| `supply_disruption` | Physical supply chain disruptions | Red Sea, YMTC expansion, CXMT dumping |
| `macro` | Macroeconomic forces | Fed rates, currency movements |
| `corporate` | Company-level strategic events | M&A, exits, capacity expansion |
| `demographic` | Population/workforce trends | Labor shortage, aging population |
| `esg` | Environmental/social/governance | Conflict minerals, carbon compliance |
