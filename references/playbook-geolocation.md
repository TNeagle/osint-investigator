# Geolocation Methodology

## Systematic Approach

1. **Macro indicators** (narrow to region/country): language on signs, driving side, landscape/climate, architectural tradition, infrastructure style
2. **Meso indicators** (narrow to city/area): specific landmarks, mountain silhouettes, distinctive buildings, transit signage
3. **Micro indicators** (narrow to exact location): street names, business names, unique features, Google Maps/Street View comparison
4. **Verification**: Cross-reference candidate location against ALL visible clues. A single contradicting detail means you need to reconsider.

## Advanced Techniques

**Shadow and sun analysis:**
- Measure shadow angle and length relative to objects of known height to estimate latitude and time of day.
- Sun direction (based on shadow direction) combined with estimated time narrows hemisphere and longitude range.
- Search for sun position calculators (e.g., SunCalc) to cross-reference candidate locations with the observed shadow angle.

**Weather cross-verification:**
- Once you have a candidate location and approximate date, search historical weather records for that location and date.
- Does the weather in the photo (cloud cover, rain, snow, visibility) match the historical record? If the photo shows clear skies but the candidate location had heavy rain that day, reconsider.
- Weather data sources: Weather Underground history, NOAA, local meteorological agencies.

**EXIF metadata extraction:**
- Many photos retain GPS coordinates, camera model, timestamp, and other metadata. Always check.
- Even without GPS, camera model + serial number can sometimes be traced. Timestamp helps narrow the time window.
- Photos from social media platforms usually have EXIF stripped, but photos from messaging apps, email attachments, or direct downloads may retain it.

**Reverse image search — multi-engine strategy:**
- Google Images (best for general matching)
- Yandex Images (often superior for Eastern Europe, Central Asia, and sometimes Asia)
- TinEye (best for finding original/earliest version)
- Bing Visual Search
- Search for partial crops of the image (isolating a specific sign, building, or landmark) to find more specific matches.

**Historical imagery comparison:**
- Google Earth Pro allows viewing historical satellite imagery for any location — compare current state with the photo's apparent era.
- Google Street View has a time slider showing historical captures — verify if the street scene matches at the right time period.
- Wayback Machine may have cached versions of business websites visible in the photo.
