from bs4 import BeautifulSoup
import requests

data = requests.get('https://www.guitarcenter.com/Used/Guitars.gc#pageName=used-page&N=18144+1076&Nao=0&recsPerPage=90&&Ns=pHL&postalCode=51301&radius=100&profileCountryCode=US&profileCurrencyCode=USD')
soup = BeautifulSoup(data.content, 'html.parser')

products = soup.find_all('li', { 'class' : 'product-container' })
# print(products)
for p in products:
    product_title = p.find('div', { 'class' : 'productTitle' }).text
    product_price = p.find('span', { 'class' : 'productPrice' }).text
    product_condition = p.find('div', { 'class' : 'productCondition' }).text


    print(product_title, product_price, product_condition)
