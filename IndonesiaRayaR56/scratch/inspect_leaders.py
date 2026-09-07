with open(r'common\characters\DEI_characters.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
chars = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', text)
print('Total characters:', len(chars))
for cid, cbody in chars:
    if 'country_leader' in cbody:
        name_m = re.search(r'name\s*=\s*\"([^\"]+)\"', cbody)
        name = name_m.group(1) if name_m else cid
        ideology_m = re.search(r'ideology\s*=\s*([a-zA-Z0-9_]+)', cbody)
        ideology = ideology_m.group(1) if ideology_m else 'unknown'
        port_m = re.search(r'large\s*=\s*\"([^\"]+)\"', cbody)
        port = port_m.group(1) if port_m else 'none'
        print(f'{cid}: name="{name}", ideology={ideology}, portrait={port}')
