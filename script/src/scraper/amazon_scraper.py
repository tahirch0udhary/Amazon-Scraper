# src/scraper/amazon_scraper.py

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError # noqa
from typing import List
from src.config import BASE_URL, TIMEOUT, PAGE_WAIT_SELECTOR
from src.data_model import Product


class AmazonScraper:
    def __init__(self):
        """ we will use playwright to avoicd blocking from amazon website.
        we first Initialize Playwright and launch the browser."""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()

    def fetch_page(self, query: str, page_number: int) -> str:
        """Fetch a single page of search results
        from Amazon using Playwright."""
        url = f"{BASE_URL}?k={query}&page={page_number}"
        try:
            self.page.goto(url, timeout=TIMEOUT)
            self.page.wait_for_selector(PAGE_WAIT_SELECTOR, timeout=15000)
            content = self.page.content()
            return content
        except PlaywrightTimeoutError:
            print(f"timeout while loading page {page_number} for query '{query}'.") # noqa
            return ""
        except Exception as e:
            print(f"error fetching page {page_number} for query '{query}': {e}") # noqa
            return ""

    def parse_products(self, html_content: str) -> List[Product]:
        """Parse product details from the HTML content. we will verify the css
        classes for productes using inspect option from our browser
        and extract the required details."""
        soup = BeautifulSoup(html_content, 'html.parser')
        product_list = []

        # this line will find all product containers
        product_containers = soup.select(
            '.s-main-slot .s-result-item, .s-card-container')
        if not product_containers:
            print("no product containers found. check the HTML structure.")
            return product_list

        for product in product_containers:
            try:
                """we will skip non-product entries like sponsers and ads"""
                if not product.get('data-asin'):
                    continue

                """ here we will extract product title. during inspection i
                see different products have different css classes for title
                so i use them all to extract title"""
                title_element = (product.select_one('h2.a-size-medium') or
                                 product.select_one('h2.a-size-base') or
                                 product.select_one('span.a-size-medium-plus'))
                title = title_element.text.strip() if title_element else "N/A"
                if title == "N/A":  # skip products with missing titles
                    continue

                """no we will extract reviews using the below classes"""
                reviews_element = product.select_one(
                    '.a-size-base.s-underline-text')
                reviews = reviews_element.text.strip() if reviews_element else "N/A" # noqa

                """here we are extracting the price of products. same like
                title we use different format of classes for different
                products. """
                price_element = product.select_one('.a-price span.a-offscreen')
                if price_element:
                    price = price_element.text.strip()
                else:
                    secondary_price_element = product.select_one('div.a-row.a-size-base.a-color-secondary span.a-color-base') or \
                                               product.select_one('div.a-row.a-size-mini.a-color-base span.a-price span.a-offscreen')
                    price = secondary_price_element.text.strip() if secondary_price_element else "N/A"

                """here we extract rating"""
                rating_element = product.select_one('span.a-icon-alt')
                rating = rating_element.text.strip().split(" ")[0] if rating_element else "N/A"

                """here we extract image URL"""
                image_element = product.select_one('img.s-image')
                image_url = image_element['src'] if image_element else "N/A"

                """here we extract number of buyers"""
                buyers_element = product.select_one('span.a-size-base.a-color-secondary')
                buyers = buyers_element.text.strip() if buyers_element else "N/A"

                """now finally here we create a product instance"""
                product_obj = Product(
                    title=title,
                    reviews=reviews,
                    price=price,
                    rating=rating,
                    image_url=image_url,
                    buyers=buyers
                )

                product_list.append(product_obj)
            except AttributeError:
                continue  # skip products with missing fields

        return product_list

    def close(self):
        """close the browser and Playwright instance."""
        self.page.close()
        self.browser.close()
        self.playwright.stop()
