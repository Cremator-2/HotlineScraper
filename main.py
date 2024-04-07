import requests
from bs4 import BeautifulSoup

url = 'https://hotline.ua/ua/sr/?q=GeForce%20RTX%204080%20SUPER'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_='list-item flex')

for product in products:
    title = product.find('a', class_='item-title text-md link link--black').text.strip()
    price_range = product.find('div', class_='text-md text-orange text-lh--1').text.strip()
    link = 'https://hotline.ua' + product.find('a', class_='item-title text-md link link--black')['href']
    item_info = " ".join([spec.text.strip() for spec in product.find_all('span', class_='spec-item spec-item--bullet')])
    print(f'Название: {title}\nЦена: {price_range}\nСсылка: {link}\nИнфо: {item_info}\n{"-" * 40}')
