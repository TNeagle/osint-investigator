# Economic & Financial Flow Investigation Playbook

## Follow the Money — Layer by Layer

| Investigation Layer | Technique | Key Sources |
|---|---|---|
| 1. Corporate financial structure | Map parent-subsidiary chains, identify special purpose vehicles (SPVs), analyze shareholding percentages | Company registries, annual reports, 公開資訊觀測站, SEC EDGAR, OpenCorporates |
| 2. Beneficial ownership tracing | Follow ownership chains through holding companies until reaching a natural person or opaque jurisdiction | ICIJ Offshore Leaks, company registries, GLEIF (LEI database), national BO registers |
| 3. Financial transaction patterns | Track public financial data: stock transactions (insider trades), real estate transactions, government procurement payments | 實價登錄, SEC insider trading, government procurement portals, land registries |
| 4. Sanctions & regulatory exposure | Check all entities against sanctions lists and regulatory warnings | OFAC SDN list, EU sanctions, UN sanctions, OpenSanctions.org, 金管會裁罰查詢 |
| 5. Cross-border flow indicators | Trade data anomalies, mispriced imports/exports, unusual trade routes | UN Comtrade, national customs data, trade databases, shipping tracking (MarineTraffic, VesselFinder) |
| 6. Crypto / digital finance | Wallet address tracing, exchange deposits/withdrawals, mixer usage | Etherscan, Blockchain.com, Arkham Intelligence, Chainalysis (public reports), OFAC sanctioned wallets |
| 7. Political-financial nexus | Campaign donations → government contracts → beneficiary companies | 政治獻金查閱平台, procurement databases, lobbying disclosures, 監察院財產申報 |

## Financial Anomaly Patterns

- **Round-tripping**: Money leaves Country A as "investment," flows through Country B shell, returns to Country A as "foreign investment" — enjoys tax benefits. Look for: same ultimate beneficial owner on both ends of a cross-border transaction.
- **Trade-based laundering**: Over/under-invoicing in import/export. A $10 widget invoiced at $10,000 creates a channel to move money. Look for: trade values dramatically different from market price, persistent trade deficits with specific counterparties.
- **Real estate layering**: Property purchased by Entity A, quickly sold to Entity B (related party) at inflated price, sold again to Entity C. Each transaction creates apparent "legitimate" profit. Look for: rapid successive transactions, circular paths, prices far above/below market.
- **Procurement corruption cycle**: Company donates to politician → politician awards government contract to company → company funnels part of profit back through intermediaries. Map the full cycle using procurement data + political donation records + corporate relationships.

## Taiwan-Specific Financial Investigation Sources

- 公開資訊觀測站 (MOPS) — public company filings, insider trades, material events, related party transactions
- 實價登錄 — actual real estate transaction prices (compare with declared values)
- 金管會裁罰資訊 — financial regulatory penalties
- 政府電子採購網 — government procurement records and winning bids
- 經濟部投審會 — foreign investment approvals (reveals cross-border flows)
