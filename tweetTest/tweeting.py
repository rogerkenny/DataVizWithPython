import tweepy

creds = open("CRED.txt", "r")

consumer_key, consumer_secret = creds.readline().strip(), creds.readline().strip()
access_token, access_token_secret = creds.readline().strip(), creds.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)