# ASW6-SO3whNyETd7EmFmdF9Tp0_LKQ
import praw

#put in seperate (local only) json file
# import json
client_id = "tytnhN9MLCYuDA"
client_secret = "ASW6-SO3whNyETd7EmFmdF9Tp0_LKQ"
user_agent = "Testin_API"
username = "stevsken"
password = "nmf2zWBy4dT9"

reddit = praw.Reddit(client_id = client_id,
                    client_secret = client_secret,
                    user_agent = user_agent,
                    username = username,
                    password = password,
                    )


announcements = reddit.subreddit("announcements")
gaming = reddit.subreddit("gaming")
askreddit = reddit.subreddit("funny")
science = reddit.subreddit("science")
worldnews = reddit.subreddit("worldnews")
lifeprotips = reddit.subreddit("lifeprotips")

subreddits = [announcements, gaming, askreddit, science, worldnews, lifeprotips]

#.hot
#.new
#.controversial
#.top
#.gilded


for subreddit in subreddits:
    subreddit_pull = subreddit.new(limit =3)
    for i in subreddit_pull:
        print(i.title)



# use the following to see all tags/features that are available
#type(new)
#x = next(new)
#dir(x)


