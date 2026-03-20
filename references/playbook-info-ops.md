# Information Operations & Influence Campaign Investigation

**Source priority for info-ops is different from other domains.** Here, social media posts, accounts, and platform data ARE the primary sources. The risk is the opposite: searching for "news articles about influence campaigns" instead of analyzing the actual accounts and content yourself. Your job is to examine the social media accounts, posting patterns, and network topology directly — not to find what journalists or researchers have already published about them. News reports about info-ops are useful for identifying known campaigns and their patterns, but your investigation should be based on your own direct analysis of the platform data.

## Coordinated Inauthentic Behavior (CIB) Detection

| Detection Layer | What to Analyze | Red Flag Signals |
|---|---|---|
| 1. Account creation patterns | Registration dates, naming conventions, profile completeness | Clusters of accounts created within days of each other; sequential usernames (user_3847, user_3848); minimal profile details |
| 2. Posting behavior | Timing patterns, content similarity, amplification networks | Posts within seconds of each other across accounts; identical or near-identical text; accounts that only retweet/share specific sources |
| 3. Network topology | Follow/follower relationships, interaction patterns | Accounts that primarily follow each other (closed network); sudden coordinated follows of a target; dormant accounts reactivated simultaneously |
| 4. Content analysis | Narrative framing, language markers, media origins | Translations with characteristic errors; talking points matching known state media; memes/graphics traced to specific creation sources |
| 5. Infrastructure | Domains, hosting, social media page administration | Multiple pages managed from same location; domains registered by same entity; shared advertising accounts |

## Disinformation Source Tracing

**Trace the origin of a false narrative:**
1. Find the earliest instance — use advanced search with date ranges, sort by oldest
2. Identify the seed account(s) — who posted first? What's their history?
3. Map the amplification network — who shared it? In what order? Was there coordinated amplification?
4. Check for cross-platform seeding — did it appear on Telegram/WeChat first, then migrate to Facebook/Twitter?
5. Analyze the narrative frame — does it match known influence operation templates?

**Language and translation forensics:**
- Machine-translated content has characteristic patterns: unusual word order, literal idiom translations, inconsistent formality levels
- Compare suspicious content against known state media outputs for framing similarities
- Check if the "local" content uses terminology or date formats from another region

## AI-Generated Content Detection

- **Deepfake video**: Look for facial boundary artifacts, inconsistent lighting, unnatural blinking patterns, audio-visual sync issues. Reverse image search for the original face source.
- **AI-generated text**: Check for characteristic LLM patterns — overly balanced hedging, lack of specific local knowledge, generic phrasing. Cross-reference claimed facts for hallucinations.
- **AI-generated images**: Look for hand/finger anomalies, text rendering errors, inconsistent shadows, repeating patterns in backgrounds. Reverse image search yields zero prior results.
- **Synthetic audio**: Unnatural prosody, breathing patterns, room tone inconsistencies. Compare with known authentic recordings of the same person.

## Taiwan-Specific Information Operations

- **Chinese cognitive warfare patterns**: Content laundering through Hong Kong/overseas Chinese media → picked up by local Taiwanese outlets; LINE group seeding; PTT manipulation; YouTube content farm networks
- **Content farm identification**: Check for sites with massive content volume, no clear editorial staff, recycled content from Chinese sources, ad-heavy layouts
- **Platform-specific analysis**: PTT account age and posting patterns; Facebook group admin analysis; LINE group forwarding chains; YouTube channel network mapping
- **Election interference indicators**: Surge in political content from new accounts before elections; coordinated attacks on specific candidates; fabricated poll results

## Influence Network Mapping with NetworkX

Map the influence operation as a directed graph:
- **Nodes**: Accounts, pages, domains, media outlets (with type: bot_suspect, amplifier, seed_account, legitimate_media)
- **Edges**: shares, retweets, quotes, cites (with timestamp for propagation analysis)
- **Tags**: `bot_suspect`, `state_affiliated`, `content_farm`, `coordinated_cluster`
- **Analysis**: Community detection reveals coordinated clusters; temporal analysis reveals synchronization; centrality reveals seed accounts
