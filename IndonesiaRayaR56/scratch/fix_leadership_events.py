import re

with open(r'events\DEI_leadership_events.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace:
# recruit_character = (CHAR)
# add_country_leader_role = { ... }
# with:
# recruit_character = \1
# promote_character = \1

pattern = r'recruit_character\s*=\s*([a-zA-Z0-9_]+)\s*add_country_leader_role\s*=\s*\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'

def repl(m):
    c_id = m.group(1)
    return f'recruit_character = {c_id}\n\t\tpromote_character = {c_id}'

new_text, count = re.subn(pattern, repl, text)
print(f'Replaced {count} occurrences of add_country_leader_role with promote_character!')

with open(r'events\DEI_leadership_events.txt', 'w', encoding='utf-8') as f:
    f.write(new_text)

diff = new_text.count('{') - new_text.count('}')
print(f'Leadership events updated! Brace diff: {diff}')
