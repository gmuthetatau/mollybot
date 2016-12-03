from reddit import reddit
from task import Task

class Chris(Task):
	def run(self):

		self.body = "This is the body of what I am going to return"
		self.title = "Chris test task"

chris = Chris()
