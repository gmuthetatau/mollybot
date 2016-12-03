from reddit import reddit
from task import Task

class Chris(Task):
	def run(self):
		self.body = "this is a test"
		self.title = "this is a title"

chris = Chris()
