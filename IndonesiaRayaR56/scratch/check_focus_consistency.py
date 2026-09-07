import os
import re

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    content = f.read()

# Match top-level focus blocks
blocks = []
depth = 0
cur = []
in_focus = False
for line in content.splitlines():
    stripped = line.strip()
    if stripped.startswith("focus = {"):
        in_focus = True
        depth = 1
        cur = [line]
        continue
    if in_focus:
        cur.append(line)
        depth += line.count("{") - line.count("}")
        if depth <= 0:
            in_focus = False
            blocks.append("\n".join(cur))
            cur = []

print(f"Total focus blocks parsed: {len(blocks)}")

focuses = {}
for b in blocks:
    id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', b)
    if not id_m: continue
    fid = id_m.group(1)
    
    xm = re.search(r'\bx\s*=\s*(-?\d+)', b)
    ym = re.search(r'\by\s*=\s*(-?\d+)', b)
    x = int(xm.group(1)) if xm else 0
    y = int(ym.group(1)) if ym else 0
    
    rel_m = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', b)
    rel = rel_m.group(1) if rel_m else None
    
    prereqs = []
    for pm in re.finditer(r'prerequisite\s*=\s*\{([^}]+)\}', b):
        for p in re.findall(r'focus\s*=\s*([a-zA-Z0-9_]+)', pm.group(1)):
            prereqs.append(p)
            
    icon_m = re.search(r'\bicon\s*=\s*([a-zA-Z0-9_]+)', b)
    icon = icon_m.group(1) if icon_m else None
    
    focuses[fid] = {'x': x, 'y': y, 'rel': rel, 'prereqs': prereqs, 'icon': icon, 'block': b}

print(f"Total focuses registered: {len(focuses)}")

# Verify all relative_position_id and prerequisites
errors = []
for fid, data in focuses.items():
    if data['rel'] and data['rel'] not in focuses:
        errors.append(f"{fid}: missing relative anchor '{data['rel']}'")
    for p in data['prereqs']:
        if p not in focuses:
            errors.append(f"{fid}: missing prerequisite focus '{p}'")

print(f"Consistency errors: {len(errors)}")
for e in errors:
    print(f"  {e}")

# Calculate absolute coordinates and check overlaps
def get_abs_pos(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return (0, 0)
    visited.add(fid)
    f = focuses[fid]
    if not f['rel']:
        return (f['x'], f['y'])
    px, py = get_abs_pos(f['rel'], visited)
    return (px + f['x'], py + f['y'])

coords = {}
overlaps = []
for fid in focuses:
    ax, ay = get_abs_pos(fid)
    if (ax, ay) in coords:
        overlaps.append((fid, coords[(ax, ay)], (ax, ay)))
    else:
        coords[(ax, ay)] = fid

print(f"Position overlaps: {len(overlaps)}")
for f1, f2, pos in overlaps:
    print(f"  Overlap at {pos}: {f1} and {f2}")
