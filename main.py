import requests
from bs4 import BeautifulSoup
import time
import random
import csv
import datetime
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s')

HOTLINE_URL = 'https://hotline.ua'
STRFTIME = "%H-%M-%S_%d-%m-%Y"

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}


def get_search_info(item: str, n_pages: int, current_time: str = datetime.datetime.now().strftime(STRFTIME)):
    _item = item.replace("_", " ")
    logging.info(f"Starting search for '{_item}' across {n_pages} pages.")

    search_item = item.replace("_", "%20")
    base_url = f'{HOTLINE_URL}/ua/sr/?q={search_item}'

    filename = f'hotline_search__{item}__{current_time}.csv'
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Price', 'Link', 'Description', 'Offers', 'Product website', 'Specification'])

        for page in range(1, n_pages + 1):
            url = f"{base_url}&p={page}"
            logging.info(f"Fetching URL: {url}")
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.text, 'html.parser')
            products = soup.find_all('div', class_='list-item flex')

            for product in products:
                title = product.find('a', class_='item-title text-md link link--black').text.strip()
                price_range = product.find('div', class_='text-md text-orange text-lh--1').text.strip()
                link = HOTLINE_URL + product.find('a', class_='item-title text-md link link--black')['href']
                item_info = " ".join(
                    [spec.text.strip() for spec in product.find_all('span', class_='spec-item')])
                offers_element = product.find('a', class_='link link--black text-sm m_b-5')
                offers_count = offers_element.text.strip().split()[2].strip('()') if offers_element else '1'

                time.sleep(random.uniform(0.313, 2.067))

                product_website, specification = get_specification_table(link)

                writer.writerow([title, price_range, link, item_info, offers_count, product_website, specification])

            time.sleep(random.uniform(1.421, 4.8943))
    logging.info(f"Finished searching. Results saved to {filename}")


def get_specification_table(link):
    url_about = f"{link}?tab=about"
    logging.info(f"Fetching URL: {url_about}")
    response = requests.get(url_about, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    link_tag = soup.find('a', {'data-tracking-id': 'product-33'})

    if link_tag and 'data-outer-link' in link_tag.attrs:
        product_website = link_tag['data-outer-link']
    else:
        product_website = 'N/A'

    specifications_table = soup.find('table', class_='specifications__table')

    for tooltip in specifications_table.find_all('div', class_='tooltip specifications__tooltip'):
        tooltip.decompose()

    specification_table_text = specifications_table.get_text(separator='\n', strip=True)

    return product_website, specification_table_text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hotline Scraper")
    parser.add_argument(
        "-s",
        "--search",
        help="Search query",
        nargs="+",
        default=[]
    )
    parser.add_argument(
        "-p",
        "--pages",
        help="Number of pages to scrape",
        type=int,
        default=1
    )
    args = parser.parse_args()

    pages = args.pages
    items = list(args.search)

    run_time = datetime.datetime.now().strftime(STRFTIME)
    for item in items:
        get_search_info(item=item, n_pages=pages, current_time=run_time)
        time.sleep(random.uniform(2.8423, 3.41294))

