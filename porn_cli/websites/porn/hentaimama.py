from mov_cli.utils.scraper import WebScraper
from bs4 import BeautifulSoup as BS
import re


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
        return q
    
    def results(self, data: str) -> list:
        req = self.client.get(f"{self.base_url}/?s={data}").text
        soup = BS(req, self.scraper)
        items = soup.findAll("div", {"class": "result-item"})
        urls = [items[i].find("a")["href"] for i in range(len(items))]
        title = [items[i].find("img")["alt"] for i in range(len(items))]
        ids = [i for i in range(len(items))]
        mov_or_tv = ["TV" for i in range(len(items))]
        return [list(sublist) for sublist in zip(title, urls, ids, mov_or_tv)]

    def ask(self, url):
        req = self.client.get(url).text
        soup = BS(req, self.scraper)
        episodes = soup.findAll("article", {"class": "item se episodes"})
        episode = int(self.askepisode(len(episodes)))
        episodes = episodes[::-1]
        url = episodes[episode - 1].find("a")["href"]
        return url, episode

    def cdn_url(self, url):
        req = self.client.get(url, True).text
        soup = BS(req, self.scraper)
        id = soup.find("input", {"name": "idpost"})["value"]
        admin_ajax = self.client.post("https://hentaimama.io/wp-admin/admin-ajax.php", data={"action": "get_player_contents", "a": id}).text
        p_regex = '\?p=(.*?)."' 
        p = re.findall(p_regex, admin_ajax)[0]
        new2 = self.client.get(self.base_url + "/new2.php?p=" + p).text
        new2_regex = 'file: "(.*?)"'
        url = re.findall(new2_regex, new2)[0]
        return url
    
    def TV_PandDP(self, t: list, state: str = "d" or "p" or "sd"):
        name = t[self.title]
        url, episode = self.ask(t[self.url])
        url = self.cdn_url(url)
        if state == "d":
            self.dl(url, name, season=".", episode=episode)
            return
        self.play(url, name)
