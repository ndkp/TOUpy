from email.mime.text import MIMEText
import my_gmail_account as my #アカウント情報の読み込み
import gmail_send #第2講冒頭で説明したプログラム

#HTMLの作成
html = """
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <h1>HTMLの利用</h1>
    <p>HTMLを利用することで、テキストの
    <strong>装飾</strong>が可能になります。<br>
    ぜひ試してみてください。</p>
</body>
</html>
"""

#メールデータをHTMLで作成
msg = gmail_send.make_mime(
    mail_to = my.account,
    subject = "HTMLメールの送信テスト",
    body = html)

#メール送信
gmail_send.send_gmail(msg)
print("done")
