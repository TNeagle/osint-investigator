# Person Investigation Playbook

Choose the playbook that matches the subject and **work through every applicable category systematically**. Don't skip categories — even a negative result ("no court records found") is valuable intelligence.

## How to use this playbook (read this first)

The layers below are numbered 1-10. This numbering is your **search order** — execute them top to bottom. Notice that news/media searches are NOT in the first half of the table. This is intentional. The whole value of OSINT is that you dig into primary sources that journalists may not have checked.

**The anti-news rule:** Do not search for `"[name]" news` or `"[name]"` in a general web search as your first action. Instead, go directly to the specific databases listed in each layer. General web searches tend to surface news articles, which then anchor your thinking around what reporters already found. You want to find what they missed.

**When you DO encounter news articles** (which will happen naturally), treat every factual claim as a lead: "The article says Person X is a director of Company Y → go to 經濟部商業司 and verify." Cite the registry, not the article.

**Report quality check:** Before finalizing, count your citations. If more than a third come from news articles, you need to revisit the layers you skipped. A strong OSINT report should be at least 2/3 primary sources (registries, court records, financial disclosures, social media posts, patent databases).

## Political Figures (legislators, officials, candidates)

| Layer | What to Search | Source Type | Specific Database |
|---|---|---|---|
| 1. Financial disclosures | Asset declarations, income sources, property holdings, stock portfolios | **Registry** | 監察院財產申報, MOPS |
| 2. Corporate connections | Company directorships (past & current), business registrations in their name or family members' names | **Registry** | 經濟部商業司, OpenCorporates |
| 3. Voting & legislative record | Bills sponsored/co-sponsored, committee memberships, voting patterns | **Registry** | 立法院議事系統 LIMS, 立法院公報 |
| 4. Campaign finance | Donation records, political fundraising events, major donors, campaign spending | **Registry** | 政治獻金查閱平台 |
| 5. Court & legal records | Lawsuits (as plaintiff or defendant), criminal records, administrative penalties | **Court** | 司法院裁判書查詢系統 |
| 6. Property & real estate | Land registry records, property transactions, addresses used in registrations | **Registry** | 實價登錄, 地政司 |
| 7. Social media deep dive | All platforms, posting patterns, follower analysis, deleted posts (via web archive) | **Direct** | Facebook, Instagram, X, LINE, YouTube, TikTok |
| 8. Family & associate network | Spouse's business interests, children's careers, known associates | **Registry + Social** | 商業司 (search spouse name), social media |
| 9. Academic & professional background | Degree verification, thesis, professional licenses, prior career | **Registry** | 台灣博碩士論文系統, professional registries |
| 10. News & media (last resort fill-in) | Only for leads NOT covered by layers 1-9, or to find starting names/dates | **News** | General web search, news databases |

Example search patterns for a Taiwanese legislator named "王大明" — notice these go to specific databases, not general news:
- **Layer 1**: search 監察院 for `王大明 財產申報` → financial disclosure
- **Layer 2**: search 經濟部商業司 for `王大明` → find all companies where they're director/shareholder
- **Layer 3**: search 立法院議事系統 for `王大明` → bills, votes, committee records
- **Layer 4**: search 政治獻金查閱平台 for `王大明` → donation records
- **Layer 5**: search 司法院裁判書 for `王大明` → court records
- **Layer 6**: `"王大明" 實價登錄` or search 實價登錄 → property records
- **Layer 7**: `"王大明" site:facebook.com`, `site:instagram.com`, `site:linkedin.com`
- **Layer 8**: search 商業司 for spouse name; `"王大明" 配偶 OR 妻子 OR 丈夫 公司`
- **Layer 9**: search 台灣博碩士論文系統 for `王大明`; verify claimed degrees
- **Layer 10** (only if gaps remain): `"王大明"` general web search for leads to chase in layers 1-9

## Business Figures (executives, founders, investors)

Same rule: layers 1-5 are registry/court sources — search them BEFORE any general web search.

| Layer | What to Search | Source Type | Specific Database |
|---|---|---|---|
| 1. Corporate network | All companies as director/shareholder (current + historical), beneficial ownership chains | **Registry** | 商業司, OpenCorporates, SEC EDGAR |
| 2. Financial filings | SEC/equivalent filings, annual reports, credit reports, tax liens | **Registry** | MOPS, SEC EDGAR, annual reports |
| 3. Legal exposure | Lawsuits, regulatory actions, bankruptcy filings, sanctions lists | **Court/Registry** | 司法院裁判書, PACER, OpenSanctions |
| 4. Intellectual property | Patents, trademarks in their name or their companies | **Registry** | TIPO, USPTO, Google Patents |
| 5. Property & assets | Property records, vehicle registrations, yacht/aircraft registries | **Registry** | 實價登錄, land registries |
| 6. Professional history | LinkedIn deep dive, prior employers, board memberships, advisory roles | **Direct** | LinkedIn, conference records |
| 7. Social media & lifestyle | Personal accounts, philanthropic activities, club memberships | **Direct** | All social platforms |
| 8. Associate mapping | Co-directors across companies, co-investors, business partners | **Registry** | Cross-reference 商業司 results |
| 9. Offshore connections | BVI/Cayman/Panama company registries, ICIJ leaked databases | **Registry** | ICIJ Offshore Leaks, BVI/Cayman registries |
| 10. News & media (fill-in) | Interviews, conference talks, op-eds — only for leads NOT found above | **News** | General web search |

## General Person Investigation

| Layer | What to Search | Source Type |
|---|---|---|
| 1. Identity verification | Full name variants, aliases, date of birth, known addresses | **Direct** |
| 2. Digital footprint | Username search across platforms, email search, domain ownership (WHOIS) | **Registry/Direct** |
| 3. Professional presence | LinkedIn, ResearchGate, GitHub, professional associations | **Direct** |
| 4. Company registrations | Business registrations in their name, company directorships | **Registry** |
| 5. Legal records | Court cases, property records | **Court/Registry** |
| 6. Social media mapping | All platforms, posting history, connections, group memberships | **Direct** |
| 7. Academic record | Publications, degrees, conference appearances | **Registry** |
| 8. News & media (fill-in) | Only for leads NOT covered above | **News** |

## Social Media Deep-Dive — MANDATORY

**Do not skip this section.** Load and execute `playbook-social-media.md` in full for every person investigation. It contains 6 phases of fully automated searches using WebSearch `site:` operators — no login required.

Key principle: social media evidence is often the only way to verify or contradict relationship claims (e.g., "I don't know that person" vs. tagged photos together). It also catches things registries miss: lifestyle inconsistent with declared income, undisclosed associations, deleted content that reveals what someone wants hidden.
