from bs4 import BeautifulSoup

path = '1.html'

with open(path, 'r',encoding='utf-8') as f:
	Soup = BeautifulSoup(f.read(), 'lxml')
	# print(Soup)
	# titles = Soup.select('body > title')[0]
	titles = Soup.select('body > title')[0].get_text()
	print(type(titles))
	print(titles)
	# keywords = Soup.select('body > div[id=div_a] > div[class=container] > input[id=aysn_keyword]')
	# keywords = Soup.select('body > div[id=div_a] > div[class=container] > input')
	keywords = Soup.select('body > div[id=div_a] > div[class=container] > input')[0]["value"]
	print(type(keywords))
	print(keywords)