import requests
import re
from bs4 import BeautifulSoup

URL = "https://imsdb.com/scripts/12-and-Holding.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
script = soup.find('pre')

print(script.text.strip())
