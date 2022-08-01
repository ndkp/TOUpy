import tweepy

#Twitter APIの認証情報
api_key = "xxxxxx"
api_secret = "xxxxxx"
access_token = "xxxxxx"
access_secret = "xxxxxx"

#Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#任意のメッセージを投稿
api.update_status("こんにちは。初めての投稿です。")
