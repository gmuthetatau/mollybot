from reddit import reddit
from task import Task

class Haiku(Task):
	def run(self):
		self.body = "This is going to the haiku"
		self.title = "This is the title of Molly's task."

haiku = Haiku()
