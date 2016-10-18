from bs4 import BeautifulSoup
import urllib.request

page = urllib.request.urlopen('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City#Community_areas').read()

soup = BeautifulSoup(page, 'html.parser')
soup.prettify()
neighborhoods = []

i = 0
j = -1
for row in soup.find('table').find_all('td'):
    if(i - 5 == j):
        indices = []
        row = str(row)
        for i in range(len(row)):
            if i <= 3:
                continue
            if row[i] != '<':
                indices.append(i)
            else:
                break
        newRow = ''.join(y for x, y in enumerate(row) if x in indices)
        neighborhoods.append(newRow)
        j = i
    i += 1
neighborhoods.pop(-1)

neigh = []
for row in neighborhoods:
    row = row.split(', ')
    for i in range(len(row)):
        neigh.append(row[i])
print(neigh)