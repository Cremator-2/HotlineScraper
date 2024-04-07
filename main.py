import requests
from bs4 import BeautifulSoup
import time
import random

base_url = 'https://hotline.ua/ua/sr/?q=GeForce%20RTX%204080%20SUPER'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
n_pages = 2

for page in range(1, n_pages + 1):
    url = f"{base_url}&p={page}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('div', class_='list-item flex')

    for product in products:
        title = product.find('a', class_='item-title text-md link link--black').text.strip()
        price_range = product.find('div', class_='text-md text-orange text-lh--1').text.strip()
        link = 'https://hotline.ua' + product.find('a', class_='item-title text-md link link--black')['href']
        item_info = " ".join(
            [spec.text.strip() for spec in product.find_all('span', class_='spec-item spec-item--bullet')])
        print(f'Название: {title}\nЦена: {price_range}\nСсылка: {link}\nОписание: {item_info}\n{"-" * 40}')

    time.sleep(random.uniform(1.421, 4.8943))


