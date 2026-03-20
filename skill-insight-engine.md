# Multi-Round Insight Engine — 多輪洞察分析引擎

> **Load this file during Phase 5.5 of the investigation workflow.**
> See SKILL.md for when to invoke.

## Overview

After collecting all evidence and running the NetworkX graph, run a **multi-round insight analysis pipeline**. This is NOT a single-shot agent — it is an iterative process where each round builds on the previous round's discoveries.

**Why multi-round?** Single-round analysis finds only first-order insights (A→B). Real intelligence requires second-order (A→B→C) and third-order reasoning (A→B→C implies D). Each round peels back a layer:
- **Round 1 (Discovery)**: What patterns exist in the data?
- **Round 2 (Contradiction)**: Which patterns contradict each other? What resolves the contradiction?
- **Round 3 (Synthesis)**: What do the resolved contradictions reveal that no single data point could?

**In Strategic Assessment Mode**, the rounds additionally map to analysis levels — each round should operate at a DIFFERENT level of abstraction, not just dig deeper at the same level:
- **Round 1**: Event-level patterns (what happened, fact patterns, timeline anomalies)
- **Round 2**: Game-theory-level reasoning (what each player is calculating about every other player, resolving apparent contradictions through strategic logic)
- **Round 3**: Structural-level synthesis (what rules/systems/paradigms are changing, positive feedback loops, irreversible shifts)

The key insight: three rounds all operating at the same level (e.g., all finding event-level patterns) are less valuable than three rounds each operating at a successively higher level. The purpose of escalating levels is to prevent the analysis from "spinning" at the surface.

**When to invoke:** After Phase 5 synthesis is complete but before writing the final report.

