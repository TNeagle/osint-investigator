# Legal & Litigation Intelligence Playbook

## Court Records Deep Analysis

Court judgments are often the most detailed public factual record available — far more detailed than news.

| Investigation Layer | What to Extract | Intelligence Value |
|---|---|---|
| 1. Judgment fact patterns | Names, dates, amounts, locations, relationships stated as findings of fact by the court | Court-verified facts; stronger than news claims |
| 2. Litigation network mapping | Who sues whom, co-defendants, co-plaintiffs, witnesses, legal representatives | Reveals hidden adversarial and cooperative relationships |
| 3. Repeat litigant patterns | Same entity appearing in multiple cases as plaintiff or defendant | Serial litigators often reveal business patterns (aggressive IP enforcement, debt collection operations, labor disputes) |
| 4. Legal representative analysis | Which law firms represent which entities | Shared legal representation between supposedly unrelated entities suggests hidden connections |
| 5. Administrative penalties | Regulatory fines, license revocations, compliance orders | Reveals violations that may not make the news |
| 6. Bankruptcy and insolvency | Creditor lists, asset declarations, restructuring plans | Exposes true financial position and creditor relationships |

## Judgment Text Mining

When you access a court judgment, extract systematically:
- **Parties**: All named individuals and entities, their roles (plaintiff, defendant, witness, third party)
- **Facts found by the court**: These are judicially verified — higher reliability than any other public source
- **Financial details**: Transaction amounts, asset values, damages awarded, settlement terms
- **Timeline**: The court's reconstruction of events, often minute-by-minute for criminal cases
- **Connections**: Relationships between parties stated in the judgment
- **Prior proceedings**: References to related cases (follow the chain)

## Taiwan Legal Sources

- **司法院裁判書查詢系統**: Full text of court judgments searchable by party name, case type, date
- **法務部行政執行署**: Administrative enforcement records
- **公平交易委員會裁處書**: Competition law decisions
- **智慧財產法院**: IP-specific litigation
- **Search patterns**: `"[NAME]" site:judicial.gov.tw`, `"[COMPANY]" 判決`, `"[NAME]" 起訴 OR 被告`

## International Legal Sources

- **US**: PACER (federal courts), state court dockets, SEC enforcement actions, OFAC designations
- **UK**: Courts and Tribunals Judiciary, Companies House disqualification orders
- **EU**: CJEU case law, European Commission decisions
- **International**: ICJ, WTO dispute settlement, international arbitration awards (ICSID)

## Litigation Network Analysis with NetworkX

Model litigation relationships as a graph:
- **Nodes**: Parties (person/organization), law firms, judges, cases
- **Edges**: plaintiff_in, defendant_in, represents, presides_over, witness_in, related_case
- **Analysis**: Community detection reveals litigation clusters; same law firm representing multiple entities = hidden relationship; co-defendant patterns reveal organizational structure
