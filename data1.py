import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.vlive.tv")
#print(raw.text)

html = BeautifulSoup(raw.text, "html.parser")
#print(html)

clips = html.select("div.content")
print(clips[9])