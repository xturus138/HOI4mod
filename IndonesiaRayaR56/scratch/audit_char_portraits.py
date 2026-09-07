import glob, re

with open(r'common\characters\DEI_characters.txt', 'r', encoding='utf-8') as f:
    char_txt = f.read()

with open(r'interface\DEI_portraits.gfx', 'r', encoding='utf-8') as f:
    gfx_txt = f.read()

# Check all sprite names in DEI_characters.txt
used_sprites = re.findall(r'large\s*=\s*\"?([a-zA-Z0-9_]+)\"?', char_txt)
print(f'Total used sprites in characters: {len(used_sprites)}')

missing_sprites = []
for s in set(used_sprites):
    if f'name = "{s}"' not in gfx_txt and f'name = \"{s}\"' not in gfx_txt:
        missing_sprites.append(s)

print('Missing sprites in DEI_portraits.gfx:', missing_sprites)
