import tweepy
import time
import secure as s

auth = tweepy.OAuthHandler(s.CONSUMER_KEY, s.CONSUMER_SECRET)
auth.set_access_token(s.OAUTH_KEY, s.OAUTH_SECRET)
api = tweepy.API(auth)


class Listener(tweepy.StreamListener):
    def on_status(self, status):
        if "RT" not in status.text:
            try:
                new = api.update_status(status=u"\U0001F692" + " No fire tweets please @" + status.author.screen_name,
                                        in_reply_to_status_id=status.id)
                print("https://twitter.com/NoFireTweetsPls/status/" + str(new.id))
                time.sleep(100)
            except tweepy.error.TweepError as e:
                print(e.response)

listener = Listener()
twitterStream = tweepy.Stream(auth=auth, listener=listener)
twitterStream.filter(track=[u"\U0001F525"], languages=["en"])
