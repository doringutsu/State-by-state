from bs4 import BeautifulSoup
import urllib2
import os
import urllib
import os
import getxml
#create connection with main page
url = 'http://www.heart.org/HEARTORG/General/State-by-State-NIH-Allocations_UCM_440585_Article.jsp'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')

#get all the links to countries
div = soup.find('div', class_ = 'content')
table = div.find('table', width = 400)

for row in table.findChildren('tr'):
	for cell in row.findChildren('td'):

		link = cell.find('a').get('href')
		url = 'http://www.heart.org/' + link

		state = cell.text

		urllib.urlretrieve (url, 'pdf/' + state + '.pdf')

		getxml.getxml('pdf/' + state)

		print state + ' done'
	