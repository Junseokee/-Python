import tweepy

app_api_key = "57D1EUdoiDrTKo5nNLRYQ"
app_api_secret = "cpJzglxNHkbFX6gRKCBFVV8iey6gKzbUdqjE9xo"
user_key = '1523651013533892610-RDPv3pYJEMKyICOeADzbOZ9aQ7f1mH'
user_secret = 'ATsUam8MaiSBPZg8ZikLKldoDgWvqWmuJm7fWwcAAjC6r'
auth = tweepy.OAuthHandler(app_api_key, app_api_secret)
# auth_url = auth.get_authorization_url()
# print(auth_url)
# pinCode = input("pin : ") #입력값을 넣을때까지 대기하는 함수
# goldenkey = auth.get_access_token(pinCode)
# print(goldenkey)
auth.set_access_token(user_key, user_secret) #Access Token

api = tweepy.API(auth) # 키값 저장


tweet0bjList = api.search_tweets(q = "우크라이나") # 특정 단어 검색

for tweet0bj in tweet0bjList:
    tweetStr = tweet0bj.text
    tweetStr = tweetStr.replace("\n","")
    print(tweetStr)
