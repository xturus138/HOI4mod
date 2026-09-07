import re

c = open(r'localisation/english/DEI_indonesia_l_english.yml', 'r', encoding='utf-8').read()
event_titles = re.findall(r'(dei_[a-z0-9_]+\.t):\s*"([^"]+)"', c)
print(f"Total event titles found: {len(event_titles)}")
for k, v in event_titles[:35]:
    print(f"{k:25}: {v}")
