with open('common/national_focus/DEI_indonesia_focus_tree.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see how end_puppet is used in focus tree
import re
matches = [m.start() for m in re.finditer(r'end_puppet\s*=\s*yes', text)]
print(f'Found {len(matches)} occurrences in DEI_indonesia_focus_tree.txt:')
for idx in matches:
    # find parent focus id
    f_idx = text.rfind('id = ', 0, idx)
    f_end = text.find('\n', f_idx)
    print(text[f_idx:f_end])
