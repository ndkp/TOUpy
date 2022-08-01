import requests
from bs4 import BeautifulSoup

#Webページ（html）の取得
url = "https://news.yahoo.co.jp/"
html = requests.get(url)

#Beautiful Soupを使って解析する
soup = BeautifulSoup(html.content, "html.parser")

#classが「sc-hCbubC gGvaw」であるタグを検索する
news = soup.find(class_="sc-hCbubC gGvaw")
#その中に含まれるすべてのliタグの一覧を取得する
for element in news.find_all("li"):
    topic = element.text
    link = element.find("a").get("href")
    print(topic, link)
