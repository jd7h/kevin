# kevin
Find the most popular 33C3 (CCC in Hamburg) talks based on tweets. Uses Python, tweepy and the Twitter REST API.
=======

Collect list of tweeted 33c3 talks and their popularity

1. find all tweets with "media.ccc.de/v/33c3" in the body
2. count the occurrence of each links
3. print top n links/nr of occurrences

### Analysis
'''Analysis based on 6174 tweets
Timeframe: 2016-12-27 13:42:47+00:00 - 2017-01-01 22:33:00+00:00
IDs: 813741923143995392 - 815687296078974976
Counting tweets
('https://media.ccc.de/v/33c3-8064-the_transhumanist_paradox', 444)
('https://media.ccc.de/v/33c3-7964-where_in_the_world_is_carmen_sandiego', 211)
('https://media.ccc.de/v/33c3-7969-shut_up_and_take_my_money', 191)
('https://media.ccc.de/v/33c3-8229-copywrongs_2_0', 155)
('https://media.ccc.de/v/33c3-7865-gone_in_60_milliseconds', 125)
('https://media.ccc.de/v/33c3-8425-the_global_assassination_grid', 120)
('https://media.ccc.de/v/33c3-8336-talking_behind_your_back', 119)
('https://media.ccc.de/v/33c3-8169-in_search_of_evidence-based_it-security', 110)
('https://media.ccc.de/v/33c3-7999-a_data_point_walks_into_a_bar', 104)
('https://media.ccc.de/v/33c3-8416-the_untold_story_of_edward_snowden_s_escape_from_hong_kong', 100)
Counting tweets and retweets
('https://media.ccc.de/v/33c3-8064-the_transhumanist_paradox', 1116)
('https://media.ccc.de/v/33c3-7964-where_in_the_world_is_carmen_sandiego', 305)
('https://media.ccc.de/v/33c3-8229-copywrongs_2_0', 268)
('https://media.ccc.de/v/33c3-7969-shut_up_and_take_my_money', 267)
('https://media.ccc.de/v/33c3-8425-the_global_assassination_grid', 222)
('https://media.ccc.de/v/33c3-8169-in_search_of_evidence-based_it-security', 220)
('https://media.ccc.de/v/33c3-7865-gone_in_60_milliseconds', 215)
('https://media.ccc.de/v/33c3-8336-talking_behind_your_back', 210)
('https://media.ccc.de/v/33c3-7999-a_data_point_walks_into_a_bar', 200)
('https://media.ccc.de/v/33c3-8151-dissecting_modern_3g_4g_cellular_modems', 172)
'''

### What I learned from making this project
* You can only get a small set of tweets from Twitter.
Twitter is hoarding the tweets. You can either get all tweets from the current moment in time (Twitter Streaming API) or get all tweets from the past 7 days (Twitter REST API)
* Logging and feedback is not optional when building a proof of concept for a new API.
* If you want to build a dataset, save your raw data for debugging and verification purposes.
* Split functions for scraping, processing data, processing a single datapoint, cleaning data and making an analysis.
* Even for a Proof of Concept, don't cram everything in the main() function.
