# Investment Value Analysis Playbook — 投資價值分析方法論

**Prerequisites**: This playbook works with two companion files:
- `playbook-investment-events.md` — Geopolitical & event impact assessment (MANDATORY for every analysis)
- `playbook-investment-graph.md` — Supply chain graph integration (MANDATORY when graph is available)
- `playbook-supply-chain.md` — Chain-tracing method for supply chain depth analysis

Load all three when conducting investment analysis.

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

For each factor, assess current status (green intact / yellow weakening / red broken):

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

### Do not start from PE

PE is calculated last, referenced briefly, and never used as the primary argument for or against an investment. For cyclical companies:
- **Low PE at the peak is a trap** — EPS is temporarily inflated, PE looks cheap, but EPS is about to collapse
- **High PE at the trough is misleading** — EPS is temporarily depressed, PE looks expensive, but EPS is about to recover
- **PEG for cyclicals is nonsensical** — Growth rates from trough-to-peak are 100-300%, making PEG look absurdly low, but growth is not sustainable

### Do not use institutional estimates older than 6 months

Stock prices and fundamentals can move 50-100% in 6 months for cyclical stocks. An estimate made when the stock was at 100 is meaningless when the stock is at 500. Rules:
- **Tag every cited estimate with its date and the stock price at that time**
- **Discard any estimate where the stock has moved >30% since publication**
- **Prefer the most recent 2-3 estimates only**

### Do not use past cycle peaks to value a company whose role has changed

If the company was a "generic PCB supplier" in 2022 and is now an "irreplaceable AI infrastructure bottleneck" in 2026, the 2022 PE range (10-25x) is not a valid reference. The comparison is:
- Wrong: "2022 peak PE was 15x, so current 50x is overvalued"
- Right: "The company's role has changed — is the new role's pricing power and margin profile sustainable enough to support the current valuation?"

### Do not present only bull or only bear case

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
| [Factor 1] | green/yellow/red | [Specific trigger] | [Weekly/Monthly/Quarterly] | [Where to look] |
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

### Sector comparison template (for multi-company analysis)

When analyzing 3+ companies in the same sector, ALWAYS produce a comparison table:

| Dimension | Company A | Company B | Company C |
|-----------|-----------|-----------|-----------|
| Pricing power (who captures most value?) | | | |
| Profit conversion speed (who turns revenue to EPS fastest?) | | | |
| Moat depth (whose position is most defensible?) | | | |
| Downside protection (who falls least in downturn?) | | | |
| Structural position (who is best positioned for transformation?) | | | |

---

## 🔴 Unified Valuation Funnel — 統一估值漏斗

All analysis (Q1 role, Q2 pricing power, Q3 profit conversion, events, risks) MUST flow into ONE valuation. No section exists in isolation.

### Step 0: Current Price Anchor (MANDATORY FIRST STEP)

**Before ANY analysis, fetch the current stock price via WebSearch.**

Tag every cited analyst estimate with date and stock price at that time. Discard if stock moved >30% since publication.

### Step 1: Segmented EPS (from Q3 Profit Conversion Analysis)

🔴 **CRITICAL: Use segmented (分部) estimation when product lines have different demand natures.**

If a company has multiple product lines with different cycle characteristics (e.g., structural NOR Flash + cyclical DDR4 + stable Logic IC), estimate EPS **per segment**, not as a single total. This prevents high-PE segments from inflating the valuation of cyclical segments.

| Segment | Revenue % | 2026E EPS Contribution | Demand Nature |
|---------|-----------|----------------------|---------------|
| [Segment A] | XX% | X.X | structural / cyclical / stable |
| [Segment B] | XX% | X.X | structural / cyclical / stable |
| **Total** | 100% | **X.X** | |

For **single-product companies**, a single EPS estimate is fine. The segmented approach is MANDATORY when:
- Two or more segments have fundamentally different demand natures (structural vs cyclical)
- One segment's PE should be >2x different from another's
- One segment is the profit driver but another provides the valuation floor

### Step 2: Event-Adjusted EPS

Each event from §6 (supply chain + event matrix) MUST be quantified as EPS impact × probability.

🔴 **EVENT DE-DUPLICATION RULE**: Multiple events that share the same root cause must be counted ONCE, not separately. Use the root cause as the event, and list the others as **supporting evidence**.

