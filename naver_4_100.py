import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

clips = html.select("div.cds")
# print(clips[0])
# 컨테이너 소스코드는 주석처리해줍니다.

for i in range(len(clips)):
    title = clips[i].select_one("dt.title")
    chn = clips[i].select_one("dd.chn")
    hit = clips[i].select_one("span.hit")
    like = clips[i].select_one("span.like")

    print(i+4,"위")
    print("제목 ", title.text.strip())
    print("채널명 ", chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)