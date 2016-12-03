from reddit import reddit, getTopCommentsOfAFriend
from task import Task

class Chris(Task):
	def run(self):

		for c in getTopCommentsOfAFriend(limit = 5):
			self.body += "<p>" + c.body + "</p>"

		self.title = "Top comments of the week for /u/hutacars"

chris = Chris()
