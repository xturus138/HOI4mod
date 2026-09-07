with open('common/decisions/DEI_decisions.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('dei_decisions_nusantara = {')
print(text[idx:idx+1200])
