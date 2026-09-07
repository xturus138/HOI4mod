with open('common/decisions/categories/DEI_decision_categories.txt', 'r', encoding='utf-8') as f:
    print('=== Categories ===')
    print(f.read()[:1000])

with open('common/decisions/DEI_decisions.txt', 'r', encoding='utf-8') as f:
    print('=== Decisions ===')
    print(f.read()[:1000])
