import tweepy

app_api_key = "57D1EUdoiDrTKo5nNLRYQ"
app_api_secret = "cpJzglxNHkbFX6gRKCBFVV8iey6gKzbUdqjE9xo"
user_key = '1523651013533892610-RDPv3pYJEMKyICOeADzbOZ9aQ7f1mH'
user_secret = 'ATsUam8MaiSBPZg8ZikLKldoDgWvqWmuJm7fWwcAAjC6r'

auth = tweepy.OAuthHandler(app_api_key, app_api_secret)
auth.set_access_token(user_key, user_secret)
# auth_url = auth.get_authorization_url()
# print(auth_url)
# pinCode = input("pin : ") #입력값을 넣을때까지 대기하는 함수
# goldenkey = auth.get_access_token(pinCode)
# print(goldenkey)

api = tweepy.API(auth)

result = api.search_tweets(q = "BTS", count = 100) # 특정 단어 검색
# api.user_timeline(screen_name="") # 특정 계정의 글 수집
# api.get_followers_ids(screen_name = "")# 특정 계정의 팔로워들 수집

# for tweetObj in result:
#     tweetid = tweetObj.id  #트윗글번호
#     tweetCreated = tweetObj.created_at #작성시간
#     authorObject = tweetObj.author #작성자 정보
#     authorName = authorObject.screen_name #id
#     tweeetText = tweetObj.text.replace("\n", "") #글 내용
#     print(tweetid,tweetCreated,authorName,tweeetText)

#cursor을 이용해서 트윗을 페이지로 수집

for tweetObj in tweepy.Cursor(api.search_tweets, q ="BTS", count= 100).items():
    tweetid = tweetObj.id  #트윗글번호
    tweetCreated = tweetObj.created_at #작성시간
    authorObject = tweetObj.author #작성자 정보
    authorName = authorObject.screen_name #작성자
    tweeetText = tweetObj.text.replace("\n", "") #글 내용
    print(tweetid, tweetCreated, authorName, tweeetText)

