# Investment Value Analysis Playbook — 投資價值分析方法論

**Core principle:** PE is a result, not the starting point. The starting point is: has the company's role in the industry changed? Is its pricing power strengthening or weakening? Can price increases be sustainably converted to profit? Only after answering these structural questions should you reference any valuation metric — and even then, valuation is supplementary, never primary.

> This playbook was distilled from iterative real-world analysis sessions on Taiwan semiconductor supply chain stocks (ABF substrate, memory). Every principle below was stress-tested against actual market conditions and corrected through multi-round debate.

---

## The Three Questions (in priority order)

Every investment investigation must answer these three questions. They are ordered by importance — do not skip to Q3 before Q1 and Q2 are resolved.

### Q1: Is the company's industry role changing?

If the role has changed, **all historical valuation frameworks are invalid.** You cannot use a past cycle's PE range to value a company whose position in the value chain is fundamentally different today.

**How to detect role change:**

| Signal | Example | Implication |
|--------|---------|-------------|
| Demand mix shift | ABF substrates: PC 70% (2015) → 15% (2030), AI <5% → 75% | Customer base is completely different — past cycle behavior won't repeat |
| Per-unit value increase | ABF layer count: 8L (PC CPU) → 20L+ (AI GPU) | Same product category but radically higher ASP and technical barrier |
| Bottleneck emergence | T-Glass monopoly (Nittobo sole source), ABF Film monopoly (Ajinomoto 99%) | Company moves from "replaceable supplier" to "irreplaceable chokepoint" |
| Customer switching cost increase | Substrate qualification: 6-12 month cycle, 20L+ yield sensitivity | Lock-in strengthens over time as complexity rises |
| BOM position shift | ABF substrate: <5% of GPU BOM but 100% critical for shipment | "Low cost, high impact" = perfect pricing power position |

**If you find 3+ of these signals, declare the role has changed and explicitly discard historical cycle comparisons.**

### Q2: Is pricing power strengthening or weakening?

Pricing power is not about whether prices are going up today. It's about whether the **structural conditions** that support price increases are intact, strengthening, or eroding.

**The Pricing Power Checklist:**

For each factor, assess current status (🟢 intact / 🟡 weakening / 🔴 broken):

| Factor | What to check | Red flag |
|--------|--------------|----------|
| **Raw material monopoly** | Is the critical input controlled by 1-2 suppliers? Is capacity expanding? | New entrant breaks monopoly, or monopolist announces major expansion |
| **Capacity expansion timeline** | How long to add new supply? (Build + qualify + ramp) | Lead time shrinking below 12 months |
| **Demand durability** | Is demand from capex commitments (durable) or consumer sentiment (volatile)? | Cloud giants cut AI capex guidance |
| **Customer concentration of alternatives** | How many qualified suppliers exist globally? | New supplier achieves qualification |
| **Substitute technology** | Is there a credible replacement? What's its timeline? | Substitute enters pilot production |
| **Contract structure** | Long-term agreements (LTA) vs. spot pricing? | Shift from spot to LTA may limit upside |
| **Customer willingness to pay** | Does the component cost matter to the customer's economics? | Customer begins aggressive cost-down negotiations |

**Count the green lights.** If 6-7/7 are green, pricing power is robust. If 2+ turn yellow, investigate deeper. If any turn red, reassess the entire thesis.

### Q3: Can price increases convert to profit efficiently?

Price increases don't automatically equal profit growth. The conversion depends on:

**Operating leverage position:**
- Fixed cost ratio (depreciation, labor) — higher = stronger leverage
- Current utilization rate vs. breakeven — above breakeven, incremental revenue drops almost entirely to bottom line
- Where in the utilization curve: 60% (still losing money) vs. 85%+ (profit machine)

**Contract mix (critical for cyclical industries):**
- Non-LTA (spot/short-term) percentage — higher = faster price reflection
- LTA percentage — higher = more stable but slower to capture upside
- Example: Company A (70% non-LTA) captures 70% of quarterly ASP increase immediately; Company B (70% LTA) captures only 30%

