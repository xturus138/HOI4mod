import re, os

r56_path = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\common\national_focus\indonesia_joint.txt"
with open(r56_path, "r", encoding="utf-8", errors="ignore") as f:
    txt = f.read()

# Parse all joint_focus blocks properly using brace counting
lines = txt.split('\n')
new_lines = []
i = 0
added = 0

while i < len(lines):
    line = lines[i]
    
    # Check if this line starts a joint_focus block
    if re.match(r'\s*joint_focus\s*=\s*\{', line):
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
        
        # Check if already has allow_branch
        if 'allow_branch' not in block_text:
            # Find the id line and insert allow_branch after it
            for k, bl in enumerate(block):
                if re.match(r'\s*id\s*=\s*', bl):
                    indent = '\t' * (len(bl) - len(bl.lstrip()))
                    ab_lines = [
                        f'{indent}\tallow_branch = {{',
                        f'{indent}\t\toriginal_tag = HOL',
                        f'{indent}\t}}',
                    ]
                    block = block[:k+1] + ab_lines + block[k+1:]
                    added += 1
                    break
        
        new_lines.extend(block)
        i = j + 1
    else:
        new_lines.append(line)
        i += 1

result = '\n'.join(new_lines)

# Write to our mod directory
out_path = os.path.join(
    r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56",
    "common", "national_focus", "indonesia_joint.txt"
)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(result)

print(f"Written {len(result)} chars to {out_path}")
print(f"Added allow_branch to {added} joint_focus blocks")
print(f"Total allow_branch in file: {result.count('allow_branch')}")
