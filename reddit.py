import praw

my_user_agent = 'MollyBot v1.0'
my_client_id = 'XVHxaAXhfZuuzA'
my_client_secret = 'PDB4fWMq_zp7NwtYCzUy7JKxjb4'
my_username = 'mollybot96'
my_password = 'mollyrules'

reddit = praw.Reddit(user_agent=my_user_agent,
                     client_id=my_client_id,
                     client_secret=my_client_secret,
                     username=my_username,
                     password=my_password)


def getFrontPage(time_filter='day', limit=10):
	return reddit.front.top(time_filter=time_filter, limit=limit)

def getSubredditPosts(subreddit, limit=10):
	return reddit.subreddit(subreddit).top(limit=limit)

def getTopCommentsOfAFriend(limit = 10, username = "hutacars"):
	return reddit.redditor(username).comments.top(time_filter="week", limit=10)