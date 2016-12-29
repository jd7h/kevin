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

def __main__():
    config = open_config("twitterauth.conf")
    print(config)
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_token_key"], config["access_token_secret"])

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)


if __name__ == "__main__":
    main()

