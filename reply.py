from reddit import reddit
import os
import re
from haiku import haiku



if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = filter(None, posts_replied_to)

subreddit = reddit.subreddit('test')
for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("give me a shitty haiku", submission.title, re.IGNORECASE):
            haiku.run()
            submission.reply(haiku.body)
            print "Bot replying to : ", submission.title
            posts_replied_to.append(submission.id)
            with open("posts_replied_to.txt", "w") as f:
                for post_id in posts_replied_to:
                    f.write(post_id + "\n")
