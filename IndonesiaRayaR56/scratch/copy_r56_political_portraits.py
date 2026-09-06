import os, shutil

r56_leaders = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\gfx\leaders\INS"
mod_leaders = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\gfx\leaders\INS"

os.makedirs(mod_leaders, exist_ok=True)

targets = [
    "r56_portrait_INS_Sukarno.dds",
    "r56_portrait_INS_Mohammad_Hatta.dds",
    "r56_portrait_INS_Sutan_Syahrir.dds",
    "r56_portrait_INS_Hubertus_van_Mook.dds",
    "r56_portrait_INS_Tjarda_van_Starkenborgh.dds",
    "r56_portrait_INS_Musso_Munawar.dds",
    "r56_portrait_INS_Tan_Malaka.dds",
    "r56_portrait_INS_Amir_Sjarifuddin_Harahap.dds",
    "r56_portrait_INS_Alimin.dds",
    "r56_portrait_INS_Dipa_Nusantara.dds",
    "r56_portrait_INS_Sudirman.dds",
    "r56_portrait_INS_Abdul_Haris_Nasution.dds",
    "r56_portrait_INS_sekarmadji_kartosuwirjo.dds",
    "r56_portrait_INS_Mohammad_Natsir.dds",
    "r56_portrait_INS_Agus_Salim.dds",
    "r56_portrait_INS_Wuryaningrat.dds",
    "r56_portrait_INS_Sukawati.dds",
    "r56_portrait_INS_Panji_Suroso.dds",
    "r56_portrait_INS_Supomo.dds",
    "r56_portrait_INS_Sutomo.dds",
    "r56_portrait_INS_Abikusno_Cokrosuyoso.dds"
]

copied = []
for t in targets:
    src = os.path.join(r56_leaders, t)
    dst = os.path.join(mod_leaders, t)
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        copied.append(t)

print(f"Copied {len(copied)} R56 leader portraits into submod.")
