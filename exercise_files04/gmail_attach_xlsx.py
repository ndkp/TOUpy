##############################
#プログラムの解説(1)

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

import my_gmail_account as my #アカウント情報の読み込み
import gmail_send #第2講冒頭で説明したプログラム

#メールデータを作成
msg = MIMEMultipart()
msg["Subject"] = "Excelファイルの送信テスト"
msg["To"] = my.account
msg["From"] = my.account

##############################
#プログラムの解説(2)

#テキストパートの追加
txt = MIMEText("Excelファイルです。\n届きましたか？")
msg.attach(txt)

#Excelファイルパートの追加
fname = "send_test.xlsx"
with open(fname, "rb") as fp:
    excel = MIMEApplication(fp.read(),Name=fname)
    msg.attach(excel)

#メールの送信
gmail_send.send_gmail(msg)
print("done")
