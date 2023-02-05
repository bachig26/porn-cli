import re

import httpx
from bs4 import BeautifulSoup as BS

def parse(text: str) -> str:
    return re.sub(r"\W+", "-", text.lower())
