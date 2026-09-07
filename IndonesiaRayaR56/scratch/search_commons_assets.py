import requests

def search_commons(query):
    url = 'https://commons.wikimedia.org/w/api.php'
    params = {
        'action': 'query',
        'generator': 'search',
        'gsrsearch': query,
        'gsrnamespace': 6,
        'gsrlimit': 5,
        'prop': 'imageinfo',
        'iiprop': 'url|size',
        'format': 'json'
    }
    headers = {'User-Agent': 'HOI4ModBot/1.0 (contact@example.com)'}
    r = requests.get(url, params=params, headers=headers).json()
    pages = r.get('query', {}).get('pages', {})
    print(f'=== Results for: {query} ===')
    for pid, pdata in pages.items():
        title = pdata.get('title')
        ii = pdata.get('imageinfo', [{}])[0]
        u = ii.get('url')
        print(f'{title} -> {u}')

search_commons('Operasi Trikora')
search_commons('Indonesian soldiers 1948')
search_commons('Tentara Keamanan Rakyat')
search_commons('TNI gerilya')
search_commons('Laskar')
