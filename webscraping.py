import requests,bs4

example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
author = example_soup.select('html')
exampletext = open('example.txt','w')
exampletext.write(author[0].getText())
exampletext.close()