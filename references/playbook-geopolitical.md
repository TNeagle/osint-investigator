# Geopolitical Event Analysis Playbook

This playbook is for analyzing dynamic geopolitical events — wars, crises, sanctions regimes, policy shifts, alliance realignments — where the core challenge is not finding hidden facts but correctly interpreting known facts across multiple interacting actors and systems.

**When to use**: Any investigation where (a) multiple state or institutional actors are involved, (b) the situation is evolving over time, (c) the user needs to understand *what it means* and *what happens next*, not just *what happened*.

**Key difference from other playbooks**: Most OSINT playbooks help you find things. This playbook helps you *think about* things you've already found. The failure mode it guards against is not "missing data" but "wrong framework" — accepting a narrative that makes the data fit a story that isn't the most accurate one.

---

## Step 1: Define the Game Board

The single most important step. An incomplete game board leads to blind-spot analysis — you'll build a sophisticated model that's missing a key player, and the missing player's actions will repeatedly surprise you.

### 1A. Four-Layer Stakeholder Identification

| Layer | Definition | How to Find Them |
|-------|-----------|-----------------|
| **Direct participants** | Actively involved in the event (belligerents, negotiators) | Obvious from news coverage |
| **Directly affected** | Not participating but suffering/benefiting from direct effects | Think about geography, supply chains, alliances |
| **Indirect beneficiaries/losers** | Affected by second-order effects (competitors, alternative suppliers) | Ask: "Who gains if this continues? Who gains if it stops?" |
| **Potential influencers** | Can change the outcome but haven't acted yet | International organizations, swing states, key corporations, financial institutions |

**Completeness check**: After listing all stakeholders, ask:
- "If I were writing a history book about this event in 10 years, who would appear in the chapter that I haven't listed?"
- "Who is conspicuously silent or absent from the news coverage? Their silence may itself be strategic."
- "Whose interests are being touched indirectly through supply chains, financial markets, or alliance obligations?"

### 1B. Player Profiles

For each stakeholder, document:

```
=== [PLAYER NAME] ===
Stated objective: [what they publicly say they want]
Likely real objective: [what their actions reveal — actions speak louder than statements]
Key resources: [military, economic, diplomatic, informational leverage]
Key constraints: [what they CAN'T do — domestic politics, economic limits, alliance obligations]
Red lines: [what would force them to escalate or change strategy]
Time horizon: [are they playing for next week, next year, or next decade?]
```

**The gap between stated and real objectives is where the best insights live.** A country that says it wants peace but keeps escalating is revealing something about its true calculations. A company that says it's "monitoring the situation" while quietly restructuring its supply chain is telling you more than its press releases.

### 1C. n×n Interaction Matrix

This is the analytical centerpiece. Create a matrix where EVERY stakeholder has a row AND a column. Each cell answers: "What is [Row] calculating about [Column]?"

This is NOT:
- n×1 analysis (everyone → target subject) ← this is the most common mistake
- 1×n analysis (one player → everyone else)

It IS:
- n×n analysis: every player's strategy depends on what they think every OTHER player will do

**Why this matters**: A player's behavior toward your analysis subject is often driven by their calculation about a THIRD party. For example: Country A's pressure on Country B may not be about B at all — it may be a signal to Country C. If you only look at A→B, you miss the real logic.

**How to fill in the matrix**:
1. Start with cells you're most confident about (direct adversaries, known alliances)
2. Leave unknown cells explicitly blank — these become your search priorities in the investigation phase
3. After searching, fill in cells and look for contradictions: does Player X's stated posture toward Player Y match what their actions reveal?

### 1D. System Framing

Before diving into facts, step back and ask:

1. **What is the largest system this event is part of?**
   - A regional war may be part of a global power transition
   - A supply chain disruption may signal the end of a globalization paradigm
   - A sanctions regime may be testing a new model of economic warfare

2. **What pre-existing structural trends does this event accelerate?**
   - Events rarely create entirely new dynamics — they usually accelerate or reveal dynamics that were already building

3. **What "rules of the game" might be changing?**
   - Not just who's winning or losing, but whether the game itself is being replaced by a different one
   - Examples: maritime freedom of navigation rules, unified vs. fragmented energy markets, just-in-time vs. just-in-case supply chain philosophy

---

## Step 2: Chronological Fact Collection (Bottom-Up)

