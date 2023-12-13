#! Python

import requests,sys, webbrowser, bs4

if len(sys.argv) >= 2:
    search = '+'.join(sys.argv[1:])
    req = requests.get(f'https://search.brave.com/search?q={search}')
    req.raise_for_status()
    soup = bs4.BeautifulSoup(req.text, 'html.parser')
    linkElems = soup.select('a[class="h svelte-1dihpoi"]')
    numoftabs = min(5,len(linkElems))
    for i in range(numoftabs):
        tab = linkElems[i].get('href')
        webbrowser.open(tab)
else:
    print('nothing')

