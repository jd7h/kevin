import tweepy

def open_config(filename):
    with open(filename,"r") as infile:
        configtext = infile.read()
    config = {}
    for configrule in configtext.split("\n"):
        if len(configrule.split(": ")) > 1:
            key,value = configrule.split(": ")
            config[key] = value
    return config

def query_twitter(api):
    search_string = "media.ccc.de/v/33c3"
    results = api.search(search_string)
    return results

def main():
    config = open_config("twitterauth.conf")
    print(config)
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_token_key"], config["access_token_secret"])

    api = tweepy.API(auth)

    ''' 
    # poc 1
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
    '''

    '''
    # poc 2: print followers
    def limit_handled(cursor):
        while True:
            try:
                yield cursor.next()
            except tweepy.RateLimitError:
                print("Rate limit encountered!")
                time.sleep(15 * 60)

    for follower in limit_handled(tweepy.Cursor(api.followers).items()):
        if follower.friends_count < 300:
            print(follower.screen_name)
    '''

    # poc 3: extract metadata and media.ccc.de urls from tweets
    results = query_twitter(api)
    original_tweets = [tweet._json for tweet in results if "retweeted_status" not in tweet._json.keys()]
    for ot in original_tweets:
        tweet_id, tweet_time, retweets = ot["id"], ot["created_at"], ot["retweet_count"]
        media_urls = [url["expanded_url"] for url in ot["entities"]["urls"] if "media.ccc" in url["expanded_url"]]
        print(tweet_id, tweet_time, retweets, media_urls)
    print("Done.")

    return results 


if __name__ == "__main__":
    main()

