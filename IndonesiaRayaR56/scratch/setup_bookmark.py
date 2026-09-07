import os

r56_bm = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\common\bookmarks\the_gathering_storm.txt"
base = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
our_bm_dir = os.path.join(base, "common", "bookmarks")
os.makedirs(our_bm_dir, exist_ok=True)
our_bm = os.path.join(our_bm_dir, "the_gathering_storm.txt")

with open(r56_bm, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

old_focuses = """		focuses = {
			INSHOL_autonomous_dominion
			INS_the_declaration_of_independence
			INS_support_tan_malakas_coup
		}"""

new_focuses = """		focuses = {
			dei_focus_root
			dei_focus_pembangkangan
			dei_focus_momentum_kemerdekaan
		}"""

if old_focuses not in text:
    # try normalized whitespace
    import re
    text = re.sub(
        r'focuses\s*=\s*\{\s*INSHOL_autonomous_dominion\s*INS_the_declaration_of_independence\s*INS_support_tan_malakas_coup\s*\}',
        'focuses = {\n\t\t\tdei_focus_root\n\t\t\tdei_focus_pembangkangan\n\t\t\tdei_focus_momentum_kemerdekaan\n\t\t}',
        text
    )
    print("Regex replaced bookmark focuses")
else:
    text = text.replace(old_focuses, new_focuses, 1)
    print("Directly replaced bookmark focuses")

with open(our_bm, "w", encoding="utf-8") as f:
    f.write(text)

print("Saved our_bm successfully!")
