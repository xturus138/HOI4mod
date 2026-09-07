import glob, re

with open(r'interface\DEI_portraits.gfx', 'r', encoding='utf-8') as f:
    txt = f.read()

sprites = re.findall(r'name\s*=\s*\"([^\"]+)\"\s*texturefile\s*=\s*\"([^\"]+)\"', txt)
print('Total portrait sprites in DEI_portraits.gfx:', len(sprites))
for s, t in sprites:
    print(f'{s} -> {t}')
