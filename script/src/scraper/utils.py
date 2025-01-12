# src/scraper/utils.py

import time
import random


def random_delay(min_seconds: float = 2.0, max_seconds: float = 5.0):
    """Introduce a random delay to mimic human behavior and avoid detection."""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)
