import requests
from bs4 import BeautifulSoup

#Webページ（html）の取得
url = "http://tsuchiya128.html.xdomain.jp/sample1.html"
html = requests.get(url)

#Beautiful Soupを使って解析する
soup = BeautifulSoup(html.content, "html.parser")

#titleタグ、h1タグ、strongタグを検索して文字列だけを表示する
print(soup.find("title").text)
print(soup.find("h1").text)
print(soup.find("strong").text)
