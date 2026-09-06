agents_file = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\AGENTS.md'

with open(agents_file, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('v1.4.1 (Dynamic Ideological Naming & Multi-Option Customization)', 'v1.4.2 (Authentic Historical Naming & No Fake Acronyms)')
text = text.replace('KPR (Komunis), KRI (Otoriter), KNI (Islamis), JPS/KMN (Majapahit)', 'KRI (Otoriter); nama murni tanpa akronim artifisial untuk Komunis, Islamis, dan Majapahit')

with open(agents_file, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated AGENTS.md to v1.4.2')
