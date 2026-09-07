import re

# Our tree
p1 = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_indonesia_focus_tree.txt"
with open(p1, "r", encoding="utf-8") as f:
    t1 = f.read()

# Show first 30 lines
lines = t1.splitlines()
for i, l in enumerate(lines[:25]):
    print(f"  OUR L{i+1}: {l}")

print("\n---")

# R56 trees
for fn in ["indonesia.txt", "r56_indonesia.txt"]:
    fp = rf"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\common\national_focus\{fn}"
    with open(fp, "r", encoding="utf-8", errors="ignore") as f:
        t = f.read()
    lines = t.splitlines()
    print(f"\nR56 {fn} (first 25 lines):")
    for i, l in enumerate(lines[:25]):
        print(f"  L{i+1}: {l}")
