from bs4 import BeautifulSoup
import re
_file = open('pdf/Alabama.xml')

soup = BeautifulSoup(_file.read(), 'xml')
_list = []
table = soup.find_all('LTTextBoxHorizontal')[3]

totals = table.find_all('LTTextLineHorizontal')
table = soup.find_all('LTTextBoxHorizontal')[10]
numbers = table.find_all('LTTextLineHorizontal')
diff = len(totals) - len(numbers)

for i,tag in enumerate(totals):
	print tag.text
	if tag.text == 'TOTAL ':
		bbox = tag.attrs['bbox'].encode('ascii', 'ignore')
		bbox = bbox[1:len(bbox)-1]
		nr = bbox.split(',', 4)
		_dict = {
		'x0' : float(nr[0]),
		'y0' : float(nr[1]),
		'x1' : float(nr[2]),
		'x2' : float(nr[3])
		}
		_list.append(_dict)

_totals = []
begin = 0
_sum = 0
for i,tag in enumerate(numbers[1:]):
	nr = int(tag.text.replace(',','')[1:])
	print nr
	if nr == _sum:
		_sum = 0
		_totals.append(nr)
	else:
		_sum = _sum + nr
	

print 'TOTALS ::::' + str(len(totals))
print 'NUMBERS ::::' + str(len(numbers))
print 'DIFFERENCE ::::' + str(diff)

print _totals
#print _list
#for item in _list:
	#print numbers[item + diff].text

