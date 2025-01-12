import json
from typing import List


def load_queries(file_path: str) -> List[str]:
    """load search queries from a JSON file. we call this function
    in main file when reading from json file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            queries = json.load(file)
            if isinstance(queries, list):
                return queries
            else:
                print("error: JSON file does not contain a list.")
                return []
    except FileNotFoundError:
        print(f"error: File not found at {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"error: Failed to decode JSON file. {e}")
        return []
