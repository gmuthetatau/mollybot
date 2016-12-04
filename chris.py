from reddit import reddit, getTopCommentsOfAFriend
from task import Task
from markdown2 import Markdown

class Chris(Task):
	def run(self):
		markdowner = Markdown()
		for c in getTopCommentsOfAFriend(limit = 5):
			self.body += "<p style='font-size:15px;'><span style='font-weight:bold; color:orange;'>" + str(c.score) + "</span>:  <a href=\"" + str(c.submission.url) + "\">" + c.submission.title + "</a></p>" 
			self.body += "<div style='margin-left:10px; border-left: 3px solid gray; padding-left: 5px; font-size: 15px;'>" + markdowner.convert(c.body) + "</div>"

		self.title = "Top comments of the week for /u/hutacars"

chris = Chris()