**🔴 [#10] Set the search budget N and round count R before starting:**

| Investigation type | N (total search budget) | R (rounds) |
|---|---|---|
| Simple single-subject | 2 | 2 |
| Standard investigation | **3** | **2** (default) |
| Complex multi-stock or multi-domain | **5-8** | **3** |

---

## Round 1: Pattern Discovery Agent

Spawn a sub-agent with this prompt (use the Agent tool):

```
---
You are an OSINT Insight Analyst — Round 1 (Pattern Discovery). You have NOT conducted the investigation — you are seeing the results cold.

Your job: find patterns, anomalies, and hidden connections that the investigator missed. For EVERY insight, you MUST provide a **reasoning chain** showing exactly which data points led to which inference.

You have access to WebSearch. You are permitted to run **at most [N_round1] targeted searches** (coordinator specifies N). Use searches ONLY to verify critical gaps.

You will receive the graph summary, key findings, and working hypothesis.

## Reasoning Chain Format (MANDATORY for every insight)

Every insight must follow this structure:

### [Insight Title]

**Observation**: [What specific data points you noticed — cite node IDs, edge labels, dates]
**Pattern**: [What pattern or anomaly connects these observations]
**Inference**: [What this pattern implies — your analytical leap]
**Confidence**: [high/medium/low] — based on: [number of supporting data points, quality of sources, presence of counter-evidence]
**What would change this**: [Specific data that would invalidate this inference]
**Search verification** (if used): "Searched: [query]. Found: [result]. Impact: [how this changes the inference]"

## Your Tasks

A. **SIGNAL CONTRADICTION SCAN**: List ALL pairs of signals that appear to contradict each other. For each pair, state which is more likely correct and why. Format:
   - Signal A: [description] (source: [node/edge], date: [date])
   - Signal B: [description] (source: [node/edge], date: [date])
   - Resolution: [which signal dominates and WHY]
   - Reasoning chain: [A because X, B because Y, X outweighs Y because Z]

B. **STRUCTURAL ANOMALY DETECTION**: Using the graph topology (centrality, communities, isolated nodes), identify nodes that are:
   - High centrality + low investigation depth (intelligence blind spots)
   - Connected to both positive and negative force nodes (volatility amplifiers)
   - Isolated but should be connected (missing edges suggest missing information)

C. **TEMPORAL SEQUENCE ANALYSIS**: Examine the event timeline for:
   - Cause-effect chains (event A caused event B — cite the dates and explain the mechanism)
   - Suspicious timing coincidences (events that are too close to be independent)
   - Information gaps in the timeline (periods with no events — what was happening?)

D. **MISSING ENTITIES**: What entities should be in this graph but aren't? For each:
   - Why you expect them (cite the domain knowledge that makes their absence surprising)
   - What their absence might mean (deliberate concealment? simply overlooked? not relevant?)

E. **HYPOTHESIS STRESS TEST**: State the investigator's working hypothesis, then construct the strongest possible counter-argument. Use at most [N] searches to find evidence for the counter-argument.

Write in 繁體中文. Be specific — name entities, cite edges, include dates. Generic insights are worthless.

--- [GRAPH SUMMARY] ---
{paste graph metrics, centrality rankings, community detection, edge type distribution}

--- [KEY FINDINGS WITH DATE TAGS] ---
{paste findings list with inline confidence tags}

--- [WORKING HYPOTHESIS] ---
{paste coordinator's current hypothesis}

--- [EVENT TIMELINE] ---
{paste chronological event list from graph}

--- [TODAY'S DATE] ---
{current date}
---
```

---

## Round 2: Contradiction Resolution Agent

After Round 1 completes, spawn a SECOND agent that receives Round 1's output PLUS the original data. This agent's job is to resolve the contradictions Round 1 identified and generate second-order insights.

```
---
You are an OSINT Insight Analyst — Round 2 (Contradiction Resolution). You are seeing:
1. The original investigation data (graph, findings, hypothesis)
2. Round 1's pattern discoveries and contradictions

Your job: resolve the contradictions Round 1 identified. For each contradiction, determine WHY two apparently conflicting signals coexist — this "why" is usually the deepest insight in the investigation.

You have access to WebSearch. You are permitted to run **at most [N_round2] targeted searches**.

## Your Tasks

A. **CONTRADICTION RESOLUTION**: For each contradiction identified in Round 1:
   - Construct a **unified explanation** that accounts for BOTH signals simultaneously
   - Reasoning chain: [Signal A exists because X. Signal B exists because Y. Both can be true if Z. Z implies W.]
   - If no unified explanation exists, determine which signal is more likely a **false signal** and why
   - Confidence in resolution: [high/medium/low]

B. **SECOND-ORDER INSIGHTS**: Using the resolved contradictions, derive implications that were invisible from the raw data:
   - "If [resolved contradiction] is correct, then [non-obvious consequence] follows because [reasoning chain]"
   - Each second-order insight must trace back to at least 2 first-order observations

C. **CAPEX / FINANCIAL RATIO CROSS-CHECK** (for investment investigations):
   - Compare financial commitments (Capex, debt) against earnings trajectories
   - Identify companies whose investment thesis requires assumptions that contradict the resolved signals
   - Reasoning chain: [Company X's thesis requires A. But resolved contradiction shows B. A and B are incompatible because C.]

D. **RISK HIERARCHY**: Rank all identified risks by:
   1. Probability (based on evidence strength)
   2. Impact (based on graph centrality of affected nodes)
   3. Detectability (will we see warning signs before it happens?)
   - Output a 3-column risk matrix with reasoning chains

E. **CANARY INDICATORS**: Identify the smallest, earliest-detectable signals that would confirm or deny your second-order insights. These are the "things to watch" — not obvious metrics, but subtle leading indicators.
   - For each: what to watch, where to find it, what it would mean, and WHY it's a leading indicator (reasoning chain)

Write in 繁體中文. Trace every claim back to specific data points.

--- [ORIGINAL GRAPH SUMMARY] ---
{same as Round 1}

--- [ROUND 1 OUTPUT] ---
{paste Round 1 agent's full output}

--- [WORKING HYPOTHESIS (possibly updated after Round 1)] ---
{updated hypothesis if Round 1 caused changes}
---
```

---

## Round 3: Strategic Synthesis Agent (complex investigations only, R=3)

For complex multi-domain investigations, spawn a THIRD agent that reads Round 1 + Round 2 and produces the final strategic synthesis.

```
---
You are an OSINT Insight Analyst — Round 3 (Strategic Synthesis). You are seeing all prior analysis rounds.

Your job: produce the final, actionable strategic assessment. Every recommendation must include a complete reasoning chain from raw data to strategic conclusion.

## Your Tasks

A. **MASTER REASONING CHAINS**: For the top 3-5 insights from the entire investigation, write a complete reasoning chain from raw observation to strategic recommendation:
   - Data point(s) observed → Pattern identified (Round 1) → Contradiction resolved (Round 2) → Strategic implication → Actionable recommendation
   - Each chain must be numbered and self-contained (readable without other context)

B. **SCENARIO MATRIX**: Construct 3 scenarios (bull/base/bear) based on which unresolved uncertainties break which way:
   - For each scenario: probability, key trigger, timeline, portfolio implications
   - Reasoning chain for each probability estimate

C. **INFORMATION VALUE ANALYSIS**: Of all remaining intelligence gaps, which ONE piece of information would most change the analysis? Why? How could it be obtained?

D. **META-ANALYSIS**: Rate the overall investigation quality:
   - Source diversity score (primary vs. secondary, geographic spread)
   - Temporal coverage gaps
   - Which conclusions are robust (survive multiple counter-arguments) vs. fragile (depend on single data points)

Write in 繁體中文. This is the capstone analysis — make it count.

--- [ROUND 1 OUTPUT] ---
{paste}

--- [ROUND 2 OUTPUT] ---
{paste}

--- [GRAPH SUMMARY] ---
{paste}
---
```

---

## Coordinator's Post-Insight Responsibilities

After ALL insight rounds complete:

1. **Merge insights into the report**: Create a `## 🔴 多輪洞察分析（Multi-Round Insight Analysis）` section organized by round, preserving all reasoning chains
2. **Update confidence tags**: If any insight round found new evidence or resolved contradictions, update affected data points' confidence levels
3. **Re-open investigation if needed**: If Round 2/3 identifies a critical missing entity or a fatal flaw in the working hypothesis, re-enter Phase 2/3 before finalizing
4. **Reasoning chain audit**: Every insight in the final report must have a visible reasoning chain. If an insight lacks a chain, either add one or remove the insight — unsupported claims are worse than no claims
5. **Tag insight provenance**: Mark each insight with its round of origin: `[R1]`, `[R2]`, or `[R3]` so readers know the depth of reasoning behind each conclusion

---

## 🔴 [#15] Level-Up Check (Phase 5.75 — 分析層級升級檢查)

After completing all insight rounds, perform this mandatory check before writing the final report. The purpose is to ensure the analysis has reached the appropriate depth — not just described events, but explained their structural meaning.

**The four analysis levels:**

| Level | Core Question | Example Output |
|-------|--------------|----------------|
| **Event level** | What happened? Who did what? | Timeline, damage assessment, price movements, capacity changes |
| **Game Theory level** | What is each player calculating? How do their strategies interact? | n×n interaction matrix, stated vs. real objectives, second-order effects between players |
| **Structural level** | What "rules" are changing? What systems are being reconfigured? | Paradigm shifts, positive feedback loops, irreversible vs. recoverable changes |
| **Positioning level** | In the new structure, where does the analysis subject sit? | Strategic position assessment, vulnerability map, action options |

**Level-Up Check procedure:**

```
=== PHASE 5.75: LEVEL-UP CHECK ===
1. What level is my current analysis at?
   → [Event / Game Theory / Structural / Positioning]
2. What does my analysis imply at the NEXT level up?
   → [Describe what the current findings mean at one level higher]
3. Have I reached the target level declared in Phase 1?
   → [yes → proceed to report / no → identify what's missing]
4. If in Strategic Assessment Mode and I haven't reached Structural level:
   → The analysis is NOT done. Ask: "How does this change the RULES, not just the SCORE?"
   → If the analysis only describes what happened and who's affected, it hasn't
     answered the strategic question yet.
5. Does the analysis explain WHY things are happening (structural forces),
   or only WHAT is happening (event descriptions)?
   → An assessment that only catalogs events and impacts is a briefing, not an assessment.
     An assessment must identify the structural forces driving the events.
======================================
```

If the Level-Up Check reveals the analysis is stuck at a lower level than intended, do NOT simply add a paragraph of speculation at the end. Instead, re-enter Phase 5.5 with a specific prompt: "Given the event-level and game-theory-level findings, what structural changes are these events revealing? What systems or paradigms are being reconfigured?"
