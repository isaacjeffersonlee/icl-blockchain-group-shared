# The above prevents output for this cell since the twint library is very verbose
import twint # Need to install directly from github repo
import datetime as dt
import pandas as pd

## For twint to work in a jupyter notebook
# import nest_asyncio
# nest_asyncio.apply()

class Scraper:
    def __init__(self,
                 srch_qry: str,
                 start_date: str,
                 num_days: int,
                 min_retweets: int):
        self.srch_query = srch_qry
        self.start_date = start_date
        self.num_days = num_days
        self.min_retweets = min_retweets
        self.tweets = []

    def _shift_date(self, date_str: str, n: int) -> str:
        """
        Shift the input date string by n days and return result.

        Args:
            date_str (str): String representation of the date, i.e '2022-01-01'
            n (int): Number of days to shift by

        Returns:
            str: String representation of the shifted date
        """
        time_delta = dt.timedelta(n)
        date_fmt = dt.date.fromisoformat(date_str)
        return str(date_fmt + time_delta)

    def _get_tweets_by_date(self, srch_qry: str, date: str, limit: int) -> None:
        """
        Append the tweets attribute with tweets for the 
        given day regarding the srch_query subject

        Args:
            srch_qry (str): Search query
            date (str): Date string, i.e 2022-01-01
            limit (int): Max number of tweets == limit * 20
        """
        config = twint.Config()
        srch_str = f"{srch_qry} min_retweets:{self.min_retweets} lang:en until:{self._shift_date(date, 1)} since:{date} -filter:links -filter:replies"
        config.Search = srch_str
        config.Limit = limit
        config.Store_object = True # Store tweets in a list
        config.Store_object_tweets_list = self.tweets
        twint.run.Search(config)

    def _get_tweets_from(self) -> None:
        """Update tweets list attribute with tweets from each day for num_days from start_date."""
        for n in range(self.num_days):
            print("")
            print(f"Getting tweets for day number: {n} / {self.num_days}")
            print("---------------------------------------------------")
            end_date = self._shift_date(self.start_date, n)
            self._get_tweets_by_date(srch_qry=self.srch_query, date=end_date, limit=1)

        print("")
        print("Finished getting tweets!")
        print("")

    def _convert_tweets_to_df(self) -> pd.DataFrame:
        """Convert the tweets list to a dataframe"""
        twt_df = pd.DataFrame(['time', 'txt', 'name', 'username', 'likes', 'retweets', 'replies'])
        for twt in self.tweets:
            txt = twt.tweet
            time = twt.datetime
            name = twt.name
            replies = twt.replies_count
            retweets = twt.retweets_count
            likes = twt.likes_count
            username = twt.username
            new_row = pd.DataFrame.from_dict({'time': [time], 'txt': [txt],
                'name': [name], 'username': [username], 'likes': [likes],
                'retweets': [retweets], 'replies': [replies]})
            twt_df = pd.concat([new_row, twt_df]).reset_index(drop=True)

        # Note: the last zero rows are just the column
        # names for some reason, so we drop them before returning
        # the dataframe.
        twt_df.drop(twt_df.tail(7).index, inplace=True)
        # Also for some reason we get a weird last column
        twt_df.drop(twt_df.columns[len(twt_df.columns)-1], axis=1, inplace=True)

        return twt_df

    def scrape_to_csv(self, path: str) -> None:
        """
        Combine all methods to scrape tweets and save to csv.

        Args:
            path (str): Path of csv to save tweets to.
        """
        # Populate tweets list attribute
        self._get_tweets_from()
        twt_df = self._convert_tweets_to_df()
        twt_df.to_csv(path, index=False)
        print(f"Saved results to: {path}")
        print("")


if __name__ == "__main__":
    curr_pair = "USDT_XRP"
    df = pd.DataFrame()
    for year in range(2021, 2016, -1):
        sc = Scraper(srch_qry="Ripple Crypto XRP",
                     start_date=f"{year}-01-01",  # The date to start scraping from
                     num_days=365,  # The number of days to scrape for
                     min_retweets=10)  # Reduce this for more tweets

        sc.scrape_to_csv(f"Data/Tweets/{curr_pair}_tweets_{year}.csv")
        next_df = pd.read_csv(f"Data/Tweets/{curr_pair}_tweets_{year}.csv", index_col=0, parse_dates=True)
        df = pd.concat([df, next_df], axis=0) 

    df.to_csv(f"Data/Tweets/{curr_pair}_tweets_2017-2022.csv", index=True)

