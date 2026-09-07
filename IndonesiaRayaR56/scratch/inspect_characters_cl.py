with open('common/characters/DEI_characters.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
cur_char = None
cur_name = None
in_cl = False
for line in lines:
    s = line.strip()
    if s.startswith('DEI_') and '=' in s and '{' in s:
        cur_char = s.split('=')[0].strip()
    if 'name =' in s and cur_char:
        cur_name = s.split('=')[1].strip().strip('\"')
    if 'country_leader =' in s:
        in_cl = True
    if in_cl and 'ideology =' in s:
        ideo = s.split('=')[1].strip()
        print(f"{cur_char:25} | {cur_name:30} | {ideo}")
        in_cl = False
