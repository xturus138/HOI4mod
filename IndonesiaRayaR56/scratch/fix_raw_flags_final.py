import re

tree_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(tree_path, "r", encoding="utf-8") as f:
    content = f.read()

# Path root IDs that KEEP their available block (with custom_trigger_tooltip)
path_roots = {
    "dei_focus_a_proklamasi",
    "dei_focus_b_root",
    "dei_focus_c_root",
    "dei_focus_d_root",
    "dei_focus_e_root",
    "dei_focus_f_root",
}

# Parse all focus blocks
lines = content.split('\n')
new_lines = []
i = 0
removed = 0

while i < len(lines):
    line = lines[i]
    
    # Check if this line starts a focus block
    if line.strip().startswith("focus = {"):
        # Collect entire block
        depth = 1
        block_start = i
        j = i + 1
        while j < len(lines):
            depth += lines[j].count("{") - lines[j].count("}")
            if depth <= 0:
                break
            j += 1
        
        block = lines[block_start:j+1]
        block_text = '\n'.join(block)
        
        # Get focus id
        id_m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', block_text)
        fid = id_m.group(1) if id_m else ""
        
        if fid not in path_roots:
            # Remove lines matching: available = { has_country_flag = dei_path_X_chosen }
            # Could be single line or multiline
            filtered = []
            skip_avail = False
            brace_depth = 0
            for bl in block:
                stripped = bl.strip()
                
                if skip_avail:
                    brace_depth += bl.count("{") - bl.count("}")
                    if brace_depth <= 0:
                        skip_avail = False
                    continue
                
                # Check if this line starts an available block with has_country_flag only
                if re.match(r'\s*available\s*=\s*\{\s*has_country_flag\s*=\s*[a-zA-Z0-9_]+_chosen\s*\}', stripped):
                    removed += 1
                    continue
                elif re.match(r'\s*available\s*=\s*\{\s*$', stripped):
                    # Multi-line available block - check next line
                    # Look ahead in remaining block
                    idx_in_filtered = len(filtered)
                    if idx_in_filtered + 1 < len(block):
                        next_line = block[idx_in_filtered + 1].strip()
                        if re.match(r'has_country_flag\s*=\s*[a-zA-Z0-9_]+_chosen', next_line):
                            # Skip this line and next lines until closing }
                            skip_avail = True
                            brace_depth = bl.count("{") - bl.count("}")
                            removed += 1
                            continue
                
                filtered.append(bl)
            
            new_lines.extend(filtered)
        else:
            new_lines.extend(block)
        
        i = j + 1
    else:
        new_lines.append(line)
        i += 1

result = '\n'.join(new_lines)

with open(tree_path, "w", encoding="utf-8") as f:
    f.write(result)

# Verify
with open(tree_path, "r", encoding="utf-8") as f:
    verify = f.read()

avail_pattern = re.compile(r'available\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}', re.DOTALL)
raw_count = 0
tooltip_count = 0
for m in avail_pattern.finditer(verify):
    block = m.group(1)
    if 'has_country_flag' in block:
        if 'custom_trigger_tooltip' in block:
            tooltip_count += 1
        else:
            raw_count += 1

print(f"Removed {removed} raw available blocks")
print(f"Raw (bad): {raw_count}")
print(f"With tooltip (good): {tooltip_count}")
