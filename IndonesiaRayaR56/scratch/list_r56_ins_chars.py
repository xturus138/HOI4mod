import re

fpath = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\common\characters\INS.txt"
with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
    txt = f.read()

chars = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{\s*name\s*=\s*"([^"]+)"', txt)
print(f"Total characters in R56 INS.txt: {len(chars)}")
for cid, name in chars:
    # check if country leader
    block_start = txt.find(cid + " = {")
    is_leader = "country_leader" in txt[block_start:block_start+1000]
    print(f"{cid:32}: {name:25} (Leader: {is_leader})")
