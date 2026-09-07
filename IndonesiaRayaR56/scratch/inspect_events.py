with open(r'localisation\english\DEI_indonesia_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

import re
from collections import Counter
keys = []
for l in lines:
    m = re.match(r'^\s*([a-zA-Z0-9_\.]+):', l)
    if m:
        keys.append(m.group(1))

counts = Counter(keys)
dups = {k: c for k, c in counts.items() if c > 1}
print('Duplicate keys found:', len(dups), dups)
