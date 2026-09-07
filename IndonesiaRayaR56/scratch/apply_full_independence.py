full_independence_block = '''			if = {
				limit = { is_subject = yes }
				OVERLORD = {
					set_autonomy = {
						target = ROOT
						autonomy_state = autonomy_free
					}
				}
			}
			set_autonomy = {
				target = ROOT
				autonomy_state = autonomy_free
			}
			end_puppet = yes
			HOL = {
				set_autonomy = {
					target = INS
					autonomy_state = autonomy_free
				}
				end_puppet = INS
				remove_from_faction = INS
			}
			remove_ideas = INS_political_idea
			remove_ideas = INS_army_idea
			remove_ideas = INS_economy_idea
			remove_ideas = INS_science_idea'''

# 1. Update DEI_indonesia_focus_tree.txt
tree_path = 'common/national_focus/DEI_indonesia_focus_tree.txt'
with open(tree_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace in dei_focus_momentum_kemerdekaan
old_m = 'end_puppet = yes\n\t\t\tset_cosmetic_tag = INS_REPUBLIK_NKRI'
new_m = f'{full_independence_block}\n\t\t\tset_cosmetic_tag = INS_REPUBLIK_NKRI'
assert old_m in text, "old_m not found in focus tree!"
text = text.replace(old_m, new_m, 1)

# Add to path roots A, B, C, D, E, F
roots = [
    'dei_focus_a_proklamasi',
    'dei_focus_b_root',
    'dei_focus_c_root',
    'dei_focus_d_root',
    'dei_focus_e_root',
    'dei_focus_f_root'
]

for r in roots:
    target_str = f'id = {r}'
    idx = text.find(target_str)
    assert idx != -1, f'{r} not found!'
    # find completion_reward = {
    cr_idx = text.find('completion_reward = {', idx)
    assert cr_idx != -1, f'completion_reward for {r} not found!'
    # insert full_independence_block right after completion_reward = {
    insert_pos = cr_idx + len('completion_reward = {')
    text = text[:insert_pos] + '\n' + full_independence_block + text[insert_pos:]
    print(f'Added full independence to {r}')

with open(tree_path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated DEI_indonesia_focus_tree.txt successfully!')

# 2. Update events/DEI_00_shared_trunk_events.txt (dei_trunk.6)
trunk_path = 'events/DEI_00_shared_trunk_events.txt'
with open(trunk_path, 'r', encoding='utf-8') as f:
    t_text = f.read()

old_trunk = 'INS = {\n\t\t\t\tend_puppet = yes'
new_trunk = f'INS = {{\n{full_independence_block}'
assert old_trunk in t_text, "old_trunk not found!"
t_text = t_text.replace(old_trunk, new_trunk, 1)

with open(trunk_path, 'w', encoding='utf-8') as f:
    f.write(t_text)
print('Updated dei_trunk.6 in DEI_00_shared_trunk_events.txt successfully!')

# 3. Update common/decisions/DEI_debug_decisions.txt
dbg_path = 'common/decisions/DEI_debug_decisions.txt'
with open(dbg_path, 'r', encoding='utf-8') as f:
    d_text = f.read()

# In dei_debug_instant_prologue: replace end_puppet = yes
old_d = 'end_puppet = yes\n\t\t\tset_cosmetic_tag = INS_REPUBLIK_NKRI'
new_d = f'{full_independence_block}\n\t\t\tset_cosmetic_tag = INS_REPUBLIK_NKRI'
assert old_d in d_text, "old_d not found in debug decisions!"
d_text = d_text.replace(old_d, new_d, 1)

# In dei_debug_path_a to f: add full_independence_block
for p in ['dei_debug_path_a', 'dei_debug_path_b', 'dei_debug_path_c', 'dei_debug_path_d', 'dei_debug_path_e', 'dei_debug_path_f']:
    idx = d_text.find(p)
    cr_idx = d_text.find('complete_effect = {', idx)
    insert_pos = cr_idx + len('complete_effect = {')
    d_text = d_text[:insert_pos] + '\n' + full_independence_block + d_text[insert_pos:]
    print(f'Added full independence to {p}')

with open(dbg_path, 'w', encoding='utf-8') as f:
    f.write(d_text)
print('Updated DEI_debug_decisions.txt successfully!')
