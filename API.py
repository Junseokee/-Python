import tweepy

app_api_key = "57D1EUdoiDrTKo5nNLRYQ"
app_api_secret = "cpJzglxNHkbFX6gRKCBFVV8iey6gKzbUdqjE9xo"
user_key = '1523651013533892610-RDPv3pYJEMKyICOeADzbOZ9aQ7f1mH'
user_secret = 'ATsUam8MaiSBPZg8ZikLKldoDgWvqWmuJm7fWwcAAjC6r'

auth = tweepy.OAuthHandler(app_api_key, app_api_secret)
auth.set_access_token(user_key, user_secret)

api = tweepy.API(auth)

tweet0bjList  = api.search_tweets(q =u "아이폰") # 특정 단어 검색

api.user_timeline(screen_name="") # 특정 계정의 글 수집
api.get_followers_ids(screen_name = "")# 특정 계정의 팔로워들 수집
for i in tweet0bjList:
    tweetStr = tweet0bj.text
    tweetStr = tweetStr.replace("\n","")
    print(tweetStr)

# auth_url = auth.get_authorization_url()
# print(auth_url)
# pinCode = input("pin : ") #입력값을 넣을때까지 대기하는 함수
# goldenkey = auth.get_access_token(pinCode)
# print(goldenkey)


