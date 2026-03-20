# Wildlife, Flora & Fauna Investigation Playbook

**Source priority:** Start with biodiversity databases (IUCN, CITES, GBIF, iNaturalist) and enforcement records (seizure databases, RFMO IUU vessel lists, Global Fishing Watch). For trafficking investigations, search platform trade keywords directly on social media and e-commerce sites — do NOT search for "news articles about wildlife trafficking" as your primary approach. News reports about seizures are useful leads, but verify every claim against the actual databases below.

## Species Identification from Photos

| What to Analyze | Technique | Sources |
|---|---|---|
| Animal species ID | Visual features: morphology, coloring, size relative to surroundings, habitat context | iNaturalist, GBIF, field guides, Google Lens, Merlin Bird ID (for birds) |
| Plant species ID | Leaf shape, flower structure, bark texture, growth form, habitat context | iNaturalist, PlantNet, GBIF, regional flora databases |
| Geographic range verification | Cross-reference identified species with known distribution range | IUCN Red List range maps, GBIF occurrence data, eBird |
| Habitat analysis | Ecosystem type, elevation indicators, climate zone, associated species | Cross-reference visible vegetation/terrain with species requirements |
| Seasonal indicators | Flowering/fruiting state, plumage, migration patterns | Phenology databases, eBird migration data |

## Conservation Status Assessment

Once a species is identified:
1. **Check IUCN Red List** (iucnredlist.org): Conservation status (CR, EN, VU, NT, LC), population trends, threats
2. **Check CITES appendices** (checklist.cites.org): Trade restrictions (Appendix I = banned, II = regulated, III = monitored)
3. **Check national protection lists**: 台灣野生動物保育法 species lists, US ESA listings, EU Habitats Directive annexes
4. **Assess trade implications**: Is this species commonly trafficked? What are the legal penalties?

## Wildlife Trafficking Investigation

**Investigation approach:** Search platforms DIRECTLY for trade keywords (see multilingual keyword list below). Your primary sources are the actual marketplace listings, social media posts, and shipping records — not news articles about trafficking. News is useful only as a secondary source to identify known routes, species, and networks that you then verify independently.

| Investigation Layer | Technique | Red Flag Signals |
|---|---|---|
| 1. Online marketplace monitoring | Search social media, e-commerce platforms, messaging apps for wildlife trade keywords | Coded language ("special delivery," "exotic pet"), private group sales, crypto payment requests |
| 2. Shipping route analysis | Track known trafficking routes, correlate with seized shipment data | Goods routed through transit hubs known for weak enforcement |
| 3. Trader network mapping | Map sellers, buyers, intermediaries, logistics providers | Same phone numbers/accounts across multiple listings; repeat sellers |
| 4. Product identification | Identify species from processed products (ivory, traditional medicine, skins, timber) | Material analysis, trademark patterns, packaging origins |
| 5. Legal entity investigation | Companies involved in wildlife trade — check permits, CITES documentation | Permits that don't match actual trade volumes; expired or forged documentation |

**Common trafficking keywords (multilingual):**
- Chinese: 活體, 標本, 象牙, 犀牛角, 穿山甲, 珍稀, 野味
- English: live specimen, taxidermy, ivory, rhino horn, pangolin, exotic pet, bushmeat
- Code words: "white gold" (ivory), "special horn" (rhino), "scale" (pangolin)

## Illegal Logging & Deforestation

- **Satellite monitoring**: Global Forest Watch alerts for near-real-time deforestation detection; Sentinel-2 imagery for forest cover change
- **Timber tracking**: Match timber species and origin claims with satellite-verified forest loss; check FSC/PEFC certification validity
- **Supply chain tracing**: Follow timber from forest to export using customs data, mill registrations, and transportation records
- **Taiwan relevance**: Check for illegal logging in mountain areas, protected forest encroachment, imported timber from high-risk origins (Myanmar, Solomon Islands, Papua New Guinea)

## Illegal Fishing Investigation

- **Vessel monitoring**: Cross-reference AIS data with fishing license registries; detect fishing in marine protected areas
- **IUU fishing flags**: Vessels on RFMO IUU vessel lists (WCPFC, IOTC, ICCAT); flag state blacklists
- **Transshipment detection**: Refrigerated cargo vessels meeting fishing boats at sea — enables laundering of illegal catch
- **Labor abuse indicators**: Vessel-specific complaints on platforms like Global Fishing Watch, Environmental Justice Foundation reports

## Biodiversity Databases

| Database | Coverage | Access |
|---|---|---|
| GBIF (Global Biodiversity Information Facility) | Global species occurrences | Free, gbif.org |
| iNaturalist | Community-verified species observations with photos/GPS | Free, inaturalist.org |
| IUCN Red List | Conservation status for 150,000+ species | Free, iucnredlist.org |
| CITES Trade Database | International wildlife trade records | Free, trade.cites.org |
| eBird | Bird observations worldwide | Free, ebird.org |
| Global Forest Watch | Forest cover change, fire alerts | Free, globalforestwatch.org |
| Global Fishing Watch | Vessel tracking, fishing activity | Free, globalfishingwatch.org |
| TW Biodiversity (台灣生物多樣性網絡) | Taiwan species data | Free, tbn.biodiv.tw |

## NetworkX Integration

Model wildlife/environmental crime networks:
- **Nodes**: Traders, buyers, logistics companies, online accounts, locations, species, vessels
- **Edges**: sells_to, ships_via, operates_at, trades_in (with species, quantities, dates)
- **Tags**: `cites_appendix_i`, `protected_species`, `repeat_offender`, `transit_hub`
- **Analysis**: Map trafficking routes; identify network hubs; detect repeat offenders across platforms
