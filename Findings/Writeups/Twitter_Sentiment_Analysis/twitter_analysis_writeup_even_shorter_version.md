# Positive or Negative Tweets Vs. Price Change

**Author: Isaac Lee**     |     **Date: 26/02/2022**     |    <img src="https://cdn.iconscout.com/icon/free/png-128/github-logo-3002017-2496133.png" alt="Github Logo Icon" style="zoom:25%;" />   <u>**[Source Code](https://github.com/isaacjeffersonlee/icl-blockchain-group-shared)**</u>   

## Introduction

The main aim of this report is to answer the following question:

> ### Question
>
> Does the number of positive/negative tweets have any link with price change for different cryptocurrencies?

We will look at the past five years for a time frame and examine three different coin pairs:

- **USDT_BTC** (Bitcoin) 
- **USDT_ETH** (Ethereum)
- **USDT_XRP** (Ripple)

## Calculating "Sentiment"

*Sentiment* in this context means how positive or negative a tweet is.
Without going into two much detail about how the model works[^1], the main idea is that it has been given a large number of common phrases/words that were rated by humans on their positivity/negativity.
Also several grammatical heuristics such as contrasting conjunctions and intensifying adverbs are used.
A compound score is calculated by taking into account the number of positive phrases Vs. number of negative phrases (and some other stuff). 

## Exploring Price Movement Vs. Twitter Data

### Tweet Count Per Day Vs. Price Movement

Does the number of relevant tweets per day (which we also refer to as the tweet density) have any correlation with price movement? For each cryptocurrency we will examine the price movement Vs. the total number of tweets per day, the total number of tweets per day with positive sentiment and the total number of tweets per day with negative sentiment.













We start with the **USDT_BTC**:

Total tweet count:

----

![](/home/isaac/Projects/icl-blockchain-group-shared/Findings/Images/USDT_BTC_price_vs_total_tweet_count_2017-2022.png)

---

Positive sentiment tweet count:

![](/home/isaac/Projects/icl-blockchain-group-shared/Findings/Images/USDT_BTC_price_vs_pos_tweet_count_2017-2022.png)

---











Negative sentiment tweet count:

![](/home/isaac/Projects/icl-blockchain-group-shared/Findings/Images/USDT_BTC_price_vs_neg_tweet_count_2017-2022.png)

So we can see that there is definite correlation between the tweet count per day and the price movement, with an increase in number of tweets for big price increases. Note that our data is capped at maximum twenty tweets per day, so some days would actually have more tweets than plotted. 

When comparing positive Vs. negative sentiment tweets we can see that there are always more positive tweets than negative, which perhaps suggests that posters have a bias to favour Bitcoin, since if they're posting about it they likely have an interest. Also interestingly it seems that in the big price dips, even though there are still more positive tweets (probably from the bias) the actual number of positive tweets decreases relative to the previous high.

Moving on, we look at tweet counts for **USDT_ETH**:

Total tweet count:

----

![](/home/isaac/Projects/icl-blockchain-group-shared/Findings/Images/USDT_ETH_price_vs_total_tweet_count_2017-2022.png)

---











Positive sentiment tweet count:

![](/home/isaac/Projects/icl-blockchain-group-shared/Findings/Images/USDT_ETH_price_vs_pos_tweet_count_2017-2022.png)

---

Negative sentiment tweet count:

![](/home/isaac/Projects/icl-blockchain-group-shared/Findings/Images/USDT_ETH_price_vs_neg_tweet_count_2017-2022.png)

---

Ethereum seems to be even more correlated than Bitcoin! With a definite increase in tweet counts per day just before big price increases, suggesting that tweet count could perhaps be a good predictor for Ethereum price. Perhaps this is because whilst Ethereum is still well known, it is far less well known outside of the cryptocurrency/financial world.

Finally we look at the tweet counts for **USDT_XRP**:

Total tweet count:

----

![](/home/isaac/Projects/icl-blockchain-group-shared/Findings/Images/USDT_XRP_price_vs_total_tweet_count_2017-2022.png)

---

Positive sentiment tweet count:

![](/home/isaac/Projects/icl-blockchain-group-shared/Findings/Images/USDT_XRP_price_vs_pos_tweet_count_2017-2022.png)

---















Negative sentiment tweet count:

![](/home/isaac/Projects/icl-blockchain-group-shared/Findings/Images/USDT_XRP_price_vs_neg_tweet_count_2017-2022.png)

---

Again, a definite correlation, however as before there is not really enough data to make any definite conclusions.

> #### Conclusions
>
> - Definite correlation between Bitcoin price movement and the tweet count per day.
> - Even stronger correlation for Ethereum.
> - Not enough data for Ripple.
> - (When there is enough data) increases in tweet count are often followed by increases in price, decreases in *positive* tweet counts are followed by price dips and the count of *negative* tweets seems to have little use.

## Summary

Now that we have finished our analysis we can answer the initial question we asked:

> ### Answer
>
> **Q.** *Does the number of positive/negative tweets have any link with price change for different cryptocurrencies?*
> **A.** Yes! Just before large price increases, there are often an increase in Tweets per day and before price dips, there are fewer *positive* tweets per day.
>**Note**: It seems that when using Twitter data, the coin in question needs to be in a "sweet spot" of popularity, where it is not over saturated to the point where even your Grandma is talking about it but still popular enough such that there is enough twitter interest.

[^1]: https://www.nltk.org/_modules/nltk/sentiment/vader.html
