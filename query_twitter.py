import tweepy
import time
import datetime
import read_write_json_data as rw
import json
import re

def write_dataset(dataset,filename):
    with open(filename,"w") as outfile:
        outfile.write(json.dumps(dataset))

def read_dataset(filename):
    with open(filename,"r") as infile:
        dataset = json.loads(infile.read())
        return dataset

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

def clean_url(dirty_url):
    # ugly hardcoded, works for now
    regexp = "[^ \?\=\#\t\n\r\f\v\\\]*media\.ccc\.de[^ \?\=\#\t\n\r\f\v\\\]*"
    matches = re.findall(regexp, dirty_url)
    if len(matches) == 0:
        return "BADURL: " + dirty_url
    elif len(matches) == 1:
        return matches[0]
    else:
        return "ERROR: multiple matches: " + str(matches)

def status_to_datapoint(search_string,status):
    datapoint = {}
    datapoint["tweet_id"] = status["id"]
    datapoint["tweet_time"] = status["created_at"]
    datapoint["nr_of_retweets"] = status["retweet_count"]
    datapoint["status"] = status

    expanded_urls = [clean_url(url["expanded_url"]) for url in status["entities"]["urls"]]
    expanded_urls = [url for url in expanded_urls if not "BADURL" in url and not "ERROR" in url]
    datapoint["media_urls"] = expanded_urls
    return datapoint

def process_dataset(search_string, dataset):
    temp_results_filename = "last_clean_results.data"
    results = []
    processed_tweets = 0
    interval = 100
    
    for status in dataset:
        results.append(status_to_datapoint(search_string,status))
        processed_tweets+=1
        if processed_tweets < interval:
            print("Processed tweet",status["id"])
        if processed_tweets > 0 and processed_tweets % interval == 0:
            print(processed_tweets,"processed so far.")

    #rw.write_data(results,temp_results_filename)
    print(processed_tweets,"tweets processed.")
    return results

def query_rest_api(api,search_string="media.ccc.de/v/32c3",newer_than_id=0):
    dataset = []
    interval = 100
    scraped_tweets = 0
    
    if newer_than_id != 0:
        cursor = tweepy.Cursor(api.search, q=search_string, since_id=newer_than_id).items()
    else:
        cursor = tweepy.Cursor(api.search, q=search_string).items()

    for status in limithandled(cursor):
        dataset.append(status._json)
        scraped_tweets +=1
        if scraped_tweets < interval:
            print("Scraped tweet",dataset[-1]["id"])
        if scraped_tweets > 0 and scraped_tweets % interval == 0:
            print(scraped_tweets,"tweets scraped so far.")
    
    print("Scraped",len(dataset),"tweets.")
    print("Writing raw data to file")
    write_dataset(dataset,"last_raw_dataset.data")
    return dataset

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

def get_api():
    config = open_config("twitterauth.conf")
    #print(config)

    # source: http://docs.tweepy.org/en/v3.5.0/getting_started.html
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_token_key"], config["access_token_secret"])

    api = tweepy.API(auth)
    # query_streaming_api(api)
    return api

def main():
    pass

if __name__ == "__main__":
    main()

