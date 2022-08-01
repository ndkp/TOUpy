import requests

#Webページの取得
url = "http://tsuchiya128.html.xdomain.jp/sample1.html"
response = requests.get(url)

#文字化けをしないようにする
response.encoding = response.apparent_encoding

print(response.text)
