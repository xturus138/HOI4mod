# HOI4 Modding Standards for Indonesia Raya R56 Submod

1. **Tag Standards**:
   - Tag is `INS` (not `DEI`).
   - Focus tree override weight: `add = 50, tag = INS`.
   - Flags kept as both `INS*.tga` and `DEI*.tga` across 3 dimensions.

2. **Encoding**:
   - Clausewitz engine strictly requires `UTF-8 with BOM` (`\xef\xbb\xbf`) on `localisation/english/DEI_indonesia_l_english.yml`.

3. **Hybrid Tree Geometry**:
   - 102 focuses total:
     - Political / Submod Branches: X=0..20
     - R56 Industry & Research: X=26..30 (`DEI_r56_industry.txt`)
     - R56 Military AD/AU/AL: X=33..43 (`DEI_r56_armed_forces.txt`)
   - Never collide (X, Y) coordinates or break `prerequisite` IDs.

4. **Visuals & Events**:
   - 61 total events (55 focus events + 6 MTTH flavor events in `DEI_flavor_events.txt`).
   - 100% of events must define valid `picture = GFX_...`.
