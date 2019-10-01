#!C:\Users\thoma\AppData\Local\Programs\Python\Python37-32\python.exe
print ("Content-Type: text/html")
print()
import cgi
import tweepy
from tweepy import OAuthHandler
import json

def twitter_setup():
    ''' Function that loads the twitter API after authorizing the user. '''

    consumer_key = "YrLjiZMn18IxX5SW3mZYKCemj" 
    consumer_secret = "nheGQ0jg3ZuQqqF1SO2ggNK4HEgPCSeXftp09k1FNzuUvmsuC8"
    access_key = "2278806824-tBFPDblG2MAJFPRGXA4rRrcZUQVreEjcdtOccBg"
    access_secret = "WeyaLWK9DEa0xhvsj24lSqvylGbxB80CxUIekOWsndwRu"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    # load the twitter API via tweepy
    return tweepy.API(auth)

# Mention the maximum number of tweets that you want to be extracted.
form=cgi.FieldStorage()


maximum_tweets= 2
#int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for
hashtag=form.getvalue('t2')
#hashtag = input('Enter the hashtag you want to scrape- ')

#user = 'ronaldo'

extractor = twitter_setup()
tweets = extractor.search(q="#"+hashtag, count=maximum_tweets)
#tweets = api.user_timeline(id=user, count=5)
print('Found %d tweets' % len(tweets))

# You now have a list of tweet objects with various attributes
# check out the structure here: http://tkang.blogspot.ca/2011/01/tweepy-twitter-api-status-object.html

# For example we can get the text of each tweet
tweets_text = [t.text for t in tweets]
filename = 'tweets-'+hashtag+'.json'
json.dump(tweets_text, open(filename, 'w'))
print('Saved to file:', filename)

with open(filename,'r') as fip:
    cfile=json.load(fip)
    print('\n')
    print(cfile)

# Can load file like this
#tweets_text = json.load(open(filename, 'r'))
