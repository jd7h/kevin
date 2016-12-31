import tweepy
import time
import datetime
import read_write_json_data as rw

def open_config(filename):
    with open(filename,"r") as infile:
        configtext = infile.read()
    config = {}
    for configrule in configtext.split("\n"):
        if len(configrule.split(": ")) > 1:
            key,value = configrule.split(": ")
            config[key] = value
    return config

def limithandled(cursor):
    found_everything = False
    strange_error = False
    while not found_everything and not strange_error:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("[",datetime.datetime.now(),"]","RateLimitError, sleeping for 15 minutes...")
            time.sleep(15*60)
        except tweepy.TweepError as e:
            print("[",datetime.datetime.now(),"]","TweepError",type(e),repr(e),"sleeping for 15 minutes...")
            time.sleep(15*60)
        except StopIteration:
            found_everything = True
        except Exception as e:
            print("[",datetime.datetime.now(),"]","Unknown error:", type(e), repr(e))
            strange_error = True

def status_to_datapoint(search_string,status,results):
    status_json = status._json
    datapoint = {}
    datapoint["tweet_id"], datapoint["tweet_time"], datapoint["nr_of_retweets"] = status_json["id"], status_json["created_at"], status_json["retweet_count"]
    media_urls = [url["expanded_url"] for url in status_json["entities"]["urls"] if search_string in url["expanded_url"]]
    if len(media_urls) == 1:
        datapoint["media_urls"] = media_urls[0]
        results.append(datapoint)
    if len(media_urls) > 1:
        for url in media_urls:
            datapoint["media_urls"] = url
            results.append(datapoint)
    return results

def query_twitter(api,search_string="media.ccc.de/v/32c3",newer_than_id=0):
    temp_results_filename = "last_query_results.data"
    results = []
    processed_tweets = 0
    interval = 100
    
    if newer_than_id != 0:
        cursor = tweepy.Cursor(api.search, q=search_string, since_id=newer_than_id).items()
    else:
        cursor = tweepy.Cursor(api.search, q=search_string).items()
    for status in limithandled(cursor):
        results = status_to_datapoint(search_string,status,results)

        processed_tweets+=1
        if len(results) > 0 and processed_tweets < interval:
            print("Processed tweet",status._json["id"])
        if processed_tweets > 0 and processed_tweets % interval == 0:
            print(processed_tweets,"processed so far.")
            if newer_than_id == 0:
                rw.write_data(results,temp_results_filename)

    if newer_than_id != 0:
        rw.append_data(results,temp_results_filename)
    else:
        rw.write_data(results,temp_results_filename)
    return results

class StdOutListener(tweepy.StreamListener):
    def on_status(self, data):
        print(data)
        return True

    def on_error(self, data):
        print(data)

def query_streaming_api(api, search_string="33c3"):
    # source: http://docs.tweepy.org/en/v3.5.0/streaming_how_to.html
    l = StdOutListener()
    stream = tweepy.Stream(api.auth, l)

    stream.filter(track=[search_string])


def main():
    config = open_config("twitterauth.conf")
    #print(config)

    # source: http://docs.tweepy.org/en/v3.5.0/getting_started.html
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_token_key"], config["access_token_secret"])

    api = tweepy.API(auth)
    # query_streaming_api(api)
    return api

if __name__ == "__main__":
    main()

