import os, re

fpath = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\DEI_r56_armed_forces.txt"
with open(fpath, "r", encoding="utf-8") as f:
    c = f.read()

chars = re.findall(r'character\s*=\s*([a-zA-Z0-9_]+)', c)
print("Characters referenced in DEI_r56_armed_forces.txt:")
for ch in set(chars):
    print(" -", ch)
