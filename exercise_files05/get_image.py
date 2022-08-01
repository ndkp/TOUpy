import requests
import urllib

#画像ファイルの絶対パスを生成し、画像を取得する
base_url = "http://tsuchiya128.html.xdomain.jp/sample2.html"
img_src = "image/tou_logo.jpg"
img_url = urllib.parse.urljoin(base_url, img_src)
img_data = requests.get(img_url)

#画像のファイル名を取得する
filename = img_url.split("/")[-1]

#画像データをファイルに書き出す
with open(filename, mode="wb") as fp:
    fp.write(img_data.content)
