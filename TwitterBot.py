"""
    Twitter Bot 
    Sign up for a developer twitter account(this will take some time for twitter to review your application)
    Get Started
    Create an app
    You need 4 keys to access the Twitter API
        consumer_key
        consumer_secret
        access_token
        access_token_secret
    Library to access twitter api: Tweepy https://www.tweepy.org/
    
# exception RateLimitError

    Is raised when an API method fails due to hitting Twitter’s rate limit.
    Makes for easy handling of the rate limit specifically.

    Inherits from TweepError, so except TweepError will catch a RateLimitError too.

# Hello Tweepy
    
    import tweepy

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)

    user = api.me() # get information about myself
    print(user.name) # prints my name
    print(user.screen_name)
    print(user.followers_count)


    def limit_handler(cursor):
        try:
            while True:
                yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000) # 1 second

    # Generous Bot 🤖🤖🤖
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if follower.name == 'some_person_twitter_name':
            follower.follow() # help me to follow this person
            break
        --OR--
        if follower.followers_count > 100:
            follower.follow() # help me to follow this person
            break
        # print(follower.name)
    
    # Narcisist Bot 🤖🤖🤖(Loves his own Tweets)
    search_string = 'python'
    number_of_tweets = 2

    for tweet in tweepy.Cursor(api.search, search_string).items(number_of_tweets):
        try:
            tweet.favorite()
            # tweet.retweet()
            print('I liked that tweet :)')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIterationError:
            break    
"""
import tweepy
import time
"""
I don't know if my code works because i could't tested
"""

