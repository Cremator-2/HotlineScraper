import requests
from bs4 import BeautifulSoup

url = 'https://hotline.ua/ua/sr/?q=GeForce%20RTX%204080%20SUPER'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)

# Парсинг HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Поиск всех продуктов на странице
products = soup.find_all('div', class_='list-item flex')

# Вывод информации о каждом продукте
for product in products:
    # Название продукта
    title = product.find('a', class_='item-title text-md link link--black').text.strip()

    # Цена продукта
    price_range = product.find('div', class_='text-md text-orange text-lh--1').text.strip()

    # Ссылка на продукт
    link = 'https://hotline.ua' + product.find('a', class_='item-title text-md link link--black')['href']

    print(f'Название: {title}\nЦена: {price_range}\nСсылка: {link}\n{"-" * 40}')
