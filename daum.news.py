#daum.news.py
import requests
from bs4 import BeautifulSoup
for n in range(1, 10):
    raw = requests.get("https://search.daum.net/search?nil_suggest=btn&w=news&DA=PGD&q=%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8&p=1"+str(n))
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.list_news>li")
    for art in articles:
        title = art.select_one("a.tit_main.ff_dot").text
        source = art.select_one("span.f_nb").text
        print(title, source)