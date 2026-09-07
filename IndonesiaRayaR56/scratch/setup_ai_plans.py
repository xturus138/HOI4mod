import os

base = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56"
ai_dir = os.path.join(base, "common", "ai_strategy_plans")
os.makedirs(ai_dir, exist_ok=True)

historical_plan = """#####-----> INS: Indonesia Raya Historical AI Plan <><> <><> <><> <><> <><>

INS_historical_plan_r56 = {
	name = "INS: Indonesia Raya Historical AI Plan"
	desc = "Historical behavior for Indonesia under Indonesia Raya submod."

	allowed = {
		original_tag = INS
	}

	enable = {
		always = yes
	}

	abort = {
		always = no
	}

	ai_national_focuses = {
		dei_focus_root
		dei_focus_pembangkangan
		dei_focus_momentum_kemerdekaan
		dei_focus_liberate_sumatra
		dei_focus_liberate_borneo
		dei_focus_liberate_timur_raya
		dei_focus_liberate_papua
		dei_focus_traktat_kedaulatan
		dei_focus_a_proklamasi
		dei_focus_a_tkr
		dei_focus_a_diplomasi
		dei_focus_a_linggarjati
		dei_focus_a_renville
		dei_focus_a_kmb
		dei_focus_a_kaa_bandung
		dei_focus_a_pancasila
		dei_focus_a_trisakti
	}
}
"""

vanilla_historical = """#####-----> INS: Indonesia Raya Vanilla Historical Plan <><> <><> <><> <><> <><>

INS_historical_strategy_plan = {
	name = "INS: Indonesia Raya Plan"
	desc = "Overrides vanilla strategy plan."

	allowed = {
		original_tag = INS
	}

	enable = {
		always = yes
	}

	abort = {
		always = no
	}

	ai_national_focuses = {
		dei_focus_root
		dei_focus_pembangkangan
		dei_focus_momentum_kemerdekaan
		dei_focus_liberate_sumatra
		dei_focus_liberate_borneo
		dei_focus_liberate_timur_raya
		dei_focus_liberate_papua
		dei_focus_traktat_kedaulatan
	}
}
"""

alternate_stub = """# Overridden by Indonesia Raya (R56 Submod)
"""

for fname, content in [
    ("INS_r56_historical_strategy_plan.txt", historical_plan),
    ("INS_r56_alternate_strategy_plan.txt", alternate_stub),
    ("INS_historical_strategy_plan.txt", vanilla_historical),
    ("INS_alternate_strategy_plan.txt", alternate_stub)
]:
    p = os.path.join(ai_dir, fname)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {fname}")
