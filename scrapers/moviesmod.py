from typing import List, Dict
from .base import BaseScraper


class MoviesMod(BaseScraper):
    def __init__(self):
        self.base_url = "https://moviesmod.cards/search/{}"

    def get_name(self) -> str:
        return "MoviesMod"

    def request(self, query: str) -> List[Dict[str, str]]:
        url = self.base_url.format(query)
        soup = self._get_soup(url)
        items = soup.find_all("article", class_="latestPost")
        results = []
        for item in items:
            if len(results) >= self.MAX_ITEMS:
                break
            title_tag = item.select_one("h2.title a")
            if not title_tag:
                continue
            title = title_tag.text.strip()
            href = title_tag.get("href", "")
            thumb_tag = item.select_one("img")
            thumbnail = thumb_tag.get("src", "") if thumb_tag else ""

            results.append({
                "title": title,
                "url": href,
                "thumbnail": thumbnail,
            })

        return results
