from bs4 import BeautifulSoup
import requests

maximum = 0
page = 1

url = "https://finance.naver.com/news/market_notice.nhn"
response = requests.get(url)
source = response.text
soup = BeautifulSoup(source, "html.parser")

last_page_a = soup.find("td", {"class":"pgRR"})
value = last_page_a.find("a").get("href")
maximum = value.split("=")[1]

print("총 " + str(maximum) + " 개의 페이지가 확인 되었습니다.")

whole_source = ""
for page_number in range(1, 2):
    url = "https://finance.naver.com/news/market_notice.nhn?&page=" + str(page_number)
    response = requests.get(url)
    whole_source = whole_source + response.text
    
soup = BeautifulSoup(whole_source, "html.parser")

find_title = soup.select("#contentarea_left > div.boardList2 > table > tr > td.publicSubject > a")
for title in find_title:
    print(title.text)