# kevin
## Find the most popular 33C3 (CCC in Hamburg) talks based on tweets. 
This project uses Python3, tweepy and the Twitter REST API.

1. find all tweets with "media.ccc.de/v/33c3" in the body
2. count the occurrence of each talk
3. print top 10 talks with nr of occurrences in tweets

## Top 10 talks of 33C3
Analysis based on 6174 tweets between 2016-12-27 and 2017-01-01

### Tweets only

1. [https://media.ccc.de/v/33c3-8064-the_transhumanist_paradox](https://media.ccc.de/v/33c3-8064-the_transhumanist_paradox) (444)
2. [https://media.ccc.de/v/33c3-7964-where_in_the_world_is_carmen_sandiego](https://media.ccc.de/v/33c3-7964-where_in_the_world_is_carmen_sandiego) (211)
3. [https://media.ccc.de/v/33c3-7969-shut_up_and_take_my_money](https://media.ccc.de/v/33c3-7969-shut_up_and_take_my_money) (191)
4. [https://media.ccc.de/v/33c3-8229-copywrongs_2_0](https://media.ccc.de/v/33c3-8229-copywrongs_2_0) (155)
5. [https://media.ccc.de/v/33c3-7865-gone_in_60_milliseconds](https://media.ccc.de/v/33c3-7865-gone_in_60_milliseconds) (125)
6. [https://media.ccc.de/v/33c3-8425-the_global_assassination_grid](https://media.ccc.de/v/33c3-8425-the_global_assassination_grid) (120)
7. [https://media.ccc.de/v/33c3-8336-talking_behind_your_back](https://media.ccc.de/v/33c3-8336-talking_behind_your_back) (119)
8. [https://media.ccc.de/v/33c3-8169-in_search_of_evidence-based_it-security](https://media.ccc.de/v/33c3-8169-in_search_of_evidence-based_it-security) (110)
9. [https://media.ccc.de/v/33c3-7999-a_data_point_walks_into_a_bar](https://media.ccc.de/v/33c3-7999-a_data_point_walks_into_a_bar) (104)
10. [https://media.ccc.de/v/33c3-8416-the_untold_story_of_edward_snowden_s_escape_from_hong_kong](https://media.ccc.de/v/33c3-8416-the_untold_story_of_edward_snowden_s_escape_from_hong_kong) (100)

### Tweets and retweets

1. [https://media.ccc.de/v/33c3-8064-the_transhumanist_paradox](https://media.ccc.de/v/33c3-8064-the_transhumanist_paradox) (1116)
2. [https://media.ccc.de/v/33c3-7964-where_in_the_world_is_carmen_sandiego](https://media.ccc.de/v/33c3-7964-where_in_the_world_is_carmen_sandiego) (305)
3. [https://media.ccc.de/v/33c3-8229-copywrongs_2_0](https://media.ccc.de/v/33c3-8229-copywrongs_2_0) (268)
4. [https://media.ccc.de/v/33c3-7969-shut_up_and_take_my_money](https://media.ccc.de/v/33c3-7969-shut_up_and_take_my_money) (267)
5. [https://media.ccc.de/v/33c3-8425-the_global_assassination_grid](https://media.ccc.de/v/33c3-8425-the_global_assassination_grid) (222)
6. [https://media.ccc.de/v/33c3-8169-in_search_of_evidence-based_it-security](https://media.ccc.de/v/33c3-8169-in_search_of_evidence-based_it-security) (220)
7. [https://media.ccc.de/v/33c3-7865-gone_in_60_milliseconds](https://media.ccc.de/v/33c3-7865-gone_in_60_milliseconds) (215)
8. [https://media.ccc.de/v/33c3-8336-talking_behind_your_back](https://media.ccc.de/v/33c3-8336-talking_behind_your_back) (210)
9. [https://media.ccc.de/v/33c3-7999-a_data_point_walks_into_a_bar](https://media.ccc.de/v/33c3-7999-a_data_point_walks_into_a_bar) (200)
10. [https://media.ccc.de/v/33c3-8151-dissecting_modern_3g_4g_cellular_modems](https://media.ccc.de/v/33c3-8151-dissecting_modern_3g_4g_cellular_modems) (172)

## What I learned from making this project
* You can only get a small set of tweets from Twitter. Twitter is hoarding the tweets. You can either get all tweets from the current moment in time (Twitter Streaming API) or get all tweets from the past 7 days (Twitter REST API). :(
* Logging, error-handling and feedback are not optional when building a proof of concept for an API.
* If you want to build a dataset, save your raw data for debugging and verification purposes.
* Split functions for scraping, processing data, processing a single datapoint, cleaning data and making an analysis.
* Even for a Proof of Concept, don't cram everything in the main() function.
