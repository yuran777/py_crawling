import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active 

sheet.title = "1st"
sheet2 = wb.create_sheet("2nd")

sheet .append(["title", "channel", "play", "like"])

raw = requests.get("https://tv.naver.com/r")
html = BeautifulSoup(raw.text, "html.parser")

# 1위 - 100위 컨테이너 선택자: dl.cds_info
clips = html.select("dl.cds_info")

for cl in clips:
    # 수정된 부분
    title = cl.select_one("dt.title").text.strip()
    chn = cl.select_one("dd.chn").text.strip()
    hit = cl.select_one("span.hit").text.strip()
    like = cl.select_one("span.like").text.strip()

    print("제목", title)
    print("채널명", chn)
    print(hit)
    print(like)
    print("="*50)

    sheet.append([title, chn, hit, like])
    sheet2.append([title, like])

wb.save("naver_Tv.xlsx")
