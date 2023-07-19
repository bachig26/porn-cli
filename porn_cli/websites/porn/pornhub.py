from bs4 import BeautifulSoup as BS
from mov_cli.utils.scraper import WebScraper

class Provider(WebScraper):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.base_url = base_url
    
    def search(self, q: str):
        q = (
            input("[!] Please Enter the name of the Porn: ")
            if q is None
            else q
        )
        return q.replace(" ", "+")

    def results(self, data: str) -> list:
        req = self.client.get(f"{self.base_url}/video/search?search={data}")
        soup = BS(req, "lxml")
        items = soup.findAll("li", {"class": "pcVideoListItem"})
        urls = [items[i].find("a")["href"] for i in range(len(items))]
        title = [items[i].find("div", {"class": "usernameWrap"}).find("a").text + " | " + items[i].find("a")["title"] + " | " for i in range(len(items))]
        ids = [items[i]["data-video-vkey"] for i in range(len(items))]
        mov_or_tv = ["Porn" for i in range(len(items))]
        return [list(sublist) for sublist in zip(title, urls, ids, mov_or_tv)]

    def cdn_url(self, id):
        url = f"{self.base_url}/embed/{id}"
        return url
    
    def MOV_PandDP(self, m: list, state: str = "d" or "p" or "sd"):
        name = m[self.title]
        url = self.cdn_url(f"{m[self.aid]}")
        if state == "d":
            self.dl(url, name)
            return
        self.play(url, name)
