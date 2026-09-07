import re, os

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    content = f.read()

# Split into focus blocks using a state machine
blocks = []
lines = content.split('\n')
i = 0
while i < len(lines):
    line = lines[i]
    if line.strip().startswith("focus = {"):
        depth = 1
        start = i
        j = i + 1
        while j < len(lines):
            depth += lines[j].count("{") - lines[j].count("}")
            if depth <= 0:
                break
            j += 1
        block_text = '\n'.join(lines[start:j+1])
        
        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block_text)
        fid = id_m.group(1) if id_m else ""
        
        # Check if has available block
        has_avail = bool(re.search(r'\s*available\s*=\s*\{', block_text))
        
        # Check if available has custom_trigger_tooltip
        has_tooltip = bool(re.search(r'custom_trigger_tooltip', block_text))
        
        blocks.append({
            'start': start,
            'end': j,
            'fid': fid,
            'text': block_text,
            'has_avail': has_avail,
            'has_tooltip': has_tooltip,
        })
        i = j + 1
    else:
        i += 1

# Path roots: keep available block (with tooltip)
path_roots = {"dei_focus_a_proklamasi", "dei_focus_b_root", "dei_focus_c_root", 
              "dei_focus_d_root", "dei_focus_e_root", "dei_focus_f_root"}

modified = 0
for b in blocks:
    if b['fid'] not in path_roots and b['has_avail'] and not b['has_tooltip']:
        # Remove the available block entirely
        # Pattern: \n\t\tavailable = { ... }
        b['text'] = re.sub(
            r'\n\s*available\s*=\s*\{[^}]*\}',
            '',
            b['text'],
            count=1
        )
        modified += 1

# Rebuild
new_lines = []
for idx, b in enumerate(blocks):
    # Add gap lines between blocks
    if idx > 0:
        gap_start = blocks[idx-1]['end'] + 1
        gap_end = b['start']
        if gap_start <= gap_end:
            new_lines.extend(lines[gap_start:gap_end])
    new_lines.extend(b['text'].split('\n'))

# Add trailing lines
last_block = blocks[-1]
if last_block['end'] + 1 < len(lines):
    new_lines.extend(lines[last_block['end']+1:])

result = '\n'.join(new_lines)

with open(tree_path, "w", encoding="utf-8") as f:
    f.write(result)

print(f"Removed {modified} raw available blocks from non-root subfocuses.")

# Verify
with open(tree_path, "r", encoding="utf-8") as f:
    verify = f.read()

# Count available blocks that have has_country_flag but NO custom_trigger_tooltip
import re as re2
# Find all available = { ... } blocks
avail_pattern = re2.compile(r'available\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}', re2.DOTALL)
raw_count = 0
tooltip_count = 0
for m in avail_pattern.finditer(verify):
    block = m.group(1)
    if 'has_country_flag' in block:
        if 'custom_trigger_tooltip' in block:
            tooltip_count += 1
        else:
            raw_count += 1

print(f"Remaining raw (bad): {raw_count}")
print(f"With tooltip (good): {tooltip_count}")
