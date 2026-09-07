path = 'interface/eventwindow.gui'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

old_block = '''			gridBoxType = {
				name = "options_grid"
				position = { x = 88 y = -55 }
				size = { width = 352 height = 30 }
				slotsize = { width = 352 height = 42 }
				max_slots_horizontal = 1
				format = "UPPER_LEFT"
			}'''

new_block = '''			gridBoxType = {
				name = "options_grid"
				position = { x = 88 y = 10 }
				size = { width = 352 height = 30 }
				slotsize = { width = 352 height = 42 }
				max_slots_horizontal = 1
				format = "UPPER_LEFT"
			}'''

assert old_block in text, "old_block not found in interface/eventwindow.gui!"
text = text.replace(old_block, new_block, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated interface/eventwindow.gui: options_grid now at y = 10 (never overlaps text)!')
