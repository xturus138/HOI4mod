import os
import re

gui_path = r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\interface\eventwindow.gui"
with open(gui_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Find containerWindowType blocks
matches = re.finditer(r'containerWindowType\s*=\s*\{', text)
for m in matches:
    start = m.start()
    # grab next 2000 chars
    chunk = text[start:start+2500]
    name_m = re.search(r'name\s*=\s*"([^"]+)"', chunk)
    name = name_m.group(1) if name_m else "UNKNOWN"
    if "event" in name.lower() or "EventWindow" in name or "country" in name.lower():
        print(f"=== WINDOW: {name} ===")
        # find picture or icon
        pic_m = re.search(r'iconType\s*=\s*\{[^}]*name\s*=\s*"Event_Picture"[^}]*\}', chunk, re.DOTALL)
        if not pic_m:
            pic_m = re.search(r'iconType\s*=\s*\{[^}]*name\s*=\s*"[eE]vent_[pP]icture"[^}]*\}', chunk, re.DOTALL)
        if not pic_m:
            pic_m = re.search(r'name\s*=\s*"[eE]vent_[pP]icture"[^}]*', chunk)
        if pic_m:
            print("PICTURE ELEMENT:")
            print(pic_m.group(0)[:400])
        
        # find options_grid
        opt_m = re.search(r'gridBoxType\s*=\s*\{[^}]*name\s*=\s*"[eE]vent_options"[^}]*\}', chunk, re.DOTALL)
        if not opt_m:
            opt_m = re.search(r'name\s*=\s*"options_grid"[^}]*', chunk)
        if opt_m:
            print("OPTIONS GRID:")
            print(opt_m.group(0)[:400])
        print()
