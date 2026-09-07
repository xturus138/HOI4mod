with open('common/national_focus/DEI_indonesia_focus_tree.txt', 'r', encoding='utf-8') as f:
    text = f.read()

roots = [
    'dei_focus_c_root',
    'dei_focus_d_root',
    'dei_focus_e_root',
    'dei_focus_f_root'
]

for r in roots:
    idx = text.find('id = ' + r)
    end_idx = text.find('country_event', idx)
    print(f'=== {r} ===')
    print(text[idx:end_idx+60])
