with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for id_name in ['view-overview', 'view-practice', 'view-vocabulary', 'view-analyzer', 'view-profile', 'view-admin', 'view-progress', 'view-bookmarks']:
    matches = list(re.finditer(f'id="{id_name}"', text))
    print(f'{id_name}: count = {len(matches)}')
