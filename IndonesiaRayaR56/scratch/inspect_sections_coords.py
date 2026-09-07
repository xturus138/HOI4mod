import re

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    text = f.read()

# Split by section
sections = text.split("# SECTION: ")
for sec in sections[1:]:
    lines = sec.splitlines()
    sec_name = lines[0].strip()
    # parse focuses in this section
    focus_ids = re.findall(r'id\s*=\s*([a-zA-Z0-9_]+)', sec)
    focus_ids = [fid for fid in focus_ids if fid != 'dei_focus_tree']
    print(f"\n--- {sec_name} ({len(focus_ids)} focuses) ---")
    for fid in focus_ids:
        # find focus block
        bm = re.search(r'focus\s*=\s*\{[^}]*id\s*=\s*' + fid + r'[^}]*\}', sec, re.DOTALL)
        if bm:
            b = bm.group(0)
            x_m = re.search(r'\bx\s*=\s*(-?\d+)', b)
            y_m = re.search(r'\by\s*=\s*(-?\d+)', b)
            rel_m = re.search(r'\brelative_position_id\s*=\s*([a-zA-Z0-9_]+)', b)
            x = x_m.group(1) if x_m else '?'
            y = y_m.group(1) if y_m else '?'
            rel = rel_m.group(1) if rel_m else 'None'
            print(f"  {fid}: x={x}, y={y}, rel={rel}")