Example of WRONG approach:
- Samsung exits DDR4: +1.0 EPS
- SK Hynix exits DDR4: +1.0 EPS
- HBM crowds out DDR4: +1.0 EPS
- Micron acquires PSMC: +0.5 EPS
- → Total: +3.5 EPS ← INFLATED (all are the same story: DDR4 supply shrinking)

Example of CORRECT approach:
- **DDR4 structural shortage** (evidence: Samsung exit + SK exit + CXMT exit + HBM crowding + Micron/PSMC): +3.0 EPS, 85% probability → weighted +2.55
- → Confidence level: HIGH (5 independent evidence sources confirm same conclusion)

```
Event-adjusted EPS = Base EPS + Σ(de-duplicated events × probability)
```

### Step 3: Segmented Valuation (PE per segment)

🔴 **Each segment gets its OWN PE based on its demand nature and the company's pricing power in that segment.**

**PE Regime Table (per segment):**

| Demand Nature | PE Range | When to use |
|--------------|----------|-------------|
| **Structural monopoly** (AI/automotive/irreplaceable) | 18-25x | Segment has 3+ years of structural demand growth + oligopoly position |
| **Structural growth** (expanding TAM, not yet monopoly) | 14-20x | Growing market, company has moat but faces competition |
| **Cyclical boom** (shortage-driven, will normalize) | 8-12x | Current super-cycle, but demand/pricing will revert to mean |
| **Stable/mature** | 12-16x | Predictable, low-growth, steady margin |
| **Pure commodity cycle** | 6-10x | No moat, fully exposed to spot pricing |

**Pricing power (Q2) adjusts the position within each segment's PE range:**

| Pricing Power | Percentile within range |
|--------------|----------------------|
| 7G | 90th |
| 6G1Y | 75th |
| 5G2Y | 50th |
| 4G3Y | 25th |
| ≤3G or 🔴 | 10th |

**Segment valuation:**
```
Segment_value = Segment_EPS × Segment_PE
Total_fair_value = Σ(Segment_values) × Risk_discount
```

For **single-segment companies**, this simplifies to the original formula:
```
Fair Value = Total EPS × Single PE × Risk_discount
```

### Step 4: Risk Discount → Applies to TOTAL, not per-segment

| Risk Factor | Condition | Multiplier |
|------------|-----------|------------|
| **Geopolitical** | China revenue >40% | ×0.85 |
| | China revenue 20-40% | ×0.92 |
| | China revenue <20% | ×1.00 |
| **Valuation extreme** | PB > historical all-time high | ×0.88 |
| | PB in historical range | ×1.00 |
| **Governance** | Succession risk / no successor named | ×0.95 |
| **Data uncertainty** | Analyst EPS spread >2x | ×0.93 |
| **Cycle position** | Late cycle (>70% of typical duration) | ×0.88 |
| | Mid-late cycle (50-70%) | ×0.92 |
| | Early-mid cycle | ×1.00 |

```
Risk_discount = Π(applicable multipliers)
Final = Σ(Segment_values) × Risk_discount
```

### Step 5: Scenario Table

| Scenario | Segment A | Segment B | Segment C | Subtotal | Risk Discount | **Final** |
|----------|-----------|-----------|-----------|----------|---------------|-----------|
| **Bull** | EPS×PE | EPS×PE | EPS×PE | XXX | ×0.90 | **XXX** |
| **Base** | EPS×PE | EPS×PE | EPS×PE | XXX | ×0.88 | **XXX** |
| **Bear** | EPS×PE | EPS×PE | EPS×PE | XXX | ×0.85 | **XXX** |

**Weighted fair value = Bull×25% + Base×50% + Bear×25%**

### Step 6: Cross-Validation (MANDATORY)

After computing the segmented funnel, cross-check with:
- **PB法**: Current PB vs historical PB range
- **隱含預期反推**: Current price ÷ weighted-average PE = implied EPS → is this achievable?
- **法人目標價**: Does the funnel align with analyst consensus? If >20% different, explain why.

### Step 7: Position Assessment

```
Current price vs. Weighted Fair Value:
  >20% below → Undervalued, attractive entry
  ±10%       → Fairly valued
  10-30% above → Priced for optimism, wait
  >30% above → Overvalued / speculative
```

### Common Pitfalls to Avoid

