import os
import sys
import platform

import click
from .utils.provider import ask
from .utils.scraper import WebScraper
from .websites.hentaimama import hentaimama
from .websites.javct import javct
from .websites.xxxmax import xxxmax
from .websites.pornhub import pornhub

calls = {
    "hentaimama": [hentaimama, "https://hentaimama.io"],
    "javct": [javct, "https://javct.net"],
    "xxxmax": [xxxmax, "https://xxxmax.net"],
    "pornhub": [pornhub, "https://www.pornhub.com"]
    }

if platform.system() == "Windows":
    os.system("color FF")  # Fixes colour in Windows 10 CMD terminal.

def porncli():  # TODO add regex
    try:
        provider = ask()
        provider_data = calls.get(provider, calls["pornhub"])
        provider:WebScraper = provider_data[0](provider_data[1])
                # provider.redo(query) if query is not None else provider.redo()
        provider.redo()  # if result else provider.redo(query)
    except UnicodeDecodeError:
        print("[!] The Current Key is not correct, please wait.")
if __name__ == '__main__':
    porncli()
