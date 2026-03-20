# NetworkX v2 JSON Schema

> **Load this file when building or updating the intelligence graph.**
> See full implementation in `scripts/network_analysis.py`.

## Entities

Fields: `id`, `label`, `type`, `notes`, `first_seen`, `last_seen`, `investigation_depth` (none/shallow/medium/deep), `tags`, `behavioral`

**Entity types**: person, organization, address, domain, account, financial, wallet, vessel, aircraft, vehicle, property, species, media_outlet, bot_account, satellite_target, legal_case

## Edges

Fields: `source`, `target`, `relation`, `weight`, `evidence`, `date`, `edge_type`

**Edge types**: ownership, directorship, financial, social, legal, location, employment, family, digital, transaction, trades_in, ships_via, amplifies, cites, litigates, operates, tracks, publishes

## Events

Fields: `id`, `description`, `date`, `entities_involved`, `significance`

## Important

🔴 **Include inline confidence tags in `notes` and `evidence` fields.**

## Commands

```bash
pip install networkx matplotlib --break-system-packages -q

python <skill-path>/scripts/network_analysis.py --input data.json --output-dir ./output
python <skill-path>/scripts/network_analysis.py --input base.json --merge sub1.json sub2.json --output-dir ./output
python <skill-path>/scripts/network_analysis.py --input data.json --output-dir ./output --find-path entity_id_1 entity_id_2
```
