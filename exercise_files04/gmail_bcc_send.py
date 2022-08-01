from email.mime.text import MIMEText
import my_gmail_account as my #アカウント情報の読み込み
import gmail_send #第2講冒頭で説明したプログラム

#メールデータの作成
text = "BCCのテストです<br>メールは届きましたか？"
msg = MIMEText(text, "html")
msg["Subject"] = "BCCのテスト"
msg["To"] = ""
msg["From"] = my.account
msg["Bcc"] = my.account

#メール送信
gmail_send.send_gmail(msg)
print("done")
