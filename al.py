from reddit import reddit
from task import Task
from reddit import getFrontPage
from random import shuffle

class Al(Task):

	def shuffle_word(self, word):
		word = list(word)
		shuffle(word)
		return ''.join(word)

	def dislexia(self, list):
		final = []
		for item in list:
			text = item.title
			tlist = text.split(" ")
			c = 0
			l = ""
			while c < len(tlist):
				word = tlist[c]
				if len(word) > 3:
					x = word[0]
					y = word[-1]
					wshuffle = word[1 : -1]
					shuffled =self.shuffle_word(wshuffle)
					fword = ("" + x + shuffled + y)
					#print word
					#print wshuffle
					#print fword
					l += fword + " "
				else:
					l += word + " "
				c += 1
			final.append(l)
		string = ""
		for i in final:
			string += final[i] + "<br>"
		return string


	def run(self):
		self.body = self.dislexia(getFrontPage())
		self.title = "The Word Shuffle"


al = Al()
