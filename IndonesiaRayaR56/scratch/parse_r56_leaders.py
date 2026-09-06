import re

fpath = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\common\characters\INS.txt"
with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
    txt = f.read()

# find blocks
char_blocks = re.findall(r'(\bINS_[a-zA-Z0-9_]+)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', txt)
print(f"Parsed character blocks: {len(char_blocks)}")

leaders = []
for cid, block in char_blocks:
    if "country_leader" in block:
        # extract ideology
        m_ideo = re.search(r'ideology\s*=\s*([a-zA-Z0-9_]+)', block)
        ideo = m_ideo.group(1) if m_ideo else "unknown"
        # extract portrait
        m_port = re.search(r'civilian\s*=\s*\{\s*large\s*=\s*([a-zA-Z0-9_]+)', block)
        port = m_port.group(1) if m_port else "no_portrait"
        leaders.append((cid, ideo, port))

print(f"Total country leaders in R56 INS.txt: {len(leaders)}")
for cid, ideo, port in sorted(leaders, key=lambda x: x[1]):
    print(f"Ideology: {ideo:25} | ID: {cid:35} | Portrait: {port}")
