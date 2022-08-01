##############################
#プログラムの解説(1)

import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as my #アカウント情報の読み込み

##############################
#プログラムの解説(2)

#メイン処理
def send_test_email():
    #メールデータ(MIME形式)を作成
    msg = make_mime(
        mail_to = my.account,
        subject = "メールの送信テスト",
        body = "メールは届きましたか？")
    #メール送信
    send_gmail(msg)

#メールデータ(MIMEオブジェクト)を生成する
def make_mime(mail_to, subject, body):
    msg = MIMEText(body, "html")
    msg["Subject"] = subject     #件名
    msg["To"] = mail_to          #宛先
    msg["From"] = my.account     #送信元
    return msg

##############################
#プログラムの解説(3)

#Gmailでメールを送信する
def send_gmail(msg):
    # Gmailサーバーに接続
    server = smtplib.SMTP_SSL(
        "smtp.gmail.com", 465,
        context=ssl.create_default_context())
    server.set_debuglevel(0) #ログ出力
    #ログインしてメールを送信
    server.login(my.account, my.password)
    server.send_message(msg)

#メインプログラムを実行
if __name__ == "__main__":
    send_test_email()
    print("send to:", my.account)
