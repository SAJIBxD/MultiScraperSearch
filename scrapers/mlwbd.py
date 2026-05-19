from typing import List, Dict
import json
import requests
from bs4 import BeautifulSoup
from .base import BaseScraper


class Mlwbd(BaseScraper):
    def __init__(self):
        self.base_url = "https://fojik.com/?s={}"
        self.reqbin_url = "https://apius.reqbin.com/api/v1/requests"

    def get_name(self) -> str:
        return "mlwbd"

    def _get_soup_via_reqbin(self, target_url: str) -> BeautifulSoup:
        """Fetch page content via reqbin API and return BeautifulSoup object."""
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:150.0) Gecko/20100101 Firefox/150.0"
        }
        
        payload = {
            "json": json.dumps({
                "method": "GET",
                "url": target_url
            })
        }
        
        response = requests.post(
            self.reqbin_url,
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            response_data = response.json()
            html_content = response_data.get("Content", "")
            if not html_content:
                raise Exception("No content returned from reqbin API")
            return BeautifulSoup(html_content, "lxml")
        else:
            raise Exception(f"Reqbin API error: Status {response.status_code}")

    def request(self, query: str) -> List[Dict[str, str]]:
        url = self.base_url.format(query)
        soup = self._get_soup_via_reqbin(url)
        items = soup.find_all("div", class_="result-item")
        results = []
        for item in items:
            if len(results) >= self.MAX_ITEMS:
                break
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
