# Cryptocurrency & Blockchain Deep Investigation Playbook

## On-Chain Analysis Methodology

| Investigation Layer | Technique | Tools & Sources |
|---|---|---|
| 1. Wallet profiling | Analyze transaction history, balance over time, first/last activity, transaction frequency | Etherscan, Blockchain.com, Solscan, Arkham Intelligence |
| 2. Wallet clustering | Identify wallets belonging to same entity through common spending patterns, change addresses, or known heuristics | Arkham Intelligence labels, OXT.me (Bitcoin), Breadcrumbs.app |
| 3. Exchange interactions | Identify deposits to / withdrawals from known exchange wallets | Exchange wallet labels (Etherscan labels, Arkham), large round-number transactions |
| 4. Mixer / privacy tool usage | Detect interaction with Tornado Cash, ChipMixer, CoinJoin, or similar | OFAC sanctioned mixer addresses, known mixer contract addresses |
| 5. DeFi protocol interactions | Track swaps, liquidity provision, lending, yield farming across protocols | DeFi protocol dashboards, Dune Analytics, DeBank |
| 6. Cross-chain tracking | Follow funds bridged between chains (Ethereum → BSC → Polygon etc.) | Bridge contract interactions, Arkham cross-chain view |
| 7. NFT transaction analysis | Detect wash trading (selling to yourself to inflate value), money laundering through NFT purchases | OpenSea history, NFT marketplace transaction data |

## Wallet Behavioral Patterns

**Suspicious patterns:**
- **Peeling chain**: Large amount split into smaller and smaller transactions across many wallets — classic laundering structure
- **Consolidation**: Many small wallets sending to one address — collecting from multiple victims or aggregating proceeds
- **Timing patterns**: Transactions always at specific times may indicate automated scripts or timezone clues
- **Dust attacks**: Tiny amounts sent to many wallets to de-anonymize users by tracking subsequent consolidation
- **Immediate forwarding**: Funds received and immediately sent elsewhere (within 1-2 blocks) = pass-through wallet, not end destination

## Crypto Scam Investigation

- **Rug pull indicators**: Liquidity removed suddenly, contract owner has special withdrawal functions, token contract not renounced
- **Ponzi/pyramid patterns**: New deposits funding old withdrawals, referral structures visible on-chain, decreasing withdrawal ability over time
- **Fake token detection**: Token name mimicking legitimate project, deployed by anonymous address, no liquidity lock
- **Exchange fraud**: Proof of reserves analysis, on-chain withdrawal patterns showing insolvency before public collapse

## Connecting On-Chain to Off-Chain Identity

- **ENS / domain names**: Ethereum Name Service registrations link wallets to human-readable names, sometimes revealing identity
- **Social media self-disclosure**: People posting wallet addresses on Twitter, Discord, Telegram for payments/donations
- **OFAC sanctioned wallets**: US Treasury publishes wallet addresses associated with sanctioned entities
- **Exchange KYC bridges**: If funds enter a regulated exchange, the exchange holds KYC data (not publicly available, but the fact of the exchange interaction is visible)
- **Arkham Intelligence labels**: Community-sourced and algorithmic entity labels for major wallets

## NetworkX Integration

Model blockchain flows as a directed graph:
- **Nodes**: Wallets, exchanges, DeFi protocols, mixer contracts (type: wallet, exchange, defi, mixer, unknown)
- **Edges**: transactions with amount, timestamp, and chain identifier
- **Tags**: `mixer_interaction`, `sanctioned`, `exchange_deposit`, `peeling_chain`, `consolidation`
- **Analysis**: Financial chain detection finds laundering paths; temporal clustering detects coordinated movements; community detection reveals wallet clusters belonging to same entity
