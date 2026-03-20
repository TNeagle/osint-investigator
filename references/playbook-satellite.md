# Satellite & Aerial Imagery Intelligence (IMINT) Playbook

## Satellite Imagery Sources

| Source | Resolution | Cost | Best For |
|---|---|---|---|
| Google Earth Pro | ~0.5m (historical imagery available) | Free | Historical comparison, time-lapse analysis, general reconnaissance |
| Sentinel Hub (Copernicus) | 10m (optical), 5m (SAR) | Free | Large-area monitoring, change detection, environmental tracking |
| Planet Labs | ~3m daily | Paid (some free access) | Near-daily revisit for monitoring construction, military, agriculture |
| Maxar (via Google/Bing) | ~0.3m | Embedded in maps | Highest resolution freely available through map services |
| FIRMS (NASA) | 1km thermal | Free | Active fire detection worldwide, real-time |

## Change Detection Methodology

The core IMINT technique: compare imagery from different dates to detect what changed.

**Step-by-step:**
1. Identify the location and approximate time period of interest
2. Obtain imagery from BEFORE the event/period
3. Obtain imagery from AFTER the event/period
4. Systematically compare: new structures, removed structures, land use changes, vehicle/ship presence changes, road/infrastructure changes
5. Document findings with annotated screenshots showing before/after

**What to look for:**
- **Construction activity**: New buildings, excavation, scaffolding, construction equipment, material stockpiles
- **Military/security**: New checkpoints, barriers, fortifications, vehicle concentrations, runway extensions
- **Environmental**: Deforestation boundaries, water body changes, pollution plumes, agricultural conversion
- **Industrial**: Factory expansion, storage tank farm changes, waste dumping, new infrastructure connections
- **Disaster assessment**: Damage extent, flooding boundaries, structural collapse, evacuation patterns

## Facility Analysis

When analyzing a specific facility from satellite imagery:
- **Perimeter**: Fencing, walls, guard posts, access control points
- **Buildings**: Count, size estimates (use known reference objects for scale), function assessment
- **Vehicles**: Types, quantities, parking patterns (regular business hours vs. unusual activity)
- **Infrastructure**: Power lines, water/sewage, road quality, rail connections
- **Activity indicators**: Thermal signatures, smoke/emissions, loading docks, container stacking patterns

## Ship and Port Analysis

- **Port activity**: Container counts, ship sizes, berth utilization changes over time
- **Dark ships**: Vessels visible on satellite imagery but not broadcasting AIS — potentially illicit activity
- **Ship-to-ship transfer**: Two vessels in close proximity at sea, away from port — potential sanctions evasion or smuggling
- **Fishing fleet monitoring**: Detect illegal fishing in protected areas through vessel density analysis

## Taiwan/Regional Applications

- **Cross-strait military monitoring**: PLA base construction, naval vessel deployments, amphibious exercise staging
- **Land development monitoring**: Illegal hillside construction, protected farmland conversion
- **Industrial pollution**: Factory emission changes, wastewater discharge points, waste dumping sites
- **Infrastructure projects**: Track actual construction progress vs. official timeline and budget
