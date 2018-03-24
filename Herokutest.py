# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

consumer_key = "RAuPj1XAJbOw2Oq8ADItKeK3n"
consumer_secret = "UwW81r9QKb0VIPKp7jRs3855UCti3oYg26C04ribEYafhR19eQ"
access_token = "975022187978678272-jTa7voYgvIHAYQZnqfipZpADheYW6RB"
access_token_secret = "aVX3B7B35FLG9yIUHOm8ro7RxS19TcFkwaUoEhY3zJiyD"

# Loop through all tweets
tweet_num =1
while tweet_num <6 :
    api.update_status("tweet num " + str(time.ctime()) + "counter " + str(tweet_num))
    tweet_num  = tweet_num + 1
    time.sleep(60)