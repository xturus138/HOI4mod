path = 'interface/eventwindow.gui'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update options_grid in EventWindow_News
old_news_grid = '''			gridBoxType = {
				name = "options_grid"
				position = { x = 80 y = -1 }
				size = { width = 300 height = 30 }
				slotsize = { width = 300 height = 47 }
				max_slots_horizontal = 1
				format = "UPPER_LEFT"
			}'''

new_news_grid = '''			gridBoxType = {
				name = "options_grid"
				position = { x = 88 y = -55 }
				size = { width = 352 height = 30 }
				slotsize = { width = 352 height = 42 }
				max_slots_horizontal = 1
				format = "UPPER_LEFT"
			}'''

# 2. Update event_option_entry
old_entry = '''	containerWindowType = {
		name = "event_option_entry"
		size = { width = 300 height = 47 }
		clipping = no
		
		background = {
			name = "event_option_background"	
			spriteType ="GFX_event_option_entry"
		}
		
		instantTextBoxType = {
			name = "Name"
			position = { x = 5 y = 0 }
			font = "hoi_20bs"
			maxWidth = 340
			maxHeight = 40
			format = center
			vertical_alignment = center
			alwaystransparent = yes
		}
	}'''

new_entry = '''	containerWindowType = {
		name = "event_option_entry"
		size = { width = 352 height = 42 }
		clipping = no
		
		background = {
			name = "event_option_background"	
			spriteType ="GFX_event_option_entry"
		}
		
		instantTextBoxType = {
			name = "Name"
			position = { x = 5 y = 1 }
			font = "hoi_20bs"
			maxWidth = 342
			maxHeight = 40
			format = center
			vertical_alignment = center
			alwaystransparent = yes
		}
	}'''

# 3. Update options_grid in EventWindow
old_event_grid = '''			gridBoxType = {
				name = "options_grid"
				position = { x = 140 y = 10 }
				size = { width = 300 height = 30 }
				slotsize = { width = 300 height = 47 }
				max_slots_horizontal = 1
				format = "UPPER_LEFT"
			}'''

new_event_grid = '''			gridBoxType = {
				name = "options_grid"
				position = { x = 114 y = 10 }
				size = { width = 352 height = 30 }
				slotsize = { width = 352 height = 42 }
				max_slots_horizontal = 1
				format = "UPPER_LEFT"
			}'''

assert old_news_grid in text, "old_news_grid not found!"
assert old_entry in text, "old_entry not found!"
assert old_event_grid in text, "old_event_grid not found!"

text = text.replace(old_news_grid, new_news_grid, 1)
text = text.replace(old_entry, new_entry, 1)
text = text.replace(old_event_grid, new_event_grid, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated interface/eventwindow.gui: EventWindow_News buttons shifted up by 54px and centered, slotsize 352x42!')
