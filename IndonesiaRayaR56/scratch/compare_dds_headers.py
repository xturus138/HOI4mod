import os

goals_dir = r"c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56\gfx\interface\goals"

for fname in ["focus_dei_pax_neerlandica.dds", "focus_dei_pembangkangan.dds", "focus_dei_momentum_kemerdekaan.dds"]:
    fp = os.path.join(goals_dir, fname)
    with open(fp, "rb") as f:
        data = f.read()
    print(f"=== {fname} ===")
    print(f"  Length: {len(data)} bytes")
    print(f"  Header magic: {data[:4]}")
    print(f"  Flags: {int.from_bytes(data[8:12], 'little')}")
    print(f"  Height: {int.from_bytes(data[12:16], 'little')}, Width: {int.from_bytes(data[16:20], 'little')}")
    print(f"  Pitch/LinearSize: {int.from_bytes(data[20:24], 'little')}")
    print(f"  FourCC: {data[84:88]}")
    print(f"  RGBBitCount: {int.from_bytes(data[88:92], 'little')}")
    print(f"  RBitMask: {hex(int.from_bytes(data[92:96], 'little'))}")
    print(f"  GBitMask: {hex(int.from_bytes(data[96:100], 'little'))}")
    print(f"  BBitMask: {hex(int.from_bytes(data[100:104], 'little'))}")
    print(f"  ABitMask: {hex(int.from_bytes(data[104:108], 'little'))}")
