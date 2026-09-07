with open('common/characters/DEI_characters.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
chars = re.findall(r'([A-Za-z0-9_]+)\s*=\s*\{[^}]*name\s*=\s*([^\n]+)', text)
print(f'Total characters: {len(chars)}')

# Check country leader roles
leaders = re.findall(r'([A-Za-z0-9_]+)\s*=\s*\{.*?country_leader\s*=\s*\{.*?ideology\s*=\s*([a-zA-Z0-9_]+)', text, re.DOTALL)
print(f'Total country_leader definitions: {len(leaders)}')
for l_id, ideo in leaders:
    print(f'  {l_id} -> {ideo}')
