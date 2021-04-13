CONSUMER_KEY = 
CONSUMER_SECRET = 
ACCESS_TOKEN = 
ACCESS_TOKEN_SECRET = 

from requests_oauthlib import OAuth1Session
from time import sleep
import json
#４つのキーをセット
CK = CONSUMER_KEY
CS = CONSUMER_SECRET
AT = ACCESS_TOKEN
ATS = ACCESS_TOKEN_SECRET
 
# 対象ツイートを検索
def search_tweet(search_word):
    url = "https://api.twitter.com/1.1/search/tweets.json"
    twitter = OAuth1Session(CK, CS, AT, ATS)
    req = twitter.get(url, params = search_word)
 
    if req.status_code == 200:
        tweet = json.loads(req.text)
        search_timeline = json.loads(req.text)
        for tweet in search_timeline['statuses']:
            print(tweet['user']['screen_name'] + "(" + tweet['user']['name'] + ") > " + tweet['text'])
            print("(tweet id = " + tweet['id_str'] + ")")
            print("-"*10)
            return tweet['id'] 
    else:
        print("ERROR: %d" % req.status_code)

# いいね        
def favorite_tweet(tweet_id):
    url = "https://api.twitter.com/1.1/favorites/create.json"
    params = {'id' : tweet_id,
             #'include_entities' : 'True'
             }
    twitter = OAuth1Session(CK, CS, AT, ATS)
    req = twitter.post(url, params = params)
    
    if req.status_code == 200:
        print('↑のツイートを いいね しました')
        print("-・"*30)
    else:
        print("ERROR: %d" % req.status_code)
        print("-・"*30)

        if __name__ == '__main__':
    count = 10
    tweet_id = 9999999999999999999
    for i in range(count):
        #print(tweet_id)
        search_word = {'q' : "#########",  #検索文字列
                       'count':1,
                       'lang' : 'ja', 
                       'result_type' : 'recent',
                       'max_id' : str(tweet_id-1)
                       }
        tweet_id = search_tweet(search_word)
        favorite_tweet(tweet_id)
        if not i==count-1: sleep(60)
 
print("finish")