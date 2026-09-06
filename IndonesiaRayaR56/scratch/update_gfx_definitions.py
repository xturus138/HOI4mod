import os, glob

mod_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
goals_dir = os.path.join(mod_dir, "gfx", "interface", "goals")
tech_dir = os.path.join(mod_dir, "gfx", "interface", "technologies")

# 1. Update DEI_goals.gfx
goal_files = sorted([os.path.basename(f) for f in glob.glob(os.path.join(goals_dir, "*.dds"))])
goals_gfx_content = ["spriteTypes = {"]
for gf in goal_files:
    sprite_name = "GFX_" + gf[:-4]
    goals_gfx_content.append(f'\tspriteType = {{\n\t\tname = "{sprite_name}"\n\t\ttexturefile = "gfx/interface/goals/{gf}"\n\t}}')
goals_gfx_content.append("}\n")

with open(os.path.join(mod_dir, "interface", "DEI_goals.gfx"), "w", encoding="utf-8") as f:
    f.write("\n".join(goals_gfx_content))
print(f"Updated DEI_goals.gfx with {len(goal_files)} sprites.")

# 2. Update DEI_technologies.gfx
tech_sprites = [
    # Armored Cars
    ("GFX_INS_braat_overvalwagen_medium", "INS_braat_overvalwagen.dds"),
    ("GFX_INS_armored_car1_medium", "INS_braat_overvalwagen.dds"),
    ("GFX_INS_armored_car_equipment_1_medium", "INS_braat_overvalwagen.dds"),
    ("GFX_INS_marmon_herrington_ctls_medium", "INS_marmon_herrington_ctls.dds"),
    ("GFX_INS_armored_car2_medium", "INS_marmon_herrington_ctls.dds"),
    ("GFX_INS_armored_car_equipment_2_medium", "INS_marmon_herrington_ctls.dds"),

    # Infantry Weapons
    ("GFX_INS_infantry_weapons_medium", "INS_infantry_weapons.dds"),
    ("GFX_INS_infantry_equipment_0_medium", "INS_infantry_weapons.dds"),
    ("GFX_INS_infantry_weapons1_medium", "INS_infantry_weapons1.dds"),
    ("GFX_INS_infantry_equipment_1_medium", "INS_infantry_weapons1.dds"),
    ("GFX_INS_improved_infantry_weapons_medium", "INS_improved_infantry_weapons.dds"),
    ("GFX_INS_infantry_equipment_2_medium", "INS_improved_infantry_weapons.dds"),
    ("GFX_INS_advanced_infantry_weapons_medium", "INS_advanced_infantry_weapons.dds"),
    ("GFX_INS_infantry_equipment_3_medium", "INS_advanced_infantry_weapons.dds"),

    # Support & Motorized
    ("GFX_INS_tech_support_medium", "INS_tech_support.dds"),
    ("GFX_INS_support_equipment_1_medium", "INS_tech_support.dds"),
    ("GFX_INS_motorised_infantry_medium", "INS_motorised_infantry.dds"),
    ("GFX_INS_motorized_equipment_1_medium", "INS_motorised_infantry.dds"),

    # Artillery & AA/AT
    ("GFX_INS_gw_artillery_medium", "INS_gw_artillery.dds"),
    ("GFX_INS_artillery1_medium", "INS_artillery1.dds"),
    ("GFX_INS_artillery_equipment_1_medium", "INS_artillery1.dds"),
    ("GFX_INS_interwar_antiair_medium", "INS_interwar_antiair.dds"),
    ("GFX_INS_anti_air_equipment_1_medium", "INS_interwar_antiair.dds"),
    ("GFX_INS_interwar_antitank_medium", "INS_interwar_antitank.dds"),
    ("GFX_INS_anti_tank_equipment_1_medium", "INS_interwar_antitank.dds"),

    # Tanks
    ("GFX_INS_gwtank_medium", "INS_gwtank.dds"),
    ("GFX_INS_gwtank_chassis_medium", "INS_gwtank.dds"),
    ("GFX_INS_basic_light_tank_medium", "INS_basic_light_tank.dds"),
    ("GFX_INS_basic_light_tank_chassis_medium", "INS_basic_light_tank.dds"),
    ("GFX_INS_improved_light_tank_medium", "INS_improved_light_tank.dds"),
    ("GFX_INS_improved_light_tank_chassis_medium", "INS_improved_light_tank.dds"),

    # Aircraft
    ("GFX_INS_cw21_demon_medium", "INS_cw21_demon.dds"),
    ("GFX_INS_early_fighter_medium", "INS_cw21_demon.dds"),
    ("GFX_INS_fighter1_medium", "INS_fighter1.dds"),
    ("GFX_INS_fighter_equipment_1_medium", "INS_fighter1.dds"),
    ("GFX_INS_cv_fighter_equipment_1_medium", "INS_fighter1.dds"),
    ("GFX_INS_fighter2_medium", "INS_fighter2.dds"),
    ("GFX_INS_fighter_equipment_2_medium", "INS_fighter2.dds"),
    ("GFX_INS_cv_fighter_equipment_2_medium", "INS_fighter2.dds"),
    ("GFX_INS_early_bomber_medium", "INS_early_bomber.dds"),
    ("GFX_INS_b25_mitchell_medium", "INS_b25_mitchell.dds"),
    ("GFX_INS_tactical_bomber1_medium", "INS_b25_mitchell.dds"),
    ("GFX_INS_tactical_bomber_equipment_1_medium", "INS_b25_mitchell.dds"),
    ("GFX_INS_transport_plane_medium", "INS_transport_plane.dds"),
    ("GFX_INS_transport_plane1_medium", "INS_transport_plane.dds"),
    ("GFX_INS_transport_plane_equipment_medium", "INS_transport_plane.dds"),

    # Naval
    ("GFX_INS_early_destroyer_medium", "INS_early_destroyer.dds"),
    ("GFX_INS_basic_destroyer_medium", "INS_early_destroyer.dds"),
    ("GFX_INS_ship_hull_light_1_medium", "INS_early_destroyer.dds"),
    ("GFX_INS_early_submarine_medium", "INS_early_submarine.dds"),
    ("GFX_INS_basic_submarine_medium", "INS_early_submarine.dds"),
    ("GFX_INS_ship_hull_submarine_1_medium", "INS_early_submarine.dds"),
    ("GFX_INS_early_light_cruiser_medium", "INS_early_light_cruiser.dds"),
    ("GFX_INS_basic_cruiser_medium", "INS_early_light_cruiser.dds"),
    ("GFX_INS_ship_hull_cruiser_1_medium", "INS_early_light_cruiser.dds")
]

tech_gfx_content = ["spriteTypes = {"]
for name, tex in tech_sprites:
    tech_gfx_content.append(f'\tspriteType = {{\n\t\tname = "{name}"\n\t\ttexturefile = "gfx/interface/technologies/{tex}"\n\t}}')
tech_gfx_content.append("}\n")

with open(os.path.join(mod_dir, "interface", "DEI_technologies.gfx"), "w", encoding="utf-8") as f:
    f.write("\n".join(tech_gfx_content))
print(f"Updated DEI_technologies.gfx with {len(tech_sprites)} sprites.")
