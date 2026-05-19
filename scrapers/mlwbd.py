from typing import List, Dict
from .base import BaseScraper


class Mlwbd(BaseScraper):
    def __init__(self):
        self.base_url = "https://fojik.com/?s={}"

    def get_name(self) -> str:
        return "mlwbd"

    def request(self, query: str) -> List[Dict[str, str]]:
        url = self.base_url.format(query)
        soup = self._get_soup(url)
        items = soup.find_all("div", class_="result-item")
        results = []
        for item in items:
            title_tag = item.select_one(".details .title a")
            if not title_tag:
                continue
            title = title_tag.text.strip()
            href = title_tag.get("href", "")
            thumb_tag = item.select_one(".image img")
            thumbnail = thumb_tag.get("src", "") if thumb_tag else ""

            results.append({
                "title": title,
                "url": href,
                "thumbnail": thumbnail,
            })

        return results
