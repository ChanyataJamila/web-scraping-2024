import requests
from bs4 import BeautifulSoup
import re

ryoii ="https://www.ryoiireview.com/review/"

# Fake browser-like headers
#BASE_HEADES = {
    #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    #"Accept": "application/x-clarity-gzip",
    #"Accept-Encoding": "gzip, deflate, br, zstd",
    #"Accept-Language": "en-US,en;q=0.9",
#}

#response = requests.get(ryoii, headers=BASE_HEADES)

page = requests.get(ryoii)
soup = BeautifulSoup(page.content, "html.parser")
content = soup.find_all(class_ = "caption")
print(content)
