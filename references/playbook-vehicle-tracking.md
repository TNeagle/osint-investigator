# Vehicle, Vessel & Aircraft Tracking Playbook

## Maritime Vessel Tracking

| Technique | Tools | What It Reveals |
|---|---|---|
| AIS tracking | MarineTraffic, VesselFinder, MyShipTracking | Real-time and historical vessel positions, routes, port calls, speed |
| AIS gap analysis | Compare expected route with actual AIS data | Vessels going "dark" (turning off AIS) = suspicious, especially near sanctioned countries |
| Ship registry lookup | IMO number search, flag state registries, Equasis | Ownership chains, flag history, classification society, inspection records |
| Ship-to-ship transfer detection | Satellite imagery + AIS data cross-reference | Vessels meeting at sea for cargo transfer — sanctions evasion or smuggling indicator |
| Port call history | MarineTraffic port calls feature | Travel patterns, trade relationships, frequency of visits to specific ports |

**Maritime red flags:**
- Flag changes (reflagging to avoid sanctions)
- Name changes (vessels renamed to obscure history)
- AIS manipulation (spoofed location, falsified identity)
- Visits to sanctioned ports (North Korea, Iran, Syria, Crimea)
- Unusual loitering patterns at sea

## Aviation Tracking

| Technique | Tools | What It Reveals |
|---|---|---|
| ADS-B tracking | FlightRadar24, FlightAware, ADS-B Exchange | Real-time and historical flight paths, altitude, speed |
| Aircraft registry | FAA N-number lookup, national civil aviation registries | Owner/operator identity, registration history |
| Private jet tracking | ADS-B Exchange (unfiltered), flight pattern analysis | Travel patterns of executives, politicians, oligarchs |
| Military aircraft monitoring | ADS-B Exchange (military filters), planespotting communities | Military movements, reconnaissance patterns, exercises |
| Charter flight analysis | FBO records, handling agent websites | Who is chartering flights and from where |

**Aviation investigation techniques:**
- Track an individual's private jet to map their actual travel (vs. public schedule)
- Detect meetings by finding two aircraft at the same small airport at the same time
- Monitor military transport flights to detect supply chain movements
- Track government aircraft for diplomatic and intelligence activity

## Vehicle Identification

| Element | What to Analyze | Intelligence Value |
|---|---|---|
| License plate format | Country/region-specific patterns, special plate types | Identifies origin jurisdiction; diplomatic plates, military plates, government plates |
| Vehicle make/model | Distinctive features, regional market availability | Narrows geographic origin (some models only sold in specific markets) |
| VIN decoding | 17-digit Vehicle Identification Number structure | Manufacturing plant, model year, specifications |
| Fleet identification | Matching vehicles, livery, markings | Organizational affiliation, logistics patterns |
| Dashcam/traffic camera | Publicly accessible traffic cameras, user-uploaded dashcam footage | Time-stamped location evidence |

## Sanctions Evasion Tracking

Combine vessel, aircraft, and corporate intelligence to detect sanctions evasion networks:
1. **Identify the vessel/aircraft** involved in suspicious activity
2. **Trace ownership** through flag state registries, beneficial ownership chains
3. **Map the network**: Who owns the management company? Who insures the vessel? Who provides the crew?
4. **Cross-reference with sanctions lists**: OFAC, EU, UN sanctions lists for entities and vessels
5. **Check for deceptive practices**: Flag changes, AIS manipulation, name changes, midnight ownership transfers
