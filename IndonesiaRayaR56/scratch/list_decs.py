import re

with open(r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\decisions\DEI_decisions.txt", "r", encoding="utf-8") as f:
    c = f.read()

categories = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{(?=\s*#[^\n]*\n|\s*dei_decision)', c)
print("Decisions by category:")
for cat in re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{([^}]+(?:\{[^}]+\}[^}]*)*)\}', c[c.find('decisions = {'):]):
    cat_name = cat.group(1)
    if cat_name != 'decisions':
        decs = re.findall(r'(dei_decision_[a-zA-Z0-9_]+)\s*=\s*\{', cat.group(2))
        print(f"[{cat_name}] ({len(decs)}): {decs}")
