import tweepy
import time
import datetime
import read_write_json_data

def open_config(filename):
    with open(filename,"r") as infile:
        configtext = infile.read()
    config = {}
    for configrule in configtext.split("\n"):
        if len(configrule.split(": ")) > 1:
            key,value = configrule.split(": ")
            config[key] = value
    return config

# todo: handle StopIteration properly
def limithandled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("[",datetime.datetime.now(),"]","RateLimitError, sleeping for 15 minutes...")
            time.sleep(15*60)
        except tweepy.TweepError as e:
            print("[",datetime.datetime.now(),"]","TweepError",type(e),repr(e),"sleeping for 15 minutes...")
            time.sleep(15*60)
        except Exception as e:
            print("[",datetime.datetime.now(),"]","Unknown error:", type(e), repr(e))

def query_twitter(api):
    search_string = "media.ccc.de/v/33c3"
    temp_results_filename = "last_query_results.data"
    results = []
    processed_tweets = 0
    interval = 60
    
    for status in limithandled(tweepy.Cursor(api.search, q=search_string).items()):
        status_json = status._json
        datapoint = {}
        datapoint["tweet_id"], datapoint["tweet_time"], datapoint["nr_of_retweets"] = status_json["id"], status_json["created_at"], status_json["retweet_count"]
        datapoint["media_urls"] = [url["expanded_url"] for url in status_json["entities"]["urls"] if search_string in url["expanded_url"]]
        if len(datapoint["media_urls"]) > 0:
            results.append(datapoint)

        processed_tweets+=1
        if processed_tweets < interval:
            print("Processed tweet",status_json["id"])
        if processed_tweets > 0 and processed_tweets % interval == 0:
            print(processed_tweets,"processed so far.")
            write_data(results,temp_results_filename)

    write_data(results,temp_results_filename)
    print(len(results),"written to",temp_results_filename)
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

    '''
    # poc 3: extract metadata and media.ccc.de urls from tweets
    query_results = query_twitter(api)
    #original_tweets = [tweet._json for tweet in query_result if "retweeted_status" not in tweet._json.keys()]
    original_tweets = [tweet._json for tweet in query_result]
    results = []
    for ot in original_tweets:
        datapoint = {}
        datapoint["tweet_id"], datapoint["tweet_time"], datapoint["nr_of_retweets"] = ot["id"], ot["created_at"], ot["retweet_count"]
        datapoint["media_urls"] = [url["expanded_url"] for url in ot["entities"]["urls"] if "media.ccc/v/33c3" in url["expanded_url"]]
        if len(datapoint["media_urls"]) > 0:
            results.append(datapoint)
            for key in ["tweet_id", "tweet_time", "nr_of_retweets", "media_urls"]:
                print(datapoint[key],"")
            print()

    write_data(results,"results.data")

    highest_id = 0
    for r in results:
        if r["tweet_id"] > highest_id:
            highest_id = r["tweet_id"]

    print("Highest tweet id:",highest_id)

    return query_result,results
    '''

    #poc 4: use cursor

    query_results = query_twitter(api)
    return query_results

if __name__ == "__main__":
    main()

