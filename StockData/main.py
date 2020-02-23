from bs4 import BeautifulSoup
import requests

data = requests.get('https://www.gurufocus.com/stock_list.php?n=100')
soup = BeautifulSoup(data.content, 'lxml')
soup.encode('utf-8')

table = soup.find('table', { 'id' : 'R1' })
tbody = table.find('tbody')

repetitions = {''}
for items in tbody.find_all('tr'):
    title = items.find('a', { 'class' : 'nav' }).text.strip()
    value = items.find_all('td')[2].text.strip()

    print(title, value)

    # repetitions.add(str(title))

print(repetitions)