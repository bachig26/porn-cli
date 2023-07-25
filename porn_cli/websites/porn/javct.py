from bs4 import BeautifulSoup as BS
from mov_cli.utils.scraper import WebScraper
from mov_cli.extractors.doodstream import dood
import re
from base64 import b64encode

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
        req = self.client.get(f"{self.base_url}/search/{data}").text
        soup = BS(req, self.scraper)
        items = soup.findAll("div", {"class": "card__content"})
        urls = [items[i].find("a")["href"] for i in range(len(items))]
        title = [items[i].find("span").find("a").text + " | " + items[i].find("h3").find("a").text  for i in range(len(items))]
        ids = [i for i in range(len(items))]
        mov_or_tv = ["Porn" for i in range(len(items))]
        return [list(sublist) for sublist in zip(title, urls, ids, mov_or_tv)]

    def doodext(self, url):
        req = self.client.get(url).text
        soup = BS(req, self.scraper)
        search = soup.prettify()
        token = re.findall(r'name="_token" value="(.*?)"', search)[0]
        socket = re.findall(r'name="_socket" value="(.*?)"', search)[0]
        key = f"{token}:{socket}"
        key = key.encode('ascii')
        auth = b64encode(key).decode("UTF-8")
        serverlist = soup.findAll("li", {"class": "switch-source"})
        dood = []
        for server in serverlist:
            if str(server).__contains__("DD"):
                dood.append(server)
        if dood == None:
            raise Exception("DoodStream Link not found")
        server = dood[0]
        datasource = server["data-source"]
        dataep = server["data-episode"]
        self.client.set_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0", "Referer": url, "Authorization": f"Basic {auth}"})
        response = self.client.post(f"{self.base_url}/ajax/player", {"episode": dataep, "filmId": datasource}).text 
        url = re.findall(r"[a-z]+.[a-z]+\\\/e\\\/(.*?)\\", response)[0]
        return url
        
    def MOV_PandDP(self, m: list, state: str = "d" or "p" or "sd"):
        name = m[self.title]
        suffix = self.doodext(m[self.url])
        url = dood(suffix)
        if state == "d":
            self.dl(url, name)
            return
        self.play(url, name)



