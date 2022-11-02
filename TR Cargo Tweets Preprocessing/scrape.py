# @imports
import snscrape.modules.twitter as snScrapeTwitter
import pandas as pd
#
#
query= '(#araskargo) lang:tr until:2022-11-01 since:2015-01-01'
tweets=[]
limit=30000
#
for tweet in snScrapeTwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date,tweet.user.username,tweet.content])
#
df = pd.DataFrame(tweets, columns=['Date','Username','Tweet'])
df.to_csv('ArasKargo_Tweets.csv')
