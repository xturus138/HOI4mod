import os, re

base = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
ft_path = os.path.join(base, "common", "national_focus", "DEI_indonesia_focus_tree.txt")
gfx_path = os.path.join(base, "interface", "DEI_goals.gfx")

with open(ft_path, "r", encoding="utf-8") as f:
    ft = f.read()
with open(gfx_path, "r", encoding="utf-8") as f:
    gt = f.read()

icons = set(re.findall(r"icon\s*=\s*([a-zA-Z0-9_]+)", ft))
missing_shine = []
missing_def = []

for ic in sorted(icons):
    if f'name = "{ic}"' not in gt:
        if "dei" in ic.lower():
            missing_def.append(ic)
    if f'name = "{ic}_shine"' not in gt:
        if "dei" in ic.lower() or "ins" in ic.lower():
            missing_shine.append(ic)

print("Icons in tree:", len(icons))
print("Missing regular DEI sprite definitions:", len(missing_def), missing_def)
print("Missing shine sprite definitions:", len(missing_shine), missing_shine)
