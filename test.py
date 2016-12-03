import reddit
from reddit import getFrontPage

# for item in vars(getFrontPage()):
#     print item

for item in getFrontPage():
    print item.subreddit
    break
    # for post in item:
    #     print post.title

    # print item.ups
    # print item.downs
    # print item.score
