import requests

# 対象のURL
url = 'https://accounts.google.com/ServiceLogin?service=youtube'

# GETリクエストを送信
response = requests.get(url)

# クッキーを取得
cookies = response.cookies

# クッキーを表示
for cookie in cookies:
    print(f'Name: {cookie.name}, Value: {cookie.value}')
