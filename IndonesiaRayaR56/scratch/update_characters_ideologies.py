char_file = r'common/characters/DEI_characters.txt'
with open(char_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace federalist_generic and majapahit_generic
content = content.replace('ideology = federalist_generic', 'ideology = conservatism')
content = content.replace('ideology = majapahit_generic', 'ideology = despotism')

# Replace islamist leaders individually
# Kartosuwiryo -> despotism (Theocratic head of state under neutrality)
# Wahid Hasyim -> oligarchism (Ulama council leadership)
# Natsir -> conservatism (Islamic democracy)

content = content.replace('''	DEI_mohammad_natsir = {
		name = "Mohammad Natsir"
		portraits = {
			civilian = {
				large = "GFX_portrait_INS_natsir"
			}
		}
		country_leader = {
			ideology = islamist_generic''', '''	DEI_mohammad_natsir = {
		name = "Mohammad Natsir"
		portraits = {
			civilian = {
				large = "GFX_portrait_INS_natsir"
			}
		}
		country_leader = {
			ideology = conservatism''')

content = content.replace('''	DEI_wahid_hasyim = {
		name = "K.H. Wahid Hasyim"
		portraits = {
			civilian = {
				large = "GFX_portrait_INS_wahid_hasyim"
			}
		}
		country_leader = {
			ideology = islamist_generic''', '''	DEI_wahid_hasyim = {
		name = "K.H. Wahid Hasyim"
		portraits = {
			civilian = {
				large = "GFX_portrait_INS_wahid_hasyim"
			}
		}
		country_leader = {
			ideology = oligarchism''')

content = content.replace('''	DEI_kartosuwiryo = {
		name = "Sekarmadji Maridjan Kartosuwiryo"
		portraits = {
			civilian = {
				large = "GFX_portrait_INS_kartosuwiryo"
			}
		}
		country_leader = {
			ideology = islamist_generic''', '''	DEI_kartosuwiryo = {
		name = "Sekarmadji Maridjan Kartosuwiryo"
		portraits = {
			civilian = {
				large = "GFX_portrait_INS_kartosuwiryo"
			}
		}
		country_leader = {
			ideology = despotism''')

with open(char_file, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated DEI_characters.txt successfully!')
