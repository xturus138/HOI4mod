src = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\eventwindow.gui'
dst = 'interface/eventwindow.gui'

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

# Target exact blocks
block1 = '''			instantTextBoxType = {
				name = "Description"
				position = { x = 31 y = 0 }
				font = "hoi4_typewriter16"
				borderSize = {x = 0 y = 0}
				text = "Long text here!"	
				maxWidth = 512
				maxHeight = 230
				format = left
			}'''

repl1 = '''			instantTextBoxType = {
				name = "Description"
				position = { x = 31 y = 0 }
				font = "hoi4_typewriter16"
				borderSize = {x = 0 y = 0}
				text = "Long text here!"	
				maxWidth = 512
				maxHeight = 230
				format = left
				scrollbarType = standardtext_slider
			}'''

block2 = '''			instantTextBoxType = {
				name = "Description"
				position = { x = 39 y = 170 }
				font = "hoi4_typewriter16"
				borderSize = {x = 0 y = 0}
				text = "Long text here!"	
				maxWidth = 460
				maxHeight = 230
				format = left
			}'''

repl2 = '''			instantTextBoxType = {
				name = "Description"
				position = { x = 39 y = 170 }
				font = "hoi4_typewriter16"
				borderSize = {x = 0 y = 0}
				text = "Long text here!"	
				maxWidth = 460
				maxHeight = 230
				format = left
				scrollbarType = standardtext_slider
			}'''

assert block1 in content, "block1 not found in vanilla eventwindow.gui!"
assert block2 in content, "block2 not found in vanilla eventwindow.gui!"

content = content.replace(block1, repl1, 1)
content = content.replace(block2, repl2, 1)

with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully added scrollbarType to EventWindow and EventWindow_News in interface/eventwindow.gui!')
