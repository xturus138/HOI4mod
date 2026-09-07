import re

p = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\indonesia_joint.txt"
with open(p, "r", encoding="utf-8") as f:
    txt = f.read()

# Count joint_focus blocks using brace counting
lines = txt.splitlines()
blocks = []
i = 0
while i < len(lines):
    line = lines[i]
    if re.match(r'\s*joint_focus\s*=\s*\{', line):
        depth = 1
        start = i
        j = i + 1
        while j < len(lines):
            depth += lines[j].count("{") - lines[j].count("}")
            if depth <= 0:
                break
            j += 1
        block = lines[start:j+1]
        blocks.append(block)
        i = j + 1
    else:
        i += 1

print(f"Total joint_focus blocks: {len(blocks)}")
no_ab = []
for b in blocks:
    bt = '\n'.join(b)
    if 'allow_branch' not in bt:
        m = re.search(r'\bid\s*=\s*([a-zA-Z0-9_]+)', bt)
        no_ab.append(m.group(1) if m else "unknown")

print(f"With allow_branch: {len(blocks) - len(no_ab)}")
print(f"Without allow_branch: {len(no_ab)}")
for fid in no_ab:
    print(f"  Missing: {fid}")
