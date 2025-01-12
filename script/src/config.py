BASE_URL = "https://www.amazon.com/s"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/85.0.4183.102 Safari/537.36"
    )
}
TIMEOUT = 60000  # timeout for page loading in milliseconds
PAGE_WAIT_SELECTOR = '.s-main-slot'  # selector to wait for before scraping
OUTPUT_DIR = 'data/outputs'  # directory to save output JSON files
