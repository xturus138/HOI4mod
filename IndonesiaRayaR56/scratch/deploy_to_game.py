import os, shutil

src = r'c:\Users\radit\Project\VisualStudioProject\Personal\HOI4MODS\Indonesia Sub Mod 56\HOI4mod\IndonesiaRayaR56'
dst = r'C:\Users\radit\Documents\Paradox Interactive\Hearts of Iron IV\mod\IndonesiaRayaR56'

print(f'Deploying from {src} to {dst}...')

ignore_dirs = {'.git', 'scratch', 'preview_app', '__pycache__'}
ignore_files = {'preview.html', 'server.py'}

copied_files = 0
for root, dirs, files in os.walk(src):
    # filter out ignored dirs
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    rel_path = os.path.relpath(root, src)
    dest_dir = os.path.join(dst, rel_path) if rel_path != '.' else dst
    
    os.makedirs(dest_dir, exist_ok=True)
    
    for f in files:
        if f in ignore_files or f.endswith('.pyc'):
            continue
        s_file = os.path.join(root, f)
        d_file = os.path.join(dest_dir, f)
        shutil.copy2(s_file, d_file)
        copied_files += 1

print(f'Deployment complete! Copied {copied_files} files.')
