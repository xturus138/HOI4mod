import re
import os

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    text = f.read()

# Parse all focuses
i = 0
focuses = {}
while True:
    idx = text.find("focus = {", i)
    if idx == -1: idx = text.find("focus={", i)
    if idx == -1: break
    start = text.find("{", idx)
    pos = start
    bc = 0
    while pos < len(text):
        if text[pos] == '{': bc += 1
        elif text[pos] == '}':
            bc -= 1
            if bc == 0:
                block = text[idx:pos+1]
                fid = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block).group(1)
                x = int(re.search(r'\bx\s*=\s*(-?\d+)', block).group(1))
                y = int(re.search(r'\by\s*=\s*(-?\d+)', block).group(1))
                rel_m = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', block)
                rel = rel_m.group(1) if rel_m else None
                icon = re.search(r'\bicon\s*=\s*([a-zA-Z0-9_]+)', block).group(1)
                prereqs = re.findall(r'prerequisite\s*=\s*\{[^}]*focus\s*=\s*([a-zA-Z0-9_]+)', block)
                mutually = re.findall(r'mutually_exclusive\s*=\s*\{[^}]*focus\s*=\s*([a-zA-Z0-9_]+)', block)
                focuses[fid] = {
                    'x': x, 'y': y, 'rel': rel, 'icon': icon,
                    'prereqs': prereqs, 'mutually': mutually
                }
                i = pos + 1
                break
        pos += 1
    else: break

# Calculate absolute positions
def get_abs(fid, visited=None):
    if visited is None: visited = set()
    if fid in visited: return (0, 0)
    visited.add(fid)
    d = focuses[fid]
    if d['rel'] and d['rel'] in focuses:
        px, py = get_abs(d['rel'], visited)
        return (px + d['x'], py + d['y'])
    return (d['x'], d['y'])

print(f"Total parsed focuses: {len(focuses)}")
abs_coords = {}
for fid, dat in focuses.items():
    abs_coords[fid] = get_abs(fid)

# Print min and max X, Y per branch/section
print("\n=== ABSOLUTE POSITIONS OF KEY BRANCHES ===")
prologue = ['dei_focus_root', 'dei_focus_pembangkangan', 'dei_focus_momentum_kemerdekaan']
for p in prologue:
    print(f"Prologue {p}: raw=({focuses[p]['x']}, {focuses[p]['y']}) -> abs={abs_coords[p]}")

# Path starters
path_starters = {
    'Path A': 'dei_focus_a_proklamasi',
    'Path B': 'dei_focus_b_root',
    'Path C': 'dei_focus_c_root',
    'Path D': 'dei_focus_d_root',
    'Path E': 'dei_focus_e_root',
    'Path F': 'dei_focus_f_root',
    'Industry': 'INS_industrial_centralisation',
    'Armed Forces 1': 'INS_army_of_the_dutch_east_indies',
    'Armed Forces 2': 'INS_the_test_flight_service',
    'Armed Forces 3': 'INS_komando_pertahanan_maritim'
}

for name, fid in path_starters.items():
    if fid in focuses:
        print(f"{name} ({fid}): raw=({focuses[fid]['x']}, {focuses[fid]['y']}) rel={focuses[fid]['rel']} -> abs={abs_coords[fid]}")

# Check long distance prerequisites
print("\n=== PREREQUISITE DISTANCE CHECK (Absolute DX, DY) ===")
long_lines = []
for fid, dat in focuses.items():
    ax, ay = abs_coords[fid]
    for p in dat['prereqs']:
        if p in abs_coords:
            pax, pay = abs_coords[p]
            dx = abs(ax - pax)
            dy = ay - pay
            if dy < 0 or dx > 10 or dy > 4:
                long_lines.append((fid, p, (ax, ay), (pax, pay), dx, dy))

print(f"Total problematic / abnormally long prerequisite lines: {len(long_lines)}")
for fid, p, cur, par, dx, dy in long_lines[:25]:
    print(f"  {fid} at {cur} <-- {p} at {par} | dx={dx}, dy={dy}")
