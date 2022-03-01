# Exploring the Correlation between Twitter Sentiment and Price Movement

#### Author: Isaac Lee  

#### Date: 26/02/2022

## [Source Code](https://github.com/isaacjeffersonlee/icl-blockchain-group-shared)   

## Introduction

We look to explore whether there is a correlation between Twitter sentiment regarding a specific
cryptocurrency and its price movement.

We will look at the past five years for a time frame and examine four different coin pairs:

- USDT_BTC (Bitcoin)
- USDT_ETH (Ethereum)
- USDT_XMR (Monero)
- USDT_XRP (Ripple)

First we gather the necessary data using various APIs, analyze the results using Python and
then interpret our findings.

## Gathering the Data

#### Price Data

In order to get pricing data we send a request to the [Poloniex API](https://docs.poloniex.com/#returnchartdata). We ask for 30 minute candle
data, from the past year. Note that this API does not support hourly candles, so instead we aggregate our
30 minute candles into hourly candles. Also we are limited to how far back we can go, so instead of 
asking for the past five years all in one request, we use a for loop and loop over each year, sending
five separate requests, one for each year.

We convert the response data into a Pandas DataFrame object. The first fews rows are given by:

|                     | weightedAverage |    close |     high |      low |     open |    volume |
| ------------------: | --------------: | -------: | -------: | -------: | -------: | --------: |
| 2017-01-01 01:00:00 |        0.006486 | 0.006498 | 0.006498 | 0.006481 | 0.006487 | 15.481315 |
| 2017-01-01 02:00:00 |        0.006498 | 0.006498 | 0.006498 | 0.006498 | 0.006498 |  0.000000 |
| 2017-01-01 03:00:00 |        0.006560 | 0.006563 | 0.006563 | 0.006551 | 0.006551 | 18.741457 |

(Note: the index is a Pandas time index object).

#### Twitter Data

The Twitter data was slightly harder to obtain, since Twitter now charges for users to access historical data
on tweets.  Also the official Twitter Python API has very harsh limits on how far back we can get tweets from and the number of requests allowed. So instead we turn to a really nice Tweet scraping python package, called "[TWINT](https://pypi.org/project/twint/)" which stands for:

- (TW)itter,
- (IN)elligence,
- (T)ool.

It is much nicer than the official Twitter API with the following benefits:

- Can fetch almost **all** tweets (Twitter API limits to last 3200 tweets only);
- Fast initial setup;
- Can be used anonymously and without Twitter sign up;
- **No rate limitations**.

However the issue with TWINT is that we want to go back five years and currently the from and until parameters that you can pass to your TWINT search seem to not work, so instead we use a little known Twitter feature that allows you to filter your search directly with a query, i.e if we input the following into the twitter search bar then we can filter tweets by date, language and minimum number of retweets. We can also filter *out* links and replies which are not useful to us:

```html
{search_query} min_retweets: n lang:en until:{end_date} since:{start_date} -filter:links -filter:replies
```

So then we incorporate this method of filtering by day with a for loop which loops over each day in the year and sends a separate request to get tweets from that day which mention the cryptocurrency pair we're interested in. 

Note that we set the minimum number of retweets to a sufficiently large number so that we can only scrape *important* tweets.

Once we have all the tweets for each day for each year we convert to a Pandas DataFrame and save as a CSV.  The first entry of our tweet DataFrame looks something like this:

|            |                                               txt |    name |      username |  likes | retweets | replies |
| ---------: | ------------------------------------------------: | ------: | ------------: | -----: | -------: | ------- |
| 2021-12-29 | The main reason why #XRP will become the most ... | Blood 🩸 | bloodorcrypto | 1741.0 |    303.0 | 111.0   |

(We also perform some data cleaning, removing all non-alphanumeric characters from each tweet).

## Calculating Sentiment

In the interest of time we use a pre-trained sentiment analysis model from the Natural Language Tool Kit Python library, which contains many great tools for Natural Language Processing and Modeling.

We use the Vader model from NLTK, which stands for:

- (V)alence;
- (A)ware;
- (D)ictionary;
- for s(E)ntiment;
- (R)easoning.

Without going into two much detail of how Vader works, the main idea is that it uses a dictionary with a large number of common phrases/words that were rated by humans on their polarity and intensity.
Also several grammatical heuristics such as contrastive conjuctions and intensifying adverbs are used.

A compound score is calculated, which is the sum of the scores of the sentiment features found in the text, normalized to fall between 0 and 1.

Also we get the percentage of (neu)tral, (pos)itive and (neg)ative sentiment features found in the text as neu, pos and neg outputs.

## Exploring Price Movement Vs. Twitter Data

So now that we have all our data and sentiments calculated we can finally try and answer the question: is Twitter data correlated with price movement? Does this depend on the cryptocurrency of choice?

### Sentiment Compound Scores Vs. Price Movement

We begin by looking at 



------

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_BTC_price_vs_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_BTC_price_vs_pos_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_BTC_price_vs_neg_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_BTC_price_vs_total_tweet_count_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_BTC_price_vs_neg_tweet_count_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_BTC_price_vs_pos_tweet_count_2017-2022.png)

### Ethereum (USDT_ETH)

------

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_ETH_price_vs_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_ETH_price_vs_pos_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_ETH_price_vs_neg_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_ETH_price_vs_total_tweet_count_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_ETH_price_vs_neg_tweet_count_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_ETH_price_vs_pos_tweet_count_2017-2022.png)

### Monero (USDT_XMR)

------

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XMR_price_vs_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XMR_price_vs_pos_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XMR_price_vs_neg_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XMR_price_vs_total_tweet_count_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XMR_price_vs_neg_tweet_count_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XMR_price_vs_pos_tweet_count_2017-2022.png)

### Ripple (USDT_XRP)

---

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XRP_price_vs_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XRP_price_vs_pos_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XRP_price_vs_neg_sentiment_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XRP_price_vs_total_tweet_count_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XMR_price_vs_sentiment_2017-2022.png)![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XRP_price_vs_neg_tweet_count_2017-2022.png)

![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/USDT_XRP_price_vs_pos_tweet_count_2017-2022.png)



## Conclusions

 

###### ![](/home/isaac/Projects/Crypto_Analysis/Findings/Images/tiled_price_vs_sentiment_2017-2018.png)



