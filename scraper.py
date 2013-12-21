import twitter
import pymongo

# Read the twitter api keys from local file
fname = '/twitterKeys.txt'
with open(fname) as f:
    content = f.read().splitlines()

    consumerKey = content[0]
    consumerSecret = content[1]
    consumerAccessTokenKey = content[2]
    consumerTokenSecret = content[3]

# connect to Mongo
client = pymongo.MongoClient()
twitterDB = client.local.twitterData

# connect to Twitter
api = twitter.Api(consumer_key=consumerKey,
                  consumer_secret=consumerSecret,
                  access_token_key=consumerAccessTokenKey,
                  access_token_secret=consumerTokenSecret)

# Get Tweets
tweets = api.GetSearch(term="hadoop")

# Get desired data and write to Mongo
for t in tweets:
    mydata = {
        'id': t.id,
        'retweet_count': t.retweet_count,
        'text': t.text,
        'user': {'screenname': t.user.screen_name,
                 'follower_count': t.user.followers_count,
                 }
    }
    twitterDB.insert(mydata)