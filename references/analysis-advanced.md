# Advanced Analysis Techniques

These cross-cutting analysis techniques apply to ALL investigation types. Load this reference when the investigation requires deeper analytical rigor.

## Temporal Intelligence Analysis

Most investigations produce a **static snapshot**. The most revealing intelligence hides in **changes over time**.

| Temporal Signal | How to Detect | What It Reveals |
|---|---|---|
| Company registration/dissolution timing | Compare company registry dates with public events (elections, scandals, investigations) | Companies created just before a politician takes office, or dissolved right before an investigation starts, signal intentional structuring |
| Domain ownership changes | WHOIS history tools show when domain ownership transferred | A website that changed hands right before promoting a new product/scheme suggests preparation |
| Social media content deletion | Wayback Machine + archive.today vs current profile | What someone chose to delete is often more revealing than what they chose to post |
| Financial disclosure changes | Compare year-over-year asset declarations (for politicians/officials) | Sudden wealth increases or asset disappearances correlate with corruption patterns |
| Corporate officer changes | Track director/shareholder changes over time in company registries | Mass resignation before a scandal = insider knowledge. New directors right after = restructuring to distance |
| Website content evolution | Archive.org Wayback Machine timeline | A crypto project's website promising 50% returns in 2023 that now says 20% = adjusting the scam as scrutiny increases |
| Job posting patterns | Track hiring/firing trends on LinkedIn, Indeed over months | Sudden mass layoffs or hiring freezes revealed through job posting disappearance |

**Timeline correlation technique:**
1. Build a chronological timeline of ALL events discovered across all sources
2. Look for suspicious clustering — multiple events within the same 2-week window often aren't coincidental
3. Look for suspicious sequences — action A consistently precedes action B = pattern
4. Look for suspicious gaps — periods with zero activity from a normally active entity

Always ask: "What did this look like 6 months ago? 1 year ago? 5 years ago?" The delta between past and present is intelligence.

## Counter-Intelligence Awareness

Recognize when a target is **actively hiding their traces**. Absence of expected information is itself intelligence.

**Obfuscation signals:**

| Pattern | What You Observe | What It Likely Means |
|---|---|---|
| Privacy service WHOIS | Every domain registered through privacy proxy | Deliberate effort to hide online assets |
| Nominee director chains | Professional nominees as directors with 50+ other companies | Real beneficial owner is hiding behind proxy structures |
| Jurisdiction shopping | Key entities registered in BVI, Cayman, Panama, Seychelles | Exploiting opacity laws to hide ownership |
| Social media absence | Person with significant public role has zero social media presence | Either extremely private or deliberately scrubbing their footprint |
| Identical corporate addresses | 10+ companies sharing a single mailbox or virtual office | Shell company farm — investigate the registered agent |
| Circular ownership loops | A owns B owns C owns A | Designed to obscure who actually controls what |
| Over-complete digital persona | Perfect LinkedIn, polished website, stock photo headshots, but no organic social presence | Potentially fabricated identity — common in scams and fraud |
| Content scrubbing | Wayback Machine shows pages that now return 404 | Active removal of compromising information |

**The "dog that didn't bark"**: A politician with no financial disclosures. A company with no employee reviews. A 15-year career gap. These absences deserve investigation and explicit mention in your report.

**Counter-obfuscation techniques:**
- Check historical WHOIS before privacy was added
- Use Wayback Machine and Google Cache for scrubbed content
- Check ICIJ leaked databases for opaque structures
- Use date-restricted searches (`before:2015`) to find older traces

## Behavioral Pattern Analysis

Read behavioral signals from public data — no interaction with the target required. Purely passive analysis of open sources.

**Organizational signals**: Email CC patterns in leaked/public correspondence reveal actual power structure. Crisis response speed and spokesperson choices reveal who holds real authority. Job posting language reveals culture and retention struggles.

**Individual signals**: Writing style differences across platforms reveal unguarded behavior. Posting timestamps reveal timezone and schedule. Public interaction speed in threads reveals relationship priorities. Gap between stated values and actual corporate lobbying/investment is intelligence.

**Behavioral timing**: Increased posting frequency, tone shifts, or sudden silence often correlate with significant events — cross-reference with your investigation timeline.

After building your entity network, select the 2-3 most important human nodes. Analyze their behavioral patterns. Look for inconsistencies. Add findings as annotations to NetworkX graph nodes.
