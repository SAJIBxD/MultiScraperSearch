import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}


class Mlwbd:
    def __init__(self):
        self.base_url = "https://fojik.com/?s={}"

    def get_name(self) -> str:
        return "mlwbd"

    def request(self, query: str) -> list[str]:
        url = self.base_url.format(query)
        r = requests.get(url, headers=headers)
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

class MoviesLeech:

    def __init__(self):
        self.base_url = "https://moviesleech.link/wp-admin/admin-ajax.php?action=mts_search&q={}"

    def get_name(self):
        return "MoviesLeech"

    def request(self, query: str):
        url = self.base_url.format(query)
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        items = soup.select("ul.ajax-search-results > li")
        results = []
        for item in items:
            title_tag = item.select_one("a")
            image_tag = item.select_one("img")
            title = " ".join(title_tag.stripped_strings)
            url = title_tag.get("href", "")
            thumbnail = image_tag.get("src", "") if image_tag else ""

            results.append({
                "title": title,
                "url": url,
                "thumbnail": thumbnail
            })

        return results


