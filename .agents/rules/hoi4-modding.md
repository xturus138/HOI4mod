# HOI4 Modding Standards for Indonesia Raya R56 Submod

1. **Tag Standards**:
   - Tag is `INS` (not `DEI`).
   - Focus tree override weight: `add = 50, tag = INS`.
   - Flags kept as both `INS*.tga` and `DEI*.tga` across 3 dimensions.

2. **Encoding**:
   - Clausewitz engine strictly requires `UTF-8 with BOM` (`\xef\xbb\xbf`) on `localisation/english/DEI_indonesia_l_english.yml`.

3. **Hybrid Tree Geometry**:
   - 139 focuses total, ALL in one master file: `common/national_focus/DEI_indonesia_focus_tree.txt` (no separate per-path files despite what older docs may imply).
     - Political / Submod Branches (shared trunk + 6 ideology paths A-F): X=0..22
     - R56 Industry & Research: X=26..30
     - R56 Military AD/AU/AL: X=33..43
   - Never collide (X, Y) coordinates or break `prerequisite` IDs.
   - Each of the 6 path roots MUST have `set_politics.ruling_party` matching the ideology GROUP (per R56's own `common/ideologies/00_ideologies.txt`, not vanilla HOI4 groups) of every character offered in its `dei_leadership.N` event — see AGENTS.md section 3 for the full group table and the v1.0.2 bugfix history. Always cross-check `country_leader.ideology` in `DEI_characters.txt` before touching any path's `ruling_party`.

4. **Visuals & Events**:
   - 155 total events across `events/DEI_*.txt` (leadership, per-path, flavor MTTH, shared trunk).
   - 100% of events must define valid `picture = GFX_...`.
   - `events/indonesia.txt` is R56's own base file, overwritten by this submod ONLY to disable `indonesia.100`'s trigger (`always = no`). Never add fields inside its effect scopes via bulk regex edits without validating brace/block structure first — this caused a real corruption bug (35 misplaced `picture=` lines) fixed in v1.0.2.
   - Audit scripts in `scratch/` (`final_verification.py`, `verify_all_loc.py`, `master_audit.py`, `comprehensive_asset_audit.py`) must only glob `DEI_*.txt` files, never R56's own `indonesia.txt`/`indonesia_joint.txt` — those carry pre-existing upstream gaps outside this submod's scope.
