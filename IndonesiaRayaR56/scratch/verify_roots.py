with open('common/national_focus/DEI_indonesia_focus_tree.txt', 'r', encoding='utf-8') as f:
    text = f.read()

roots = [
    'dei_focus_momentum_kemerdekaan',
    'dei_focus_a_proklamasi',
    'dei_focus_b_root',
    'dei_focus_c_root',
    'dei_focus_d_root',
    'dei_focus_e_root',
    'dei_focus_f_root'
]

for r in roots:
    idx = text.find('id = ' + r)
    end_idx = text.find('id = ', idx + 10) if idx != -1 else -1
    print(f'=== {r} ===')
    chunk = text[idx:idx+700]
    for line in chunk.splitlines():
        if any(k in line for k in ['ruling_party', 'recruit_character', 'promote_character', 'set_cosmetic_tag', 'end_puppet']):
            print(' ', line.strip())
