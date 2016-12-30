import read_write_json_data as rw 

def clean_url(dirty_url, search_string):
   url = [part for part in dirty_url.split("#") if search_string in part][0]
   url = [part for part in url.split("?") if search_string in part][0]
   url = [part for part in url.split("&") if search_string in part][0]
   url = [part for part in url.split("=") if search_string in part][0]
   return url

def stats(results, count_retweets=True):
    stats = {}
    for tweet in results:
        url = clean_url(tweet["media_urls"], "media.ccc.de")
        if url not in stats.keys():
            stats[url] = 0
        if count_retweets:
            stats[url] += tweet["nr_of_retweets"]
        stats[url] += 1
    return stats

def main():
    results = rw.read_data("last_query_results.data")
    print(len(results))
    #clean_results = clean_data(results)
    print("Without retweets")
    results_without = stats(results, False)
    for result in list(sorted(results_without.items(), key=lambda x: x[1]))[-1:-11:-1]:
        print(result)
    print("With retweets")
    results_with = stats(results, True)
    for result in list(sorted(results_with.items(), key=lambda x: x[1]))[-1:-11:-1]:
        print(result)

    return results_without,results_with


if __name__ == "__main__":
    main()
