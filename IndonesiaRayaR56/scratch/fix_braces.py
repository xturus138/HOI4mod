import re

with open(r'common\national_focus\DEI_indonesia_focus_tree.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the triple closing braces in each path root
for p in ['a', 'b', 'c', 'd', 'e', 'f']:
    old_end = f'''country_event = {{ id = dei_path_{p}.1 hours = 6 }}
	}}
		}}
	}}'''
    new_end = f'''country_event = {{ id = dei_path_{p}.1 hours = 6 }}
	}}
	}}'''
    if old_end in text:
        text = text.replace(old_end, new_end)
        print(f'Replaced old_end for path {p}')
    else:
        print(f'old_end NOT found for path {p}')

with open(r'common\national_focus\DEI_indonesia_focus_tree.txt', 'w', encoding='utf-8') as f:
    f.write(text)

open_b = text.count('{')
close_b = text.count('}')
print(f'New brace balance: open={open_b}, close={close_b}, diff={open_b - close_b}')