**Cost pass-through ability:**
- Can the company pass raw material cost increases to customers? Or is it squeezed?
- Does it have vertical integration that insulates from upstream price spikes?

**Depreciation trajectory:**
- Is capex rising? New depreciation will eat into margins in 2-3 years
- Is the profit surge sustainable through the depreciation ramp?

---

## What NOT to Do

### ❌ Do not start from PE

PE is calculated last, referenced briefly, and never used as the primary argument for or against an investment. For cyclical companies:
- **Low PE at the peak is a trap** — EPS is temporarily inflated, PE looks cheap, but EPS is about to collapse
- **High PE at the trough is misleading** — EPS is temporarily depressed, PE looks expensive, but EPS is about to recover
- **PEG for cyclicals is nonsensical** — Growth rates from trough-to-peak are 100-300%, making PEG look absurdly low, but growth is not sustainable

### ❌ Do not use institutional estimates older than 6 months

Stock prices and fundamentals can move 50-100% in 6 months for cyclical stocks. An estimate made when the stock was at 100 is meaningless when the stock is at 500. Rules:
- **Tag every cited estimate with its date and the stock price at that time**
- **Discard any estimate where the stock has moved >30% since publication**
- **Prefer the most recent 2-3 estimates only**

### ❌ Do not use past cycle peaks to value a company whose role has changed

If the company was a "generic PCB supplier" in 2022 and is now an "irreplaceable AI infrastructure bottleneck" in 2026, the 2022 PE range (10-25x) is not a valid reference. The comparison is:
- Wrong: "2022 peak PE was 15x, so current 50x is overvalued"
- Right: "The company's role has changed — is the new role's pricing power and margin profile sustainable enough to support the current valuation?"

### ❌ Do not present only bull or only bear case

Every investment analysis must include both sides. Structure as:
- **Bull case**: What has to go right?
- **Bear case**: What could go wrong?
- **Key debate**: What is the single most important disagreement between bulls and bears?

---

## The Monitoring Framework

Instead of a static "buy/sell" conclusion, deliver a **monitoring framework** — a set of conditions the investor should track to know whether the thesis remains valid.

### Template: Support Factor Dashboard

| Support Factor | Current Status | Failure Condition | Check Frequency | Data Source |
|---------------|---------------|-------------------|-----------------|-------------|
| [Factor 1] | 🟢/🟡/🔴 | [Specific trigger] | [Weekly/Monthly/Quarterly] | [Where to look] |
| ... | ... | ... | ... | ... |

Rules:
- Minimum 5 factors, maximum 10
- Each factor must have a **specific, observable** failure condition (not "things get worse")
- Each factor must have a data source the investor can actually check
- **When any factor turns red, the thesis needs reassessment — not necessarily exit, but reassessment**

---

## Multi-Company Comparison Framework

When comparing multiple companies in the same industry, do NOT compare PE ratios. Compare:

| Dimension | What it reveals | How to measure |
|-----------|----------------|----------------|
| **Pricing power** | Who captures the most value from price increases? | Non-LTA %, raw material self-sufficiency, customer lock-in |
| **Profit conversion speed** | Who turns revenue growth into EPS growth fastest? | Operating leverage, utilization rate, contract mix |
| **Moat depth** | Whose competitive position is most defensible? | Technology barrier (layer count capability), key partnerships, customer qualification status |
| **Downside protection** | Who falls least in a downturn? | Business diversification, fixed cost structure, cash reserves |
| **Structural position** | Who is best positioned for the role transformation? | AI revenue mix, customer composition, capacity for next-gen products |

**The right question is not "who is cheapest" but "who occupies the most advantageous structural position in the industry's transformation."**

---

## Integration with Supply Chain Graph

Always query the knowledge graph (`supply_chain_mcp/data/supply_chain.json`) for:

1. **Customer concentration risk** — Is >30% of revenue from one customer?
2. **Supply chain position verification** — Confirm OSINT-claimed customer/supplier relationships against graph edges
3. **Cross-company linkages** — Shared customers, shared suppliers, cross-holdings
4. **Competitive mapping** — Who else serves the same customers?
5. **Anonymous customer de-anonymization** — Use graph adjacency + revenue triangulation

Graph data provides **structure**; web search provides **dynamics**. Neither alone is sufficient.

---

## Structural Valuation Range — 結構性估值區間

While static target prices are unreliable for cyclical stocks, investors need a price reference. The solution is a **Structural Valuation Range** — derived from the Three Questions analysis, not from mechanical PE application.

### Step 0: Current Price Anchor (MANDATORY FIRST STEP)

**Before ANY analysis, fetch the current stock price via WebSearch.** Every subsequent assessment is relative to this anchor.

```
Current price: [XXX] TWD (date: YYYY-MM-DD)
52-week range: [low] - [high]
Price position: [near low / mid-range / near high / above 52w high]
```

Tag every cited analyst estimate with: (estimate date, stock price at that date). **Discard any estimate where stock has moved >30% since publication.**

### Step 1: Derive EPS Range from Structural Analysis (not from analyst consensus)

Use the Three Questions to bound the EPS range:

| Scenario | Q1 Role | Q2 Pricing Power | Q3 Profit Conversion | Resulting EPS |
|----------|---------|-------------------|----------------------|---------------|
| **Bull** | Role transformed + all green lights | 6-7/7 🟢 | High leverage, favorable mix | [highest credible EPS] |
| **Base** | Role partially changed | 4-5/7 🟢 | Normal conversion | [consensus-like EPS] |
| **Bear** | Role unchanged / cycle peaks | 2-3/7 🟢 or 🔴 appearing | Margin compression | [trough EPS] |

The EPS range comes from **what pricing power and profit conversion can structurally support**, not from analyst spreadsheets.

### Step 2: Determine Appropriate Multiple Range

The multiple is determined by the Q1 role assessment:

| Q1 Result | Multiple Source | Example |
|-----------|----------------|---------|
| **Role transformed** (3+ signals) | Comparable companies in NEW role, NOT historical | If company became AI infrastructure bottleneck, compare to other AI infra stocks, not to its own 2022 PE |
| **Role partially changed** | Blend of historical and new-role comparables | Weight 50/50 |
| **Role unchanged** | Historical cycle range is valid | Use past cycle PE band |

### Step 3: Calculate Structural Valuation Range

```
Bull range:  Bull EPS × New-role upper multiple = [price]
Base range:  Base EPS × Blended multiple = [price]
Bear range:  Bear EPS × Historical trough multiple = [price]

Weighted midpoint: Bull × 25% + Base × 50% + Bear × 25% = [price]
```

### Step 4: Position Assessment

```
Current price vs. range:
  Below Bear range     → Deeply undervalued (rare — check if something is broken)
  Bear to Base         → Attractive entry zone
  Base to Bull         → Fairly valued, hold if owned
  Above Bull           → Overvalued / requires Bull case to be fully correct
  Way above Bull       → Speculative / momentum only — not supported by structural analysis
```

### Step 5: Dynamic Adjustment Rules

The range is NOT static. Adjust when monitoring dashboard factors change:

| Dashboard Change | Range Adjustment |
|-----------------|-----------------|
| Factor turns 🟢→🔴 | Shift entire range DOWN by removing that factor's contribution |
| New catalyst confirmed | Shift Bull case UP |
| Competitor enters market | Compress range (lower Bull, raise Bear) |
| Role transformation confirmed by new data | Discard historical Bear floor, use new-role floor |

**The valuation range is a LIVING output tied to the monitoring dashboard, not a one-time calculation.**

---

## Future Development Path Projection — 未來發展路徑推測

Every investment analysis must include a **structured projection of possible development paths** over the next 2-3 years. This is NOT a prediction — it is a map of branching possibilities with triggers that determine which path materializes.

### Why this matters

Static valuation says "the stock is worth X." Development path projection says "the stock is worth X today, but could become worth Y or Z depending on which path unfolds." This is far more actionable — it tells the investor what to watch for and when to reassess.

### Template: Development Path Map

For each of 3 scenarios (Bull/Base/Bear), construct a **timeline with milestones**:

```
Scenario [A/B/C]: [Name] (probability: XX%)

2026 H1: [What happens first — specific event/milestone]
2026 H2: [What follows — cause-effect chain from H1]
2027 H1: [Inflection point or continuation]
2027 H2: [Where this path leads]
2028+:   [Long-term structural outcome]

→ Resulting EPS trajectory: [year-by-year]
→ Resulting valuation range: [price]
→ Trigger that confirms this path: [specific observable event]
→ Trigger that invalidates this path: [specific observable event]
```

### Rules for development path projection:

1. **Each path must be internally consistent** — don't mix bull assumptions for revenue with bear assumptions for margins
2. **Paths must branch from specific decision points** — "Q2 2026 customer certification result" is a branch point; "things go well" is not
3. **Include the company's OWN strategic moves** — new factories, new products, M&A plans, geographic expansion
4. **Include external forces** — industry cycle, competitor actions, regulatory changes, technology shifts
5. **Time-stamp everything** — "sometime in 2027" is too vague; "2027 Q1 based on 18-month fab construction timeline" is useful
6. **Identify the single most important branch point** — the one event/decision that most changes the outcome

### Integration with valuation

The Structural Valuation Range (Steps 1-4) should be derived FROM the development paths, not independently. Each scenario's EPS comes from tracing the path's timeline to its financial outcome.

---

## Price Deviation Investigation — 價格偏離調查

**When the current stock price is >50% above the Bull case OR >30% below the Bear case, a mandatory Price Deviation Investigation must be conducted.** The purpose is to determine WHY the market disagrees with the structural analysis — the market may know something the analyst doesn't, or it may be wrong.

### When to trigger

| Condition | Action |
|-----------|--------|
| Price > Bull × 1.5 | 🔴 MANDATORY deviation investigation |
| Price > Bull × 1.0 | 🟡 Recommended deviation check |
| Price within Bear-Bull range | ✅ No investigation needed |
| Price < Bear × 0.7 | 🟡 Recommended deviation check (may be broken) |

### Investigation procedure

**Step 1: Identify the deviation source** — Ask "What would the market need to believe to justify this price?"

Calculate the implied EPS: `Implied EPS = Current Price / Reasonable PE for this industry`
Compare with your structural EPS estimate. The gap is the "belief gap."

**Step 2: Search for the hidden catalyst** — The market may be pricing in something you missed:

- WebSearch: `"{company name}" 利多 催化劑 題材 2026`
- WebSearch: `"{company name}" insider buying 內部人買進`
- WebSearch: `"{company name}" 併購 合併 私有化 收購`
- WebSearch: `"{company name}" new product 新產品 新客戶 大單`
- Check: Is a parent company or major shareholder driving speculative interest?
- Check: Is there a sector-wide theme (e.g., memory supercycle) creating spillover?

**Step 3: Classify the deviation**

| Classification | Description | Analyst action |
|---------------|-------------|----------------|
| **Justified gap** | Market has information analyst missed (confirmed new catalyst, insider buying pattern, M&A rumor with substance) | Update the structural analysis to incorporate the new information; revise Bull case upward |
| **Theme spillover** | Stock is riding a sector wave without company-specific justification (e.g., memory concept stock for a non-memory company) | Flag as speculative premium; note the theme's duration risk |
| **Narrative bubble** | Price is driven by retail momentum, social media hype, or misidentification (e.g., confused with another company) | Flag as 🔴 extreme risk; note that structural analysis cannot support current price |
| **Structural miss** | Analyst's framework is missing a key variable (e.g., underestimated the role transformation) | Re-evaluate Q1/Q2/Q3 from scratch with new lens |

**Step 4: Document the finding**

In the report, add a section: `## 價格偏離分析 (Price Deviation Investigation)`

```
| Item | Value |
|------|-------|
| Current price | XXX |
| Structural Bull | YYY |
| Deviation | +ZZ% |
| Implied market belief | "Market is pricing EPS of [N], which requires [assumption]" |
| Deviation source | [Justified / Theme spillover / Narrative bubble / Structural miss] |
| Hidden catalyst found? | [Yes: description / No: pure speculation] |
| Recommendation | [Adjust analysis / Flag as speculative / Maintain original thesis] |
```

**This step prevents two failure modes:**
1. **Dismissing the market too quickly** — "It's just speculation" when actually the market has spotted a real catalyst you missed
2. **Accepting the market too easily** — "The market must be right" when actually the price is a bubble with no structural support

---

## Geopolitical & Major Event Impact Assessment — 地緣政治與重大事件衝擊評估

**Every investment analysis MUST include a supply chain stress test against current major global events.** This is not optional — a company analysis that ignores the geopolitical environment is like a ship navigation that ignores weather.

### Why this is mandatory

Taiwan sits at the intersection of multiple geopolitical fault lines. A company's structural position (Q1-Q3) can be invalidated overnight by:
- Trade policy changes (tariffs, export controls, entity lists)
- Supply chain disruptions (shipping routes, raw material embargoes)
- Geopolitical escalation (Taiwan Strait, Middle East, Russia-Ukraine)
- Regulatory shifts (carbon taxes, data sovereignty, forced localization)

### Step 1: Scan current major events (MANDATORY WebSearch)

Before finalizing any analysis, run ONE WebSearch to capture the current geopolitical landscape:

`WebSearch: "台灣 供應鏈 地緣政治 關稅 2026 {current month}"`

Build a **Current Event Registry** — a simple table of active global events that could affect Taiwan supply chains:

| Event | Status | Affected supply chains | Impact direction |
|-------|--------|----------------------|-----------------|
| US-China trade war / tariffs | [active/escalating/de-escalating] | Semiconductor, electronics, chemicals | [positive/negative for subject] |
| China export controls (rare earth, gallium, germanium, tungsten) | [active] | Semiconductor materials, LED substrates, sputtering targets | [risk level] |
| Taiwan Strait tensions | [current status] | ALL Taiwan companies | [probability × impact] |
| Red Sea / Middle East shipping | [current status] | Oil-dependent industries, shipping costs | [impact] |
| US CHIPS Act / reshoring | [current status] | Semiconductor, advanced packaging | [opportunity/threat] |
| EU CBAM / carbon regulation | [current status] | Steel, cement, chemicals | [compliance cost] |
| [Other current events] | | | |

### Step 2: Company-specific impact assessment

For the company under investigation, map EACH event to its specific supply chain:

**Template: Event Impact Matrix**

| Event | Upstream impact | Downstream impact | Company-specific exposure | Severity | Timeline |
|-------|----------------|-------------------|--------------------------|----------|----------|
| [Event 1] | [Which suppliers/materials are affected?] | [Which customers are affected?] | [% of revenue/cost at risk] | 🟢/🟡/🔴 | [Immediate/6mo/12mo+] |
| [Event 2] | ... | ... | ... | ... | ... |

### Step 3: Use the supply chain graph

Query the knowledge graph (`supply_chain_mcp/data/supply_chain.json`) to identify:

1. **Upstream vulnerability**: Trace Tier 2/3 suppliers — are any in geopolitically sensitive regions?
   - China-sourced materials (rare earth 93%, tungsten 80%, polysilicon 80%)
   - Single-country dependencies (Japan for specialty chemicals, Korea for memory)
   - Shipping route dependencies (Strait of Hormuz, Suez Canal, Taiwan Strait)

2. **Customer concentration by geography**: Use `revenue_by_geography` and `china_revenue_pct` fields
   - China revenue >30% = 🔴 high geopolitical risk
   - China revenue 10-30% = 🟡 moderate
   - China revenue <10% = 🟢 low

