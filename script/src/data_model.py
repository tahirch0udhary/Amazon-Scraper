from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Product:
    title: str
    reviews: str
    price: str
    rating: str
    image_url: str
    buyers: str
    scrape_date: str = field(
        default_factory=lambda: datetime.now().isoformat())

    def to_dict(self):
        """convert the Product dataclass to a dictionary."""
        return {
            "title": self.title,
            "reviews": self.reviews,
            "price": self.price,
            "rating": self.rating,
            "image_url": self.image_url,
            "buyers": self.buyers,
            "scrape_date": self.scrape_date,
        }
