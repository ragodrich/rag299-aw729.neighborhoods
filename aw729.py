from bs4 import BeautifulSoup
import requests

r = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

neighborhoods = []
test = soup.find('table', class_ = 'wikitable').find_all('td')
for i,j in enumerate(test):
	if i == len(test)-1 or i%5 != 4:
		continue
	text = j.renderContents()
	trimmed_text = str(text.strip())
	if '<' in trimmed_text:
		neighborhoods.append(trimmed_text[2:trimmed_text.index('<')])
	elif "99" in trimmed_text:
		neighborhoods.append(trimmed_text[2:trimmed_text.index('\\xe')] + "'" + trimmed_text[trimmed_text.index('\\xe')+12:-1])
	else:
		neighborhoods.append(trimmed_text[2:-1])
finalneighbors = []

for j in neighborhoods:
	q = j.split(', ')
	for end in q:
		finalneighbors.append(end)

print(finalneighbors)
print(len(finalneighbors))