3. **Cross-reference with graph edges**: Which of the company's confirmed customers/suppliers are themselves exposed to geopolitical events?
   - Example: If Company A supplies NVIDIA, and NVIDIA faces China export restrictions, Company A is indirectly affected

### Step 4: Beneficiary vs. Victim classification

Every major event creates BOTH winners and losers. Classify the subject company:

| Classification | Description | Example |
|---------------|-------------|---------|
| **Direct beneficiary** | Event directly increases demand for company's products | US-China decoupling → Taiwan OSAT gets orders diverted from China |
| **Indirect beneficiary** | Event removes a competitor or creates scarcity | China rare earth export ban → non-China material suppliers gain pricing power |
| **Neutral** | Event has no material impact | Middle East tensions on a domestic-focused food company |
| **Indirect victim** | Event affects company's customers or suppliers | China AI chip ban → reduces demand for packaging services |
| **Direct victim** | Event directly restricts company's operations | Export controls on company's products; tariffs on company's exports |

### Step 5: Integrate into valuation

Geopolitical events should adjust the Structural Valuation Range:

- If company is a **direct beneficiary**: Shift Bull case probability UP by 5-10%
- If company is a **direct victim**: Shift Bear case probability UP by 10-20%
- If company has **China revenue >40%**: Add a "Geopolitical Bear" scenario at 50% of current Bear
- If company's Tier 3 raw materials are **>80% from one geopolitically sensitive country**: Flag as 🔴 in monitoring dashboard

### Step 0 (MANDATORY): Fresh Event Scan via WebSearch

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

**After building the Fresh Event Registry, ALSO check these structural themes** (these change slowly but must be verified):

1. US-China trade/tech war — tariffs, entity lists, export controls (current status?)
2. China resource export controls — rare earth, gallium, germanium, tungsten, antimony (any new additions?)
3. Taiwan Strait tensions — current military activity level, political signals
4. Semiconductor reshoring — CHIPS Act, EU Chips Act, Japan subsidies (any new announcements?)
5. Energy/shipping disruptions — Red Sea, Strait of Hormuz, oil prices (current status?)
6. Carbon regulation — EU CBAM, Taiwan carbon fee (implementation timeline?)
7. Regional manufacturing shifts — India, Vietnam, Mexico, Thailand (new incentives?)
8. Currency/monetary policy — Fed rate decisions, TWD/USD, JPY weakness (impact on exporters?)

**The combination of fresh WebSearch results + structural theme verification ensures the geopolitical assessment is CURRENT, not based on months-old assumptions.**

---

## Report Output Standards

### Required sections (investment analysis):

1. **Current price anchor** — Stock price fetched via WebSearch BEFORE any analysis (mandatory first step)
2. **One-line verdict** — Direct answer to "is there investment value at current price?"
3. **Industry role assessment (Q1)** — Has it changed? Evidence. 3+ signals = role transformed.
4. **Pricing power dashboard (Q2)** — Factor-by-factor with 🟢/🟡/🔴
5. **Profit conversion analysis (Q3)** — Operating leverage, contract mix, margin trajectory
6. **Structural Valuation Range** — Bull/Base/Bear with EPS derivation from Q1-Q3, NOT from PE × consensus
7. **Current price position** — Where does current price sit in the range? Is it attractive?
8. **Price Deviation Investigation** — MANDATORY if price >50% above Bull or >30% below Bear.
9. **Geopolitical & Event Impact** — First query event nodes from graph (type="event" edges to this company), then run Fresh Event Scan via WebSearch to catch new events. Build impact matrix. Classify beneficiary/victim.
10. **Future Development Path** — 3 scenarios with timeline, triggers, branch points. Must incorporate geopolitical scenarios from §9.
11. **Supply chain graph findings** — Key relationships, concentration risks, Tier 2/3 geographic exposure
12. **Bull vs. Bear** — Both sides with the key debate identified. Must include a geopolitical bear scenario if China revenue >20% or Tier 3 materials >50% from single sensitive country.
13. **Monitoring framework** — Support Factor Dashboard (min 6 factors, must include at least 1 geopolitical factor with 🟢/🟡/🔴)
14. **Disclaimer** — Mandatory

