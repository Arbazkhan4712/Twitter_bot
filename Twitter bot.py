import tweepy

auth = tweepy.OAuthHandler(API key , API secret key)
auth .set_access_token(Access token,Access token secret )
api = tweepy.API(auth)

print("done")

def reply():
    tweets = api.home_timeline()
    for tweet in tweets:
        print(tweet.text)

def update_status():
    api.update_status("ADD THE STATUS YOU WANT!")

def get_tweets():
    api.user_timeline()

def replynewtweets():
    tweets = api.user_timeline(screen_name="addusername")
    firt_tweet = tweets[0]
    print(firt_tweet.text)
    print("done")
    api.update_status('@addusername cool this is response from AI JARVIS bot', firt_tweet.id)
