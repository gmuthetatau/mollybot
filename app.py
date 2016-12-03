#imports from everyone's part of the project
#from haiku import haiku
from chris import chris

tasks = [chris]

for task in tasks:
	task.run()
	task.send()

