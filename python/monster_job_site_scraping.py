#! /usr/bin/env python3

import requests
import pprint
from bs4 import BeautifulSoup

URL = "https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia"
page = requests.get(URL)
print(page.content)
# soup = BeautifulSoup(page.content, 'html.parser')

# result = soup.select("div", class_="results-card")
# print(result[0])
# print(f"results count: {len(result)}")