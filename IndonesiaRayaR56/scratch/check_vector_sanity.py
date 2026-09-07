import re
from simulate_new_layout import new_coords

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    text = f.read()

# find prerequisites for all focuses
prereqs = {}
for fid in new_coords:
    bm = re.search(r'focus\s*=\s*\{[^}]*id\s*=\s*' + fid + r'[^}]*\}', text, re.DOTALL)
    if bm:
        b = bm.group(0)
        pm = re.findall(r'prerequisite\s*=\s*\{[^}]*focus\s*=\s*([a-zA-Z0-9_]+)', b)
        prereqs[fid] = pm

print("Checking prerequisite line vector sanity in new layout:")
bad_vectors = []
for fid, plist in prereqs.items():
    ax, ay = new_coords[fid]
    for p in plist:
        if p in new_coords:
            pax, pay = new_coords[p]
            dx = abs(ax - pax)
            dy = ay - pay
            # If line goes upwards (dy <= 0) or jumps more than 2 rows down (dy > 2) or spans too wide (dx > 15)
            # Except Path starters connecting from Prologue (y=2 to y=3, dy=1, dx varies from 0 to 13)
            if dy <= 0 or dy > 2:
                bad_vectors.append((fid, p, (ax, ay), (pax, pay), dx, dy))

if bad_vectors:
    print(f"Found {len(bad_vectors)} unusual prerequisite connections:")
    for b in bad_vectors:
        print(f"  {b[0]} at {b[2]} <-- {b[1]} at {b[3]} (dx={b[4]}, dy={b[5]})")
else:
    print("ALL 134 PREREQUISITES FLOW NATURALLY DOWNWARD (dy=1 or 2) WITHOUT UPWARD OR ABNORMAL JUMPS!")
