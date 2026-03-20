# Technology Intelligence Playbook

## Technical Footprint Analysis

| Investigation Layer | Technique | What It Reveals |
|---|---|---|
| 1. Tech stack fingerprinting | BuiltWith, Wappalyzer, or manual HTTP header analysis on their website/app | Actual technologies used (vs. what they claim), infrastructure spending level, third-party dependencies |
| 2. Open source intelligence | Search GitHub/GitLab for: (a) the company's public repos, (b) employees' personal repos, (c) repos mentioning the company | Internal tools leaked to public repos, development priorities, code quality, security practices, unreleased features |
| 3. API discovery | Check robots.txt, sitemap.xml, search for API documentation, try common API paths (/api/v1/, /graphql), review mobile app traffic | Undocumented endpoints, data structures, internal service names, deprecation patterns |
| 4. Infrastructure mapping | DNS records (all subdomains via crt.sh certificate transparency), IP ranges (ARIN/RIPE/APNIC), cloud provider identification | Development/staging environments, internal tools (jira.company.com, jenkins.company.com), geographic distribution, cloud spending |
| 5. Dependency analysis | Check package manifests if public (package.json, requirements.txt), or analyze known dependencies via tech stack | Supply chain risk, technology bets, potential vulnerabilities |
| 6. Mobile app analysis | App store metadata, permission requests, SDK integrations (via AppBrain, Exodus Privacy) | Data collection practices, third-party analytics/tracking, feature roadmap (from update notes history) |

## Developer and Engineering Intelligence

- **GitHub organization analysis**: Public repos, stars, contribution frequency, active vs archived repos. A repo with 50 contributors and daily commits = active product. A repo with 2 commits in 6 months = abandoned.
- **Stack Overflow / developer forums**: What questions are employees asking? Tag analysis reveals technology struggles and decisions in real-time.
- **Technical blog posts and conference talks**: Engineers revealing architecture decisions, scaling challenges, and technology choices.
- **npm / PyPI / crate registrations**: Companies publishing their own packages reveal internal tooling and API design philosophies.

## Technology Competitive Intelligence

- **Patent landscape mapping**: Search patent offices by technology keywords (not just company names). Who holds the foundational patents? Who's filing aggressively in a new area? Patent clusters reveal technology strategy 1-3 years ahead.
- **Academic-industry pipeline**: Which universities are collaborating with which companies? Co-authored papers = technology transfer pipeline. Search Google Scholar for `"company name" AND university`.
- **Standards body warfare**: Who's pushing standards that favor their technology? IEEE, W3C, 3GPP, IETF working groups — participation reveals long-term strategic positioning.
- **Acquisition target identification**: Small companies being cited in large companies' patents, or whose technology fills a gap in a platform — these are acquisition targets. Map patent citation networks and partnership announcements.

## AI / Emerging Tech Specific

- **Model and dataset tracking**: For AI companies — what models are they training? What datasets are they using or creating? Check Hugging Face, Papers with Code, academic preprints.
- **Compute infrastructure signals**: Large GPU cluster orders, cloud spending patterns (job postings for "infrastructure engineer, GPU clusters"), data center construction permits — these reveal scale of AI ambitions.
- **Regulatory positioning**: Who is lobbying for/against AI regulation? Submissions to regulatory consultations reveal both capability and strategic intent.
