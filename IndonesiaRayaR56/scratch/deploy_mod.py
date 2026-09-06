import os, shutil

src_mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
paradox_mod_root = r"C:\Users\radit\Documents\Paradox Interactive\Hearts of Iron IV\mod"
dest_mod_dir = os.path.join(paradox_mod_root, "IndonesiaRayaR56")
dest_mod_file = os.path.join(paradox_mod_root, "IndonesiaRayaR56.mod")

print(f"Source: {src_mod_dir}")
print(f"Destination mod folder: {dest_mod_dir}")
print(f"Destination .mod file: {dest_mod_file}")

os.makedirs(paradox_mod_root, exist_ok=True)
os.makedirs(dest_mod_dir, exist_ok=True)

# Subfolders to copy
copy_dirs = ["common", "events", "gfx", "history", "interface", "localisation"]
copy_files = ["descriptor.mod", "thumbnail.png"]

for cd in copy_dirs:
    s_path = os.path.join(src_mod_dir, cd)
    d_path = os.path.join(dest_mod_dir, cd)
    if os.path.exists(d_path):
        print(f"Removing old {d_path}...")
        shutil.rmtree(d_path)
    print(f"Copying {cd} -> {d_path}...")
    shutil.copytree(s_path, d_path)

for cf in copy_files:
    s_path = os.path.join(src_mod_dir, cf)
    d_path = os.path.join(dest_mod_dir, cf)
    if os.path.exists(s_path):
        print(f"Copying {cf} -> {d_path}...")
        shutil.copy2(s_path, d_path)

# Create IndonesiaRayaR56.mod in Paradox mod directory
mod_content = """version="1.0.0"
tags={
	"Alternate History"
	"National Focus"
	"Events"
}
name="Indonesia Raya: Road to Merdeka (R56 Submod)"
supported_version="*"
path="mod/IndonesiaRayaR56"
picture="thumbnail.png"
dependencies={
	"The Road to 56"
}
"""

with open(dest_mod_file, "w", encoding="utf-8") as f:
    f.write(mod_content)
print(f"Created {dest_mod_file}")

# Verify deployed files
print("\n=== VERIFYING DEPLOYMENT ===")
print("Descriptor mod file exists:", os.path.exists(dest_mod_file))
print("Deployed folder exists:", os.path.exists(dest_mod_dir))

deployed_goals = len(os.listdir(os.path.join(dest_mod_dir, "gfx", "interface", "goals")))
deployed_tech = len(os.listdir(os.path.join(dest_mod_dir, "gfx", "interface", "technologies")))
deployed_events = len(os.listdir(os.path.join(dest_mod_dir, "events")))
deployed_focuses = len(os.listdir(os.path.join(dest_mod_dir, "common", "national_focus")))

print(f"Deployed Goals: {deployed_goals} files")
print(f"Deployed Technologies: {deployed_tech} files")
print(f"Deployed Events: {deployed_events} files")
print(f"Deployed Focus Files: {deployed_focuses} files")
print("\nDEPLOYMENT COMPLETED 100% SUCCESSFULLY!")
