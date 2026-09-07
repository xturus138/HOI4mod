with open('common/characters/DEI_characters.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Split by top-level characters
blocks = re.findall(r'(\t[A-Za-z0-9_]+)\s*=\s*\{(.*?)(?=\n\t[A-Za-z0-9_]+\s*=\s*\{|\n\})', text, re.DOTALL)
print(f'Parsed blocks: {len(blocks)}')
for name, body in blocks:
    clean_name = name.strip()
    if 'country_leader' in body:
        ideo = re.search(r'ideology\s*=\s*([a-zA-Z0-9_]+)', body)
        ideo_str = ideo.group(1) if ideo else 'None'
        portrait = re.search(r'civilian\s*=\s*\{[^}]*large\s*=\s*"?([a-zA-Z0-9_]+)"?', body)
        p_str = portrait.group(1) if portrait else 'None'
        print(f'{clean_name:30} Ideology: {ideo_str:20} Portrait: {p_str}')
