# OSINT Sources and Techniques Quick Reference

## Table of Contents
1. [Image Analysis Techniques](#image-analysis)
2. [People Investigation Sources](#people-investigation)
3. [Organization Investigation Sources](#organization-investigation)
4. [Geolocation Techniques](#geolocation)
5. [Digital Footprint Analysis](#digital-footprint)
6. [Regional Source Guide](#regional-sources)

---

## Image Analysis

### Metadata Extraction
- EXIF data (camera model, GPS coordinates, timestamp)
- File naming conventions (IMG_XXXX → iPhone, DSC_XXXX → Nikon, etc.)
- Image dimensions and compression artifacts

### Visual Clue Categories
| Category | What to Look For | Intelligence Value |
|----------|-----------------|-------------------|
| Text/Signs | Language, font style, regulatory format | Country/region identification |
| Vehicles | License plate format, brand distribution | Country, sometimes city |
| Road Markings | Line colors, patterns, lane width | Country identification |
| Vegetation | Tree species, crop types, season | Climate zone, hemisphere |
| Architecture | Building materials, roof style, window patterns | Cultural region |
| Infrastructure | Power pole design, traffic lights, bollards | Country-specific standards |
| Sun/Shadows | Shadow angle and direction | Time of day, latitude estimate |
| Sky/Weather | Cloud patterns, visibility, precipitation | Season, climate zone |

### Reverse Image Search Engines
- Google Images (lens.google.com)
- TinEye (tineye.com)
- Yandex Images (often best for Eastern Europe/Asia)
- Bing Visual Search

## People Investigation

### Public Records
- Corporate director registries
- Court case databases
- Property records
- Voter registration (where public)
- Professional licenses

### Professional Presence
- LinkedIn profiles and connections
- Academic publications (Google Scholar, ResearchGate)
- Patent filings (Google Patents, WIPO)
- Conference speaker lists
- Professional association memberships

### Digital Presence
- Social media profiles across platforms
- Personal websites/blogs
- Forum posts and comments
- Code repositories (GitHub, GitLab)
- Domain registrations (WHOIS history)

## Organization Investigation

### Corporate Intelligence
- Business registration databases (by country)
- Annual reports and financial filings
- SEC/equivalent filings
- Credit rating reports
- Trademark and patent portfolios

### Relationships and Networks
- Board member cross-references
- Shared addresses between entities
- Supply chain connections
- Partnership announcements
- Joint patent filings

### Digital Infrastructure
- Website technology stack (BuiltWith, Wappalyzer)
- DNS records and hosting history
- SSL certificate details
- Email domain configuration (MX records)

## Geolocation

### Country-Level Indicators
| Indicator | Example |
|-----------|---------|
| Driving side | Left: UK, Japan, Australia, Thailand; Right: most others |
| Road marking colors | US: white/yellow; Europe: white; Japan: white/orange |
| License plate format | EU blue strip, US state designs, JP kei-car yellow |
| Language on signs | Script type immediately narrows region |
| Electrical infrastructure | Pole design, voltage markings differ by country |

### Precision Techniques
1. Match mountain/hill silhouettes against topographic maps
2. Use sun angle + shadow length to estimate latitude
3. Cross-reference visible business names with mapping services
4. Match road intersection geometry against satellite imagery
5. Use visible transit route numbers to pinpoint location

## Digital Footprint

### Username Pivot
- Search same username across multiple platforms
- Check username history/changes
- Look for email addresses associated with usernames

### Email Investigation
- Domain verification
- Breach database mentions (ethical: only check existence, not contents)
- Associated accounts via password reset pages (observe, don't exploit)

### Website Analysis
- WHOIS historical records
- Web archive (Wayback Machine) for historical versions
- Linked pages and outbound references
- Analytics/tracking ID connections between sites

## Regional Sources

### Taiwan / 台灣

**公司與商業**
- 經濟部商業司 商工登記公示資料查詢 (MOEA company registry) — 公司負責人、董監事、資本額、登記地址
- 公開資訊觀測站 MOPS (TWSE disclosure) — 上市櫃公司財報、重大訊息、董監事持股
- 經濟部智慧財產局 (TIPO) — 專利、商標查詢

**政治與政府**
- 監察院廉政專刊 / 公職人員財產申報 — 立委、官員財產申報資料（搜尋「監察院 財產申報 [姓名]」）
- 監察院政治獻金查閱平台 — 政治獻金收支明細
- 立法院議事暨公報管理系統 (LIMS) — 立委提案、質詢、表決紀錄
- 立法院國會圖書館 — 立委個人資料、經歷、學歷
- 政府電子採購網 — 政府標案得標紀錄
- 行政院公報 — 人事任命、法規命令

**法律**
- 司法院裁判書查詢系統 (court decisions) — 民事、刑事、行政判決全文
- 司法院法學資料檢索系統 — 法規、判例、裁定

**財產與不動產**
- 內政部地政司 — 土地登記資料（需透過地政事務所查詢）
- 實價登錄查詢 — 不動產交易價格公開資訊

**社群媒體常用平台**
- Facebook（台灣最主流社群平台）
- Instagram
- LINE（通訊為主但有公開群組）
- PTT / Dcard（論壇）
- YouTube
- X/Twitter（較少但政治人物常用）

**其他**
- 財政部稅務入口網
- 關貿網路 — 進出口資料
- 台灣博碩士論文知識加值系統 — 學位論文查詢

### China / 中國
- 天眼查 / 企查查 / 啟信寶 (company lookup) — 公司股東、董事、投資關係、法律訴訟
- 中國裁判文書網 (court decisions)
- 國家企業信用信息公示系統 — 工商登記、行政處罰
- 中國知網 CNKI (academic)
- 中國執行信息公開網 — 失信被執行人（老賴）名單
- 全國組織機構統一社會信用代碼數據服務中心
- 微博、微信公眾號、抖音、小紅書 — 社群媒體

### Japan / 日本
- 国税庁法人番号公表サイト
- EDINET (financial disclosure)
- J-PlatPat (patents/trademarks)
- 裁判所 裁判例情報 (court decisions)
- 官報 (government gazette)

### United States
- SEC EDGAR (financial filings)
- PACER (federal courts)
- State Secretary of State business registries
- USPTO (patents/trademarks)
- OpenCorporates (aggregator)
- FEC (Federal Election Commission) — campaign finance
- OpenSecrets.org — political donations, lobbying data
- USAspending.gov — government contracts
- OFAC Sanctions List
- Federal Register — government actions

### Europe
- EU company registries (varies by country)
- EUR-Lex (EU law/cases)
- EPO Espacenet (European patents)
- OpenCorporates
- EU Transparency Register — lobbying

### Cross-Regional Tools
- ICIJ Offshore Leaks Database — Panama Papers, Pandora Papers, Paradise Papers
- OpenSanctions — global sanctions and PEP (Politically Exposed Persons) data
- OCCRP Aleph — organized crime and corruption project database
- Wayback Machine (web.archive.org) — historical website snapshots
- Social media username search tools: search "[username] site:facebook.com", "[username] site:instagram.com" etc.
