import tweepy # pip install tweepy

auth = tweepy.OAuthHandler(API key , API secret key)
auth .set_access_token(Access token,Access token secret )
api = tweepy.API(auth)

print("done")

def get_tweets():
    tweets = api.home_timeline()
    for tweet in tweets:
        print(tweet.text)

def update_status():
    api.update_status("ADD THE STATUS YOU WANT!")

def reply_new_tweets(): # it will reply to retweets as well
    user_name = input(print("Enter User Name to reply"))
    tweets = api.user_timeline(screen_name=user_name)
    firt_tweet = tweets[0]
    print(firt_tweet.text)
    print("done")
    api.update_status('@{} cool this is response from AI JARVIS bot'.format(user_name), firt_tweet.id)

def reply_with_media(): # it will reply to retweets as well
    user_name = input(print("Enter User Name to reply"))
    filename = input(print("Enter the file name"))
    tweets = api.user_timeline(screen_name=user_name)
    firt_tweet = tweets[0]
    print(firt_tweet.text)
    print("done")
    api.update_status(filename,'@{} cool this is response from AI JARVIS bot'.format(user_name), firt_tweet.id) #add the file name 

def no_retweet(): # it will not reply to retweets
    user_name = input(print("Enter User Name to reply"))
    tweets = api.user_timeline(screen_name=user_name)
    for tweet in tweets:
        if tweet.text[0:2] != "RT":
            api.update_status('@{} cool this is response from AI JARVIS bot'.format(user_name), firt_tweet.id)


def no_retweet_with_media(): # it will not reply to retweets 
    user_name = input(print("Enter User Name to reply"))
    filename = input(print("Enter the file name"))
    tweets = api.user_timeline(screen_name=user_name)
    for tweet in tweets:
        if tweet.text[0:2] != "RT":
            firt_tweet = tweets[0]
            print(firt_tweet.text)
            print("done")
            api.update_status(filename,'@{} cool this is response from AI JARVIS bot'.format(user_name), firt_tweet.id) #add the file name 

if  __name__ == "__main__":
    a = input(print("Press 1 to Get All Tweets \n Press 2 to Reply To All Tweets & Retweets \n Press 3 to Reply To Tweets & Retweets With Media \n Press 4 to Reply To Only Tweets No Retweet \n Press 5 to Reply To Only Tweets with Media No Retweet \n  Press 6 to Update Status\n"))
    if a == 1:
        get_tweets()
    elif a == 2:
        reply_new_tweets()
    elif a == 3:
        reply_with_media()
    elif a == 4:
        no_retweet()
    elif a == 5:
        no_retweet_with_media()
    elif a == 6:
        update_status()
    else:
        print("Invalid Input")
        print("Press 1 to Get All Tweets \n Press 2 to Reply To All Tweets & Retweets \n Press 3 to Reply To Tweets & Retweets With Media \n Press 4 to Reply To Only Tweets No Retweet \n Press 5 to Reply To Only Tweets with Media No Retweet \n  Press 6 to Update Status\n")
