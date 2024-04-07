import requests
from bs4 import BeautifulSoup
import time
import random
import csv
import datetime
import argparse


def get_search_info(item: str, n_pages: int):
    search_item = item.replace("_", "%20")
    base_url = f'https://hotline.ua/ua/sr/?q={search_item}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f'hotline_search-{item}-{current_time}.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Link', 'Description', 'Offers'])

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
                    [spec.text.strip() for spec in product.find_all('span', class_='spec-item')])
                offers_element = product.find('a', class_='link link--black text-sm m_b-5')
                offers_count = offers_element.text.strip().split()[2].strip('()') if offers_element else '1'
                writer.writerow([title, price_range, link, item_info, offers_count])

            time.sleep(random.uniform(1.421, 4.8943))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "-s",
        "--search",
        help="",
        nargs="+",
        default=[]
    )
    parser.add_argument(
        "-p",
        "--pages",
        help="",
        type=int,
        default=1
    )
    args = parser.parse_args()

    pages = args.pages
    items = list(args.search)

    for item in items:
        time.sleep(random.uniform(2.8423, 3.41294))
        get_search_info(item=item, n_pages=pages)

