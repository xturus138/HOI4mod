import re, os

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    content = f.read()

# Path root IDs (only these keep available with tooltip)
path_roots = {
    "dei_focus_a_proklamasi": "dei_path_a_chosen",
    "dei_focus_b_root": "dei_path_b_chosen",
    "dei_focus_c_root": "dei_path_c_chosen",
    "dei_focus_d_root": "dei_path_d_chosen",
    "dei_focus_e_root": "dei_path_e_chosen",
    "dei_focus_f_root": "dei_path_f_chosen",
}

# Strategy: parse all focus blocks, for each block:
# - if it's a path root, keep available block (already has custom_trigger_tooltip)
# - if it's a subfocus, remove available = { has_country_flag = ... } entirely

# Parse focus blocks
blocks = []
depth = 0
cur = []
in_focus = False
block_starts = []
for i, line in enumerate(content.splitlines()):
    if line.strip().startswith("focus = {"):
        in_focus = True
        depth = 1
        cur = [line]
        block_starts.append(i)
        continue
    if in_focus:
        cur.append(line)
        depth += line.count("{") - line.count("}")
        if depth <= 0:
            in_focus = False
            blocks.append((block_starts[-1], "\n".join(cur)))
            cur = []
            block_starts.pop()

# Process each block
new_content = []
last_end = 0
for start, block in blocks:
    # Find the id
    id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block)
    fid = id_m.group(1) if id_m else ""
    
    # Check if this is a path root
    is_path_root = fid in path_roots
    
    if not is_path_root:
        # Remove available = { has_country_flag = dei_path_X_chosen }
        # Pattern: available = { ... } where content is just has_country_flag
        block = re.sub(
            r'\s*available\s*=\s*\{\s*has_country_flag\s*=\s*[a-zA-Z0-9_]+_chosen\s*\}',
            '',
            block
        )
    
    # Write content from last_end to start, then the block, then gap to next
    new_content.append(content[last_end:start])
    new_content.append(block)
    last_end = start + len(block) + 1  # +1 for newline

# Append remaining
new_content.append(content[last_end:])

new_text = "".join(new_content)

with open(tree_path, "w", encoding="utf-8") as f:
    f.write(new_text)

# Count removed
removed = len(re.findall(r'has_country_flag\s*=\s*[a-zA-Z0-9_]+_chosen', content)) - len(re.findall(r'has_country_flag\s*=\s*[a-zA-Z0-9_]+_chosen', new_text))
print(f"Removed {removed} raw has_country_flag lines from subfocuses. Kept {len(re.findall(r'has_country_flag', new_text))} total (path roots + allow_branch).")
