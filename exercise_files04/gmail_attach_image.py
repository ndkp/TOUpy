##############################
#プログラムの解説(1)

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import my_gmail_account as my #アカウント情報の読み込み
import gmail_send #第2講冒頭で説明したプログラム

#メールデータを作成
msg = MIMEMultipart()
msg["Subject"] = "画像の送信テスト"
msg["To"] = my.account
msg["From"] = my.account

##############################
#プログラムの解説(2)

#テキストパートの追加
txt = MIMEText("東京通信大学のロゴ画像です。\n届きましたか？")
msg.attach(txt)

#画像パートの追加
fname = "tou_logo.jpg"
with open(fname, "rb") as fp:
    img = MIMEImage(fp.read(), Name=fname)
    msg.attach(img)

#メールの送信
gmail_send.send_gmail(msg)
print("done")
