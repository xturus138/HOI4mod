import re, os

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    content = f.read()

# Strategy: for each focus block, if id is NOT a path root,
# remove any available = { ... } block that contains ONLY has_country_flag (no custom_trigger_tooltip)

# Parse focus blocks properly
blocks = []
lines = content.split('\n')
i = 0
while i < len(lines):
    if lines[i].strip().startswith("focus = {"):
        depth = 1
        start = i
        j = i + 1
        while j < len(lines):
            depth += lines[j].count("{") - lines[j].count("}")
            if depth <= 0:
                break
            j += 1
        block_lines = lines[start:j+1]
        block_text = '\n'.join(block_lines)
        
        # Get id
        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block_text)
        fid = id_m.group(1) if id_m else ""
        blocks.append((start, fid, block_text, j))
        i = j + 1
    else:
        i += 1

# Path roots keep their available block
path_roots = {
    "dei_focus_a_proklamasi": True,
    "dei_focus_b_root": True,
    "dei_focus_c_root": True,
    "dei_focus_d_root": True,
    "dei_focus_e_root": True,
    "dei_focus_f_root": True,
}

modified = 0
new_blocks = []
for start, fid, block_text, end in blocks:
    if fid not in path_roots:
        # Remove available = { ... } that has only has_country_flag (no custom_trigger_tooltip)
        # Match multiline available blocks
        pattern = re.compile(
            r'\s*available\s*=\s*\{\s*has_country_flag\s*=\s*[a-zA-Z0-9_]+_chosen\s*\}',
            re.MULTILINE
        )
        if pattern.search(block_text):
            block_text = pattern.sub('', block_text)
            modified += 1
    new_blocks.append(block_text)

# Rebuild content
new_content = []
for idx, (start, fid, block_text, end) in enumerate(blocks):
    if idx == 0:
        new_content.append(block_text)
    else:
        gap = '\n'.join(lines[end+1:start])
        new_content.append(gap)
        new_content.append(block_text)

# Add trailing content
last_end = blocks[-1][3]
if last_end < len(lines) - 1:
    new_content.append('\n'.join(lines[last_end+1:]))

result = '\n'.join(new_content)

with open(tree_path, "w", encoding="utf-8") as f:
    f.write(result)

print(f"Removed {modified} raw available blocks from non-root subfocuses.")

# Verify
with open(tree_path, "r", encoding="utf-8") as f:
    verify = f.read()

# Count available blocks with has_country_flag but NO custom_trigger_tooltip
bad = re.findall(r'available\s*=\s*\{[^}]*has_country_flag[^}]*\}', verify)
good = re.findall(r'available\s*=\s*\{[^}]*custom_trigger_tooltip[^}]*has_country_flag[^}]*\}', verify)
print(f"Bad (raw flags): {len(bad)}")
print(f"Good (with tooltip): {len(good)}")
