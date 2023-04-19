import pandas as pd
import snscrape.modules.twitter as sntwitter

keyword = input("Enter the keyword: ")
num = int(input("Enter no. of tweets: "))

result = sntwitter.TwitterSearchScraper(keyword)

tweets = []
for i, tweet in enumerate(result.get_items()):
    att = [
        tweet.date,
        tweet.content,
        tweet.user.username,
        tweet.likeCount,
        tweet.retweetCount,
    ]
    tweets.append(att)
    if i>num-2:
        break

tweets = pd.DataFrame(tweets, columns=['date', 'content', 'username', 'like_count', 'retweet_count'])

print(tweets)

tweets.to_csv('IndiaTweets.csv', index='False')