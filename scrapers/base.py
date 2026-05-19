from __future__ import annotations
import abc
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.127 Safari/537.36'
}


class BaseScraper(abc.ABC):
    """Abstract base class for scrapers."""

    headers = HEADERS
    MAX_ITEMS = 10

    @abc.abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def request(self, query: str) -> List[Dict[str, str]]:
        raise NotImplementedError

    def _get_soup(self, url: str, headers: Optional[dict] = None) -> BeautifulSoup:
        h = headers or self.headers
        r = requests.get(url, headers=h)
        return BeautifulSoup(r.text, "lxml")
