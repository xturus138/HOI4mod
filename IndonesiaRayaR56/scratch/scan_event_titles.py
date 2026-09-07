import re

with open(r'localisation/english/DEI_indonesia_l_english.yml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

event_titles = []
for i, line in enumerate(lines):
    # Match pattern: dei_something.t: "..."
    m = re.match(r'\s*([a-zA-Z0-9_]+\.[0-9]+\.t):\s*"([^"]+)"', line)
    if m:
        event_titles.append((i+1, m.group(1), m.group(2)))

print(f"Total event titles: {len(event_titles)}")
for ln, k, t in event_titles:
    print(f"L{ln:4} | {k:20} | {t}")
