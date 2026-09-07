with open(r'C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\history\countries\INS - Indonesia.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('add_ideas = {')
print(text[idx:idx+400])
