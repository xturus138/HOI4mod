import os

r56_leaders = r"C:\Program Files (x86)\Steam\steamapps\workshop\content\394360\820260968\gfx\leaders\INS"
if os.path.exists(r56_leaders):
    for f in os.listdir(r56_leaders):
        print(f)
else:
    print("Not found")
