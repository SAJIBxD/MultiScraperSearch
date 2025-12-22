import requests
from bs4 import BeautifulSoup


class Mlwbd:
    def __init__(self):
        self.base_url = "https://freefunz.com/?s={}"

    def get_name(self) -> str:
        return "mlwbd"

    def request(self, query: str) -> list[str]:
        url = self.base_url.format(query)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        items = soup.find_all("div", class_="result-item")
        results = []
        for item in items:
            title_tag = item.select_one(".details .title a")
            title = title_tag.text.strip()
            url = title_tag["href"]
            thumbnail = item.select_one(".image img")["src"]

            results.append({
                "title": title,
                "url": url,
                "thumbnail": thumbnail
            })

        return results
class MoviesMod:

    def __init__(self):
        self.base_url = "https://moviesmod.cards/search/{}"

    def get_name(self):
        return "MoviesMod"

    def request(self, query: str):
        url = self.base_url.format(query)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        items = soup.find_all("article", class_="latestPost")
        results = []
        for item in items:
            title_tag = item.select_one("h2.title a")
            title = title_tag.text.strip()
            url = title_tag["href"]
            thumbnail = item.select_one("img")["src"]

            results.append({
                "title": title,
                "url": url,
                "thumbnail": thumbnail
            })

        return results