1. **Double-counting same-source events** — Samsung exit + SK exit + HBM crowding are ONE story, not three
2. **Applying high-PE segment's multiple to cyclical segment's EPS** — NOR Flash (20x) should NOT multiply DDR4's earnings
3. **Ignoring cycle position** — A stock at 10x forward PE looks cheap, but if EPS is at cyclical peak and about to halve, it's actually 20x normalized PE
4. **Confusing revenue weight with profit weight** — A segment may be 35% of revenue but 60% of profit; use EPS contribution, not revenue share

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

-> Resulting EPS trajectory: [year-by-year]
-> Resulting valuation range: [price]
-> Trigger that confirms this path: [specific observable event]
-> Trigger that invalidates this path: [specific observable event]
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
| Price > Bull x 1.5 | MANDATORY deviation investigation |
| Price > Bull x 1.0 | Recommended deviation check |
| Price within Bear-Bull range | No investigation needed |
| Price < Bear x 0.7 | Recommended deviation check (may be broken) |

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
| **Narrative bubble** | Price is driven by retail momentum, social media hype, or misidentification (e.g., confused with another company) | Flag as extreme risk; note that structural analysis cannot support current price |
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

## Report Output Standards

### Required sections (v5 streamlined — 11 sections, no redundancy):

1. **現價錨定** — Stock price via WebSearch FIRST. Basic metrics (市值/股本/PB/TTM PE). Analyst targets with dates.

2. **一句話判斷** — Direct answer to "is there investment value at current price?"

3. **角色評估（Q1）→ PE聯賽** — 5-signal test. Score determines valuation regime:
   - 5/5+結構 → Growth Monopoly (25-35x)
   - 5/5+週期 → Transformed Cyclical (14-22x)
   - 3-4/5 → Blended (10-18x)
   - 0-2/5 → Pure Cyclical (6-12x)

4. **定價權（Q2）→ PE定位 + 風險EPS敏感度** — 7-factor 🟢/🟡/🔴 determines percentile within PE regime. PLUS:
   - 🔴 **EPS敏感度表（MANDATORY）**：`| 風險因子 | EPS影響 | 可控性 | 觸發條件 |`

5. **財務數據 + 利潤轉換（Q3）→ Base EPS** — Revenue, margins, EPS. Output: Bull/Base/Bear EPS.

6. **🔴 供應鏈與事件情報 → 事件調整EPS** — Graph traversal + event matrix. Each event quantified as `EPS impact × probability`. Output: Event-adjusted EPS.

7. **🔴 統一估值漏斗（分部制）** — THE core section. For multi-segment companies:
   ```
   公允價值 = Σ(各產品線EPS × 各自PE) × 風險折價
   ```
   For single-segment companies: `公允價值 = EPS × PE × 風險折價`
   Must show: segmented EPS table, per-segment PE with justification, risk discount chain, scenario table (Bull/Base/Bear), cross-validation (PB法+隱含預期+法人目標價).
   - 🔴 **事件去重**：同源事件只算一次，其餘列為證據強度
   - 🔴 **假設前提清單（黃旗）**：3-5 preconditions for Base Case.

8. **未來發展途徑** — 3 scenarios with triggers. Must tie to funnel scenarios.

9. **多輪洞察（僅新發現）** — ONLY insights NOT already stated in §3-§7. Skip if nothing new.

10. **雙軌建議 + 退場條件** — TWO separate recommendations:

    **A. 新入場建議（New Entry）**:
    | 項目 | 內容 |
    | 建議 | [進場/等回調/不建議] |
    | 進場區間 | [XX-YY元] |
    | 安全邊際 | [現價 vs Base %] |
    | 風險報酬比 | [上檔+X% / 下檔-Y%] |
    | 等待條件 | [若不建議，等什麼] |

    **B. 已持有建議（Current Holders）**:
    | 項目 | 內容 |
    | 建議 | [續抱/減碼/停利/出場] |
    | 停損價 | [XX元（理由）] |
    | 加碼/減碼觸發 | [條件] |
    | 退場條件 | [論點失效信號] |
    | 關鍵監控 | [1-2個最重要指標] |

    **The two can be DIFFERENT.** Holders have cost basis advantage.

11. **來源列表** — Simple list with (一次/二次) tags. No separate audit table needed.

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
