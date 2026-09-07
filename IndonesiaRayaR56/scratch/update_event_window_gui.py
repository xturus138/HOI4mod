path = 'interface/eventwindow.gui'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's locate EventWindow midsection and bottom_Window
import re

old_mid_and_bottom = '''		containerWindowType = {
			name = "midsection"
			position = { x=0 y=121 }	
			size = { width = 580 height = 100 }
			moveable = yes
			clipping = no
			Orientation = UPPER_LEFT

			background = {
				name = "Background"	
				quadTextureSprite ="GFX_event_report_tileable_midsection"
			}

			instantTextBoxType = {
				name = "Description"
				position = { x = 31 y = 0 }
				font = "hoi4_typewriter16"
				borderSize = {x = 0 y = 0}
				text = "Long text here!"	
				maxWidth = 512
				maxHeight = 230
				format = left
				scrollbarType = standardtext_slider
			}	
		}			

		containerWindowType = {
			name = "bottom_Window"
			position = { x=0 y=221 }	
			size = { width = 581 height = 206 }
			moveable = yes
			clipping = no
			Orientation = UPPER_LEFT

#			background = {
#				name = "Background"	
#				spriteType ="GFX_event_report_tileable_bottom_section"
#			}

			background = {
				name = "Background"	
				spriteType ="GFX_event_report_bottom_win"
			}

			iconType = {
				name ="event_picture"
				spriteType = "GFX_report_event_001"
				position = { x = 5 y = 5 }
				Orientation = "UPPER_LEFT"
				alwaystransparent = yes				
			}

			iconType = {
				name ="event_pic_clip"
				spriteType = "GFX_event_pic_clip"
				position = { x = -3 y = 35 }
				Orientation = "UPPER_LEFT"
			}


			gridBoxType = {
				name = "options_grid"
				position = { x = 215 y = -1 }
				size = { width = 300 height = 30 }
				slotsize = { width = 300 height = 47 }
				max_slots_horizontal = 1
				format = "UPPER_LEFT"
			}
		}'''

new_mid_and_bottom = '''		containerWindowType = {
			name = "midsection"
			position = { x=0 y=121 }	
			size = { width = 580 height = 100 }
			moveable = yes
			clipping = no
			Orientation = UPPER_LEFT

			background = {
				name = "Background"	
				quadTextureSprite ="GFX_event_report_tileable_midsection"
			}

			iconType = {
				name ="event_picture"
				spriteType = "GFX_report_event_001"
				position = { x = 185 y = 5 }
				Orientation = "UPPER_LEFT"
				alwaystransparent = yes				
			}

			instantTextBoxType = {
				name = "Description"
				position = { x = 31 y = 190 }
				font = "hoi4_typewriter16"
				borderSize = {x = 0 y = 0}
				text = "Long text here!"	
				maxWidth = 512
				maxHeight = 230
				format = left
				scrollbarType = standardtext_slider
			}	
		}			

		containerWindowType = {
			name = "bottom_Window"
			position = { x=0 y=221 }	
			size = { width = 581 height = 206 }
			moveable = yes
			clipping = no
			Orientation = UPPER_LEFT

			background = {
				name = "Background"	
				spriteType ="GFX_event_report_bottom_win"
			}

			iconType = {
				name ="event_pic_clip"
				spriteType = "GFX_event_pic_clip"
				position = { x = -2000 y = -2000 }
				Orientation = "UPPER_LEFT"
			}

			gridBoxType = {
				name = "options_grid"
				position = { x = 140 y = 10 }
				size = { width = 300 height = 30 }
				slotsize = { width = 300 height = 47 }
				max_slots_horizontal = 1
				format = "UPPER_LEFT"
			}
		}'''

assert old_mid_and_bottom in text, "old_mid_and_bottom block not matched!"
text = text.replace(old_mid_and_bottom, new_mid_and_bottom, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated interface/eventwindow.gui: photo is now centered at top (x=185, y=5), description below it (y=190), buttons centered (x=140), paperclip removed!')
