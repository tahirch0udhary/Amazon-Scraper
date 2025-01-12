import os
import sys
from src.input_reader import load_queries
from src.scraper import AmazonScraper
from src.output_writer import save_to_json
from src.scraper.utils import random_delay


def scrape_amazon(queries: list):
    """our main function to scrape Amazon for all queries.
    we scrape the first 20 pages for all queries"""
    scraper = AmazonScraper()

    try:
        for query in queries:
            all_products = []
            print(f"\nstarting scrape for query: '{query}'")
            for page in range(1, 2):  # scrape the first 20 pages
                print(f"scraping page {page} for query '{query}'")
                html_content = scraper.fetch_page(query, page)
                if html_content:
                    products = scraper.parse_products(html_content)
                    all_products.extend(products)
                    print(f"parsed {len(products)} products from page {page}")
                else:
                    print(f"no content fetched for page {page} of query '{query}'") # noqa

                random_delay(2, 5)

            """here we save the results to a JSON file we use
            imported save_to_json function from output_writer.py"""
            save_to_json(all_products, query)
            print(f"completed scraping for query: '{query}'\n")

    except KeyboardInterrupt:
        print("\nscraping interupted by user. saving current progress...")
        save_to_json(all_products, query)
        sys.exit(0)
    except Exception as e:
        print(f"an unexpected error occurred: {e}")
    finally:
        scraper.close()


if __name__ == "__main__":
    input_file = os.path.join('data', 'user_queries.json')
    queries = load_queries(input_file)
    if queries:
        scrape_amazon(queries)
    else:
        print("no queries found please check the 'user_queries.json' file.")
