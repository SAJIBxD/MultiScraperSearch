from typing import List, Dict
from .base import BaseScraper


class MoviesLeech(BaseScraper):
    def __init__(self):
        self.base_url = "https://moviesleech.link/wp-admin/admin-ajax.php?action=mts_search&q={}"

    def get_name(self) -> str:
        return "MoviesLeech"

    def request(self, query: str) -> List[Dict[str, str]]:
        url = self.base_url.format(query)
        soup = self._get_soup(url)
        items = soup.select("ul.ajax-search-results > li")
        results = []
        for item in items:
            title_tag = item.select_one("a")
            if not title_tag:
                continue
            image_tag = item.select_one("img")
            title = " ".join(title_tag.stripped_strings)
            href = title_tag.get("href", "")
            thumbnail = image_tag.get("src", "") if image_tag else ""

            results.append({
                "title": title,
                "url": href,
                "thumbnail": thumbnail,
            })

        return results
