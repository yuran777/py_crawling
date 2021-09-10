import requests
from bs4 import BeautifulSoup
f = open("naver_news2.csv", "w", encoding = "utf-8-sig" )
f.write("title, source" + "\n")

for n in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8&sm=tab_opt&sort=0&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0"+str(n))
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.list_news> li")
    for art in articles:
        title = art.select_one("a.news_tit").text
        source = art.select_one("a.info.press").text

        title = title.replace(",", "")
        source = source.replace(",", "")
        print(title, source)
        f.write(title + "," + source + "\n" )

f.close()
