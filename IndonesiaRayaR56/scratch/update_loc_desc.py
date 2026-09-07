import codecs

path = 'localisation/english/DEI_indonesia_l_english.yml'
with open(path, 'rb') as f:
    raw = f.read()

has_bom = raw.startswith(codecs.BOM_UTF8)
text = raw.decode('utf-8-sig')

old_desc = 'Across the bustling port cities and interior highlands of Java and Sumatra, the general strike wave has paralyzed the colonial apparatus. Docks at Tanjung Priok and Tanjung Perak stand silent, railways have ceased operations, and municipal administrative offices have been emptied as civil servants walk out in sweeping defiance.\n\nIn the military garrisons of Cimahi and Magelang, native KNIL soldiers have refused orders to suppress the strikes, detaining colonial officers and opening the armories to revolutionary youth leagues. What began as labor resistance has escalated into a nationwide, coordinated uprising across the entire archipelago.\n\nFrom clandestine radio stations in Bandung and Yogyakarta, the momentous Proclamation of Independence is broadcast to the world. As the red-and-white banner unfurls over public squares from Sabang to Merauke, the colonial authority of the Dutch East Indies has collapsed, ushering Nusantara into an unprecedented new era.'

new_desc = 'Across Java and Sumatra, the general strike wave has paralyzed the colonial apparatus. Docks at Tanjung Priok stand silent and railways have ceased as civil servants walk out in sweeping defiance.\n\nIn Cimahi and Magelang, native KNIL soldiers have refused orders to quell the strikes, opening armories to revolutionary youth. From clandestine radio stations in Bandung and Yogyakarta, the Proclamation of Independence is broadcast to the world.\n\nAs the Merah-Putih banner unfurls from Sabang to Merauke, colonial authority has collapsed, ushering Nusantara into a sovereign new era.'

if old_desc in text:
    print('Found old dei_trunk.6.d, replacing...')
    text = text.replace(old_desc, new_desc)
    new_raw = codecs.BOM_UTF8 + text.encode('utf-8')
    with open(path, 'wb') as f:
        f.write(new_raw)
    print('Replaced successfully! UTF-8 BOM verified.')
else:
    print('old_desc not found exactly, let us inspect dei_trunk.6.d in file...')
    idx = text.find('dei_trunk.6.d:')
    print(text[idx:idx+500])
