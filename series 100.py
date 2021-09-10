#series 100.py

import requests
from bs4 import BeautifulSoup
for n in range(1,6):
    raw = requests.get("https://series.naver.com/ebook/top100List.series?page=1"+str(n),
                   headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, "html.parser")
    section = html.select("ul.lst_thum.v1>li")
    for sec in section:
        title = sec.select_one("strong").text
        author = sec.select_one("span.writer").text
        print(title, author)