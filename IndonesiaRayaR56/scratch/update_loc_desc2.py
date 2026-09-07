import codecs, re

path = 'localisation/english/DEI_indonesia_l_english.yml'
with open(path, 'rb') as f:
    raw = f.read()

text = raw.decode('utf-8-sig')

pattern = r'(dei_trunk\.6\.d:\s*")[^"]*(")'
match = re.search(pattern, text)
if match:
    print('Match found!')
    new_text = r'Across Java and Sumatra, the general strike wave has paralyzed the colonial apparatus. Docks at Tanjung Priok stand silent and railways have ceased as civil servants walk out in sweeping defiance.\n\nIn Cimahi and Magelang, native KNIL soldiers have refused orders to quell the strikes, opening armories to revolutionary youth. From clandestine radio stations in Bandung and Yogyakarta, the Proclamation of Independence is broadcast to the world.\n\nAs the Merah-Putih banner unfurls from Sabang to Merauke, colonial authority has collapsed, ushering Nusantara into a sovereign new era.'
    replaced = text[:match.start(1)] + 'dei_trunk.6.d: "' + new_text + '"' + text[match.end(2):]
    new_raw = codecs.BOM_UTF8 + replaced.encode('utf-8')
    with open(path, 'wb') as f:
        f.write(new_raw)
    print('Updated successfully with UTF-8 BOM!')
else:
    print('Pattern not matched!')
