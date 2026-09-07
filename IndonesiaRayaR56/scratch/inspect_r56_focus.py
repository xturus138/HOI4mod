import os
import glob
import re

r56_dir = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968"
print("Scanning R56 for INS national focus files...")

r56_focus_files = glob.glob(os.path.join(r56_dir, "common", "national_focus", "*.txt"))
for ff in r56_focus_files:
    with open(ff, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    if "tag = INS" in content or "tag = DEI" in content:
        print(f"Found match in R56: {os.path.basename(ff)}")
        # Check focus tree id and factor
        m = re.search(r'focus_tree\s*=\s*\{[^}]*id\s*=\s*([a-zA-Z0-9_]+)', content)
        if m:
            print(f"  Tree ID: {m.group(1)}")
        m_mod = re.search(r'modifier\s*=\s*\{[^}]*add\s*=\s*(\d+)[^}]*tag\s*=\s*(INS|DEI)', content)
        if m_mod:
            print(f"  Priority modifier: add = {m_mod.group(1)} for tag = {m_mod.group(2)}")
