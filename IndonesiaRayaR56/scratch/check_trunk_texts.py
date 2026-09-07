with open('localisation/english/DEI_indonesia_l_english.yml', 'r', encoding='utf-8') as f:
    text = f.read()

for i in range(1, 7):
    k = f'dei_trunk.{i}.d:'
    idx = text.find(k)
    if idx != -1:
        end = text.find('\n', idx)
        print(f'=== {k} ===')
        print(text[idx:end])
