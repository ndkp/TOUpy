##############################
#プログラムの解説(1)

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import my_gmail_account as my #アカウント情報の読み込み
import gmail_send #第2講冒頭で説明したプログラム

#メールデータを作成
msg = MIMEMultipart()
msg["Subject"] = "ZIPファイルの送信テスト"
msg["To"] = my.account
msg["From"] = my.account

##############################
#プログラムの解説(2)

#テキストパートの追加
txt = MIMEText("演習用ファイル一式です。\n届きましたか？")
msg.attach(txt)

#ZIPファイルパートの追加
fname = "04_exercise_files.zip"
zip_part = MIMEBase("application", "zip")
with open(fname, "rb") as fp:
    zip_part.set_payload(fp.read())
encoders.encode_base64(zip_part)
zip_part.add_header("Content-Disposition",
    "attachment", filename=fname)
msg.attach(zip_part)

#メールの送信
gmail_send.send_gmail(msg)
print("done")
