with open('events/DEI_leadership_events.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
events = re.findall(r'id\s*=\s*(dei_leadership\.[0-9]+)', text)
print('Leadership events found:', events)

# Check for any remaining add_country_leader_role or broken syntax
print('add_country_leader_role in leadership events:', 'add_country_leader_role' in text)
print('promote_character in leadership events:', 'promote_character' in text)
