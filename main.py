import tweepy
import json
import time
import secure as s

auth = tweepy.OAuthHandler(s.CONSUMER_KEY, s.CONSUMER_SECRET)
auth.set_access_token(s.OAUTH_KEY, s.OAUTH_SECRET)
api = tweepy.API(auth)


class Listener(tweepy.StreamListener):
    def on_data(self, data):
        js = json.loads(data)
        if "RT" not in js["text"]:
            print("Tweet: " + js["text"])
            print("Tweet URL: http://twitter.com/" + js["user"]["screen_name"] + "/status/" + str(js["id"]))
            try:
                api.update_status(u"\U0001F692" + " No fire tweets please @" +
                                  js["user"]["screen_name"], in_reply_to_status_id=js["id"])
                print("Tweeted @" + js["user"]["screen_name"] + "\n\n")
                time.sleep(87)
            except tweepy.TweepError:
                print("API ERROR:")
                print(tweepy.TweepError)
                print("\n\n")
                time.sleep(87)
        return True

    def on_error(self, status):
        print("STREAM ERROR: " + str(status))


twitterStream = tweepy.Stream(auth, Listener())
while True:
    try:
        twitterStream.filter(track=u"\U0001f525", languages="en")
    except:
        print("BASIC ERROR")
        continue
