import read_write_json_data as rw 
import datetime

def clean_url(dirty_url, search_string):
   url = [part for part in dirty_url.split("#") if search_string in part][0]
   url = [part for part in url.split("?") if search_string in part][0]
   url = [part for part in url.split("&") if search_string in part][0]
   url = [part for part in url.split("=") if search_string in part][0]
   return url

def stats(results, count_retweets=True):
    stats = {}
    for tweet in results:
        for url in tweet["media_urls"]:
            if url not in stats.keys():
                stats[url] = 0
            if count_retweets:
                if "retweeted_status" in tweet["status"].keys():
                    if tweet["status"]["retweeted_status"]["retweet_count"] != tweet["status"]["retweet_count"]:
                        stats[url] += tweet["nr_of_retweets"]
                    else:
                        pass
                else:
                    stats[url] += tweet["nr_of_retweets"]
            stats[url] += 1
    return stats

def parsetime(tweet):
    return datetime.datetime.strptime(tweet["tweet_time"], '%a %b %d %X %z %Y')

def timeframe(results):
    oldest_time = parsetime(results[0])
    oldest_id = results[0]["tweet_id"]
    newest_time = parsetime(results[0])
    newest_id = results[0]["tweet_id"]

    for tweet in results:
        tweet_time = parsetime(tweet)
        if tweet_time < oldest_time:
            oldest_time = tweet_time
            oldest_id = tweet["tweet_id"]
        if tweet_time > newest_time:
            newest_time = tweet_time
            newest_id = tweet["tweet_id"]
    return oldest_time, oldest_id, newest_time, newest_id

def print_analysis(results):
    print("Analysis based on", len(results),"tweets")
    oldest,oldest_id,newest,newest_id = timeframe(results)
    print("Timeframe:",oldest,"-",newest)
    print("IDs:",oldest_id,"-",newest_id)
    
    print("Counting tweets")
    results_without = stats(results, False)
    for result in list(sorted(results_without.items(), key=lambda x: x[1]))[-1:-11:-1]:
        print(result)
    print("Counting tweets and retweets")
    results_with = stats(results, True)
    for result in list(sorted(results_with.items(), key=lambda x: x[1]))[-1:-11:-1]:
        print(result)



def main(filename):
    results = rw.read_data(filename)
    results_without, results_with = print_analysis(results)

    return results_without,results_with


if __name__ == "__main__":
    main()
