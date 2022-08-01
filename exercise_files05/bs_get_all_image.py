import requests
from bs4 import BeautifulSoup
import urllib

#Webページを取得して解析する
url = "http://tsuchiya128.html.xdomain.jp/sample2.html"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

#すべてのimgタグを検索し、リンクを取得する
for element in soup.find_all("img"):
    img_src = element.get("src")
    #絶対URLを作成して、画像データを取得する
    img_url = urllib.parse.urljoin(url, img_src)
    img_data = requests.get(img_url)
    #絶対URLからファイル名を取り出す
    filename = img_url.split("/")[-1]
    #画像データをファイルに書き出す
    with open(filename, mode="wb") as fp:
        fp.write(img_data.content)
