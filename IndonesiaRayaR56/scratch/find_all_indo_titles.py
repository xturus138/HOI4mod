import os
import re

loc_path = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\localisation\english\DEI_indonesia_l_english.yml"
lines = open(loc_path, "r", encoding="utf-8-sig").readlines()

# Common Indonesian words that shouldn't be in English titles (unless proper names)
indo_indicators = [
    "kerjasama", "riset", "teknologi", "kodifikasi", "hukum", "pembentukan", 
    "resimen", "armada", "penobatan", "pendirian", "pusat", "tertinggi", 
    "sistem", "keuangan", "tanpa", "pemberantasan", "pembangkangan", 
    "penguatan", "pengembangan", "pembangunan", "perluasan", "pembersihan", 
    "penataan", "restorasi", "kebangkitan", "pemulihan", "angkatan", "kelima",
    "dan", "di", "ke", "dari", "untuk", "pada", "dengan", "secara", "kedaulatan",
    "gerilya", "benteng", "samudra", "laut", "udara", "darat", "rakyat", "buruh",
    "tani", "komune", "sita", "aset", "asing", "pakta", "semesta", "dewan",
    "darurat", "militer", "bubarkan", "partai", "dwifungsi", "karyawan", "wajib",
    "selat", "malaka", "hegemoni", "selatan", "mahkamah", "syariah", "akademi",
    "mujahidin", "anti", "riba", "liga", "muslim", "khilafah", "sumpah", "palapa",
    "baru", "kutaramanawa", "maharaja", "jung", "raksasa"
]

# Proper historical terms we intentionally preserve:
# "Baitul Mal", "Dharmaputra", "Syariah", "Kutaramanawa", "Pancasila", "Majapahit", "KNIL", "TKR", "TII", "LEKRA", "BFO", "ORI", "Sumpah Palapa", "KMB"

found_titles = []
for idx, line in enumerate(lines):
    # Match focus names (no _desc, no _tt), event titles (.t), decision names
    m = re.match(r'^\s*([a-zA-Z0-9_\.]+):\d*\s*"(.*)"', line)
    if m:
        key, val = m.group(1), m.group(2)
        # Skip descriptions, tooltips, effect tooltips
        if any(key.endswith(suffix) for suffix in ["_desc", "_tt", "_d"]):
            continue
        
        words = re.findall(r'[a-zA-Z]+', val.lower())
        matched = [w for w in words if w in indo_indicators]
        if matched:
            found_titles.append((idx + 1, key, val, matched))

with open(r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\scratch\all_indo_titles.txt", "w", encoding="utf-8") as out:
    out.write(f"Total potential Indonesian titles found: {len(found_titles)}\n")
    for line_no, k, v, matched in found_titles:
        out.write(f"L{line_no:4} | {k:38} | {v:50} | matched: {matched}\n")
print(f"Total potential Indonesian titles found: {len(found_titles)}. Written to scratch/all_indo_titles.txt")
