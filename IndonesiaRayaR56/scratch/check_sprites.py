import os, re

with open('interface/DEI_event_pictures.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

sprites = re.findall(r'name\s*=\s*"(GFX_dei_news_event_[^"]+)"', text)
print('News event sprites in DEI_event_pictures.gfx:', len(sprites))
for s in sprites:
    print(' ', s)

# Also check texture files
textures = re.findall(r'texturefile\s*=\s*"([^"]+)"', text)
for t in textures:
    if 'news' in t:
        p = t.replace('/', os.sep)
        exists = os.path.exists(p)
        print(' Texture:', p, 'Exists:', exists)
