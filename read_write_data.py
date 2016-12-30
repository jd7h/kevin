import csv

def read_data(filename):
    results = []
    with open(filename,"r",newline='') as infile:
        reader = csv.DictReader(infile,["tweet_id","tweet_time","nr_of_retweets","media_urls"])
        for row in reader:
            results.append(row)
    return results

def write_data(results,filename):
    with open(filename,"w",newline='') as outfile:
        writer = csv.DictWriter(outfile,["tweet_id","tweet_time","nr_of_retweets","media_urls"])
        writer.writerows(results)
