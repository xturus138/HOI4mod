import glob, os, re

focus_files = sorted(glob.glob(r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\common\national_focus\*.txt'))
with open(r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml', 'r', encoding='utf-8-sig') as lf:
    loc_text = lf.read()

def get_loc(key):
    pattern = r' ' + key + r':\s*"([^"]+)"'
    m = re.search(pattern, loc_text)
    return m.group(1) if m else 'MISSING'

for f in focus_files:
    print('=== ' + os.path.basename(f) + ' ===')
    with open(f, 'r', encoding='utf-8') as fl:
        text = fl.read()
        focuses = re.findall(r'focus\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_]+)', text)
        for foc in focuses:
            print(f'  {foc} -> {get_loc(foc)}')