**Principle: Collection goes from small to large. Facts first, interpretation later.**

### 2A. Day-by-Day Timeline

Search chronologically, not topically. For each day of the event:
- `"[event] [YYYY-MM-DD]"` or `"[event] March 3"`
- Record: date, what happened, who acted, what changed, primary source

### 2B. Fact vs. Analysis Separation

For every piece of information, classify it:

| Category | What it is | How to handle |
|----------|-----------|--------------|
| **Hard fact** | Verifiable event, official statement, measurable data | Record with primary source citation |
| **Reported claim** | News report of an event, not yet independently verified | Tag as (conf: low) until verified |
| **Analysis/opinion** | Someone's interpretation of what facts mean | DO NOT record as fact. Note the framing separately. |
| **Framework** | The narrative structure that organizes facts into a story | Most dangerous if absorbed unconsciously. Always build your own. |

**The critical distinction**: A news article saying "oil prices rose 15% to $127/barrel" is reporting a fact. The same article saying "this selective blockade reveals Iran's strategy to..." is offering a framework. The number can be cited. The framework must be independently derived.

### 2C. Primary Source Hierarchy for Geopolitical Events

| Source Type | Examples | Trust Level |
|-------------|----------|-------------|
| Official government statements & documents | UN resolutions, executive orders, official communiqués | High for stated positions; treat with skepticism for claimed facts |
| Tracking data | AIS (ship), ADS-B (aircraft), satellite imagery | High for physical movements |
| Financial market data | Commodity prices, insurance premiums, shipping rates | High for market reactions |
| Think tank / intelligence assessments | CSIS, IISS, RAND, Chatham House | Medium — analytical, not raw data |
| News wire services | Reuters, AP, AFP | Medium — fast but can be wrong; verify key claims |
| News analysis | Named columnists, editorial boards | Low — this is someone else's framework |
| Social media | Government officials' posts, OSINT community | Variable — verify everything |

---

## Step 3: Game Theory Analysis (Top-Down from Structure)

**Principle: Analysis goes from large to small. Structure first, events are explained BY the structure.**

### 3A. System Stress Analysis

For each global system relevant to the event:
- What was the system's pre-existing state? (stable, strained, already fragmenting?)
- How does this event stress the system?
- Is the stress reversible or irreversible?
- Are there positive feedback loops? (A worsens B which worsens A)

### 3B. Player Strategy Derivation

For each stakeholder:
1. Given the n×n matrix, what is their **optimal strategy** considering all other players?
2. Where does their stated strategy diverge from their optimal strategy? (The gap reveals either deception or domestic constraints)
3. **Who wants the situation to continue?** (These players will subtly obstruct resolution)
4. **Who wants it to end?** (These players will seek settlement terms)
5. **Who benefits from ambiguity?** (These players will resist clarity)

### 3C. Second and Third-Order Effects

Don't stop at "A causes B". Push to:
- A causes B, which causes C (second order)
- The pattern of A→B→C reveals D about the entire system (third order)

**Template for escalation**:
```
First order:  [Event] → [Direct impact on sector/country]
Second order: [Direct impact] → [How affected parties respond] → [Cascade effect]
Third order:  [The pattern of cascading effects] → [What this reveals about structural vulnerability]
```

---

## Step 4: Structural Impact Assessment

This is where assessment diverges most sharply from investigation. Investigation asks "what?" — assessment asks "so what?"

### 4A. Rule Changes vs. Score Changes

| Type | Description | Example |
|------|-------------|---------|
| **Score change** | One player gains/loses within existing rules | Oil price rises; some countries pay more |
| **Rule change** | The system governing the game is altered | Maritime insurance refuses to cover a key strait; entire trade route becomes uneconomic |

**Assessment must identify rule changes, not just score changes.** A score change reverses when the event ends. A rule change persists.

### 4B. Positive Feedback Loop Identification

The most dangerous structural outcomes involve positive feedback loops — where Effect A worsens Condition B which worsens Effect A:

```
Identify: Does the weakening of System X make System Y more vulnerable?
         Does the vulnerability of System Y feed back to further weaken System X?
         Are there THREE or more systems in a mutual weakening loop?
```

If yes, the situation is structurally unstable — even if the triggering event resolves, the damage to interconnected systems may persist.

### 4C. Reversibility Assessment

For each identified impact:
- **Reversible in days/weeks**: Market price movements, temporary supply disruptions
- **Reversible in months/years**: Contract renegotiations, supply chain rerouting, diplomatic relationships
- **Irreversible or very difficult to reverse**: Destroyed infrastructure, shattered trust/alliances, nuclear proliferation, permanent trade route abandonment

---

## Step 5: Positioning Analysis

Finally, return to the analysis subject (e.g., Taiwan, a specific industry, a company) and assess their position within the new structure identified in Step 4.

### 5A. Structural Position Map

- What pillars support the subject's current position? (e.g., maritime trade access, energy supply, alliance protection, technology dominance)
- Which pillars are being weakened by the identified structural changes?
- Are multiple pillars weakening simultaneously? (compound vulnerability)

### 5B. Scenario Projection

Build 2-4 scenarios based on which uncertainties resolve which way:

For each scenario:
- **Probability**: Based on game theory analysis, not gut feeling
- **Key trigger**: What specific event would confirm this path?
- **Timeline**: When would we know?
- **Impact on subject**: Specific, measurable consequences
- **Decision nodes**: Points where the trajectory could change

### 5C. Actionable Intelligence

The final output should answer:
- What should the analysis subject do NOW (immediate actions)?
- What should they prepare for (contingency planning)?
- What should they watch (early warning indicators)?
- What is irreversible and must be accepted vs. what can still be influenced?

---

## Anti-Patterns to Avoid

These are the most common failure modes in geopolitical assessment, identified through real analytical mistakes:

1. **Absorbing news narratives as analytical frameworks**: News articles package facts inside an interpretive story. You can use their facts; you must not use their story. Build your own framework from primary sources.

2. **Single-direction perspective-taking**: Analyzing "how does X affect Taiwan" is n×1 thinking. Real assessment requires n×n thinking: how X affects Y affects Z, and the compound effect on your subject.

3. **Incremental player discovery**: If you keep discovering new relevant players mid-analysis, your Phase 1 scoping was incomplete. Pause and do a complete re-scan rather than bolting new players onto an existing incomplete framework.

4. **Staying at event level when structural analysis is needed**: Describing what happened (even thoroughly and accurately) is a briefing, not an assessment. Assessment explains what the events MEAN for the larger system.

5. **Mixing collection with analysis in the same pass**: When you search for evidence while simultaneously building your interpretive framework, you unconsciously filter for evidence that supports the framework you're building. Keep these two cognitive modes strictly separate.

6. **Flat analysis across identical levels**: Running three "rounds" of analysis that all operate at the same level (finding more event-level patterns, then more event-level patterns, then more event-level patterns) is less valuable than three rounds that each escalate to a higher level of abstraction.

7. **Confusing smart with right**: A sophisticated, internally consistent analysis that starts from a wrong premise will produce elegant wrong conclusions. Always test your starting premises, not just your logic chain.

---

## Report Template for Strategic Assessment

```markdown
# 戰略研判報告（Strategic Assessment Report）

## 執行摘要
[3-5句話：核心研判結論——不是事件摘要，而是結構性含義]

## 棋盤定義（Game Board）
### 利害關係方清單
[四層掃描結果]
### n×n 互動矩陣
[表格格式，含已知互動和待驗證互動]

## 事實基礎（Chronological Facts）
### 時間線
[逐日事件，嚴格區分事實與分析]
### 關鍵數據點
[附 confidence tag 和 primary source]

## 博弈分析（Game Theory Analysis）
### 各方策略推導
[每個玩家：表面目標 vs 真實目的 vs 最佳策略]
### 二階/三階效應
[A→B→C 推理鏈]

## 結構性影響（Structural Impact）
### 規則變化（不只是分數變化）
[哪些系統性規則正在改變]
### 正反饋循環
[相互加強的脆弱性]
### 可逆性評估
[哪些影響是不可逆的]

## 定位分析（Positioning）
### 分析對象的結構性位置
[支柱、脆弱性、複合風險]
### 情境推演
[2-4 個路徑，含概率、觸發點、時間線]
### 可行動情報
[現在該做什麼、該準備什麼、該觀察什麼]

## 分析品質自評（Meta-Analysis）
### 來源審計
[一次/二次來源比例]
### 分析層級達成
[是否達到目標層級]
### 關鍵假設與脆弱性
[哪些結論最依賴尚未驗證的假設]
```
