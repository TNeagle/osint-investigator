# Enterprise / Organization Deep Investigation Playbook

Beyond basic company registry lookups, use these techniques to uncover hidden corporate structures and connections.

**Source priority:** Always start with company registries (經濟部商業司, OpenCorporates, SEC EDGAR) and technical infrastructure analysis (WHOIS, crt.sh, DNS records). Only after exhausting these primary sources should you turn to news articles or industry reports for leads. News about a company is commentary — registry data, infrastructure data, and court records are evidence.

## Shared Infrastructure Detection

| Technique | How to Do It | What It Reveals |
|---|---|---|
| Google Analytics ID tracking | Search for a company's GA tracking ID (UA-XXXXXXX or G-XXXXXXX) across the web | Other websites owned by the same entity, even if registered under different names |
| Shared hosting / IP analysis | Look up the website's IP address and find other domains on the same server | Related websites, especially for small operations running multiple sites |
| SSL certificate analysis | Check certificate details (crt.sh) for domain and organization information | Parent companies, alternative domain names, organizational structure |
| WHOIS history | Check historical WHOIS records for domain ownership changes | Previous owners, registration patterns, privacy service usage |
| Email domain analysis | Check MX records, SPF records for email infrastructure | Shared email infrastructure between supposedly separate companies |

## Shell Company and Hidden Ownership Detection

- **Shared registered address**: Search the company's registered address to find all other companies at the same address. 10+ companies at a residential address or a small office is a strong shell company indicator.
- **Nominee director patterns**: The same person serving as director of 50+ companies is likely a nominee/proxy, not a real operator. Search the director's name across company registries.
- **Circular ownership**: Company A owns Company B which owns Company C which owns Company A. Map ownership chains to detect loops.
- **Same-day registration clusters**: Multiple companies registered on the same day, at the same address, by the same agent — classic bulk shell company creation.
- **Beneficial ownership gaps**: If the registered owner is a holding company in an opaque jurisdiction (BVI, Cayman, Panama), check ICIJ leaked databases (Offshore Leaks, Panama Papers, Pandora Papers) for the real beneficial owner.

## Employee and Insider Intelligence

- Glassdoor / Indeed reviews — former employees often reveal internal culture, management problems, real business practices, and upcoming changes.
- LinkedIn employee analysis — how many employees? What roles are they hiring for? Rapid hiring in a specific area reveals strategic direction. Mass departures reveal problems.
- Job postings analysis — job requirements often reveal the tech stack, tools, methodologies, and upcoming projects a company is working on. A government contractor suddenly hiring Mandarin speakers tells you something.
