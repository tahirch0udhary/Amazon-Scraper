import json
import os
from typing import List
from src.data_model import Product


def save_to_json(data: List[Product], file_name: str):
    """Save scraped data to a JSON file."""
    current_dir = os.path.dirname(__file__)
    frontend_data_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..', 'Scraper', 'frontend', 'scraper-frontend', 'public', 'data')) # noqa

    """we will ensure the frontend/data directory exists"""
    os.makedirs(frontend_data_dir, exist_ok=True)

    """define the full path for the JSON file"""
    file_path = os.path.join(frontend_data_dir, f"{file_name}.json")

    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            # convert Product instances to dictionaries
            json.dump([product.to_dict() for product in data],
                      file,
                      indent=4,
                      ensure_ascii=False)
        print(f"successfully saved data to {file_path}")
    except IOError as e:
        print(f"error saving file {file_path}: {e}")


"""import json
import os
from typing import List
from src.data_model import Product
from src.config import OUTPUT_DIR


def save_to_json(data: List[Product], file_name: str):
    save scraped data to a JSON file.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_path = os.path.join(OUTPUT_DIR, f"{file_name}.json")
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([product.to_dict() for product in data],
                      file,
                      indent=4,
                      ensure_ascii=False)
        print(f"successfully saved data to {file_path}")
    except IOError as e:
        print(f"error saving file {file_path}: {e}")
"""
