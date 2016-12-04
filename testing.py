import unirest
import json
import re
from reddit import reddit, getFrontPage
from task import Task

class haiku(Task):
	def run(self):
		
		for subs in getFrontPage():
			subArray = subs.title.split()
			for i in subArray:
				print "i is: " + i
				matchO = re.match("^((?![,.?!;:]).)*$", i)
				if matchO:

					url = "https://wordsapiv1.p.mashape.com/words/" + i + "/syllables"
					print "url is: " + url
					# These code snippets use an open-source library. http://unirest.io/python
					
					try:
						response = unirest.get(url,
						  headers={
						    "X-Mashape-Key": "MqocUSZZ8vmshdZKANtf2ay0cP9jp1JGrdcjsn0faXKxsOlkoC",
						    "Accept": "application/json"
						  }
						)

						print json.loads(response.raw_body["syllables"])
					except:
						print "something happened"
				else:
					print "no match!"
					

haiku = haiku()