### What NOT to include:

- PE as primary valuation argument (use structural range instead)
- Analyst estimates older than 6 months or where stock moved >30% since publication
- Historical cycle PE comparisons when role has changed (Q1 = transformed)
- Static "buy at X, sell at Y" without monitoring conditions
- PEG ratios for cyclical stocks

### File output:

- **Format**: MD (Markdown) only. No PDF or HTML needed.
- **Naming**: `{ticker}_{公司名}_investment_analysis.md` or `{theme}_analysis.md`
  - Example: `2330_台積電_investment_analysis.md`, `memory_sector_analysis.md`
  - Always include the company name in Chinese — ticker alone is not human-readable
  - Do NOT add version suffixes like _v2, _v3, _v4 — the file should always represent the latest analysis

### Post-analysis: Write back to graph (MANDATORY)

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

### Event nodes in the graph — 事件圖譜

The supply chain graph contains **event nodes** (type="event") representing major external forces that impact companies. These are NOT static — they must be refreshed via WebSearch and updated when status changes.

**9 event categories:**
- `geopolitical` — trade wars, sanctions, military tensions
- `tech_shift` — AI boom, CPO, HBM, EV penetration
- `industry_cycle` — memory supercycle, petrochemical trough, ABF shortage
- `regulation` — carbon tax, housing curbs, IFRS17
- `supply_disruption` — Red Sea, YMTC expansion, CXMT dumping
- `macro` — Fed rates, currency movements
- `corporate` — M&A, exits, capacity expansion
- `demographic` — labor shortage, aging population
- `esg` — conflict minerals, carbon compliance

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

**Event→Company edges:**
```json
{
  "type": "impacts",
  "impact": "beneficiary|victim|neutral",
  "magnitude": "extreme|high|medium|low",
  "description": "How this event affects this company"
}
```

**How to use event nodes during analysis:**

1. **Query which events affect the company:**
   ```python
   for u, v, d in G.in_edges(stock_id, data=True):
       if G.nodes[u].get('type') == 'event':
           print(f"Event: {G.nodes[u]['name']} → impact: {d['relations'][0]['impact']}")
   ```

2. **Check event status (is it escalating or de-escalating?)** — this changes the risk weight

3. **Cross-reference events across companies** — if two companies in the same portfolio are both victims of the same event, that's concentrated event risk

4. **Update events when status changes** — after each WebSearch round, update `status` and `last_updated` on relevant event nodes. If an event resolves, set status="resolved" but keep the node for history.

5. **Create new event nodes** when the Fresh Event Scan (Step 0 of Geopolitical Assessment) discovers events not yet in the graph. Use the schema above and connect to all affected companies.

### Betweenness Centrality interpretation guide

When using graph betweenness centrality (bc), distinguish two types:

| Type | Characteristics | Example | Investment implication |
|------|----------------|---------|----------------------|
| **Infrastructure type** | High bc + high out-degree + low margin | 中鋼 (bc=0.042, 416 edges) | Breadth = many customers but NO pricing power. bc ≠ moat |
| **Bottleneck type** | High bc + moderate degree + high margin | 台積電 (bc=0.036, high margin 60%+) | Depth = irreplaceable position. bc = moat |

**Rule: NEVER cite high bc alone as evidence of investment value. Always check whether it reflects breadth (infrastructure) or depth (bottleneck).**

### Sector comparison template (for multi-company analysis)

When analyzing 3+ companies in the same sector, ALWAYS produce a comparison table:

| Dimension | Company A | Company B | Company C |
|-----------|-----------|-----------|-----------|
| Pricing power (who captures most value?) | | | |
| Profit conversion speed (who turns revenue → EPS fastest?) | | | |
| Moat depth (whose position is most defensible?) | | | |
| Downside protection (who falls least in downturn?) | | | |
| Structural position (who is best positioned for transformation?) | | | |

**The right question is not "who is cheapest" but "who occupies the most advantageous structural position."**
