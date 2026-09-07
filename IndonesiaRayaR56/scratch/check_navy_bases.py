for path_id in ['b', 'c', 'd', 'e', 'f']:
    with open(f'history/units/DEI_navy_starter_{path_id}.txt', 'r', encoding='utf-8') as f:
        c = f.read()
    print(f'Naval base for Path {path_id.upper()}:', 'naval_base = 13520' in c)
