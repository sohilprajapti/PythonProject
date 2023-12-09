import webbrowser, requests

res = requests.get('https://readnovelfull.com/omniscient-readers-viewpoint/chapter-421-the-secretive-plotter-6.html')

res.raise_for_status()


print(len(res.text))

playfile = open('orv.html','wb')

for chunk in res.iter_content(100000):
    playfile.write(chunk)