import unirest
import urllib
import json
import re
import random
from reddit import reddit, getFrontPage
from task import Task


class haiku(Task):
	def run(self):
		di = {}
		for subs in getFrontPage():
			subArray = subs.title.split()
			count = 0
			for i in subArray:
				#Getting rid of characters ending with non-alphabetic characters

				legal = re.match("^((?![,.?!;:+]).)*$", i)
				if legal:
					#HTML Encoding
					ie = urllib.quote(i)
					
					url = "https://wordsapiv1.p.mashape.com/words/" + ie + "/syllables"
					url_type = "https://wordsapiv1.p.mashape.com/words/" + ie


					response_type = unirest.get(url_type,
					  headers={
					    "X-Mashape-Key": "M8guaipuA3mshQuGICoduiiJgHLlp1A3jjZjsngXUoWO7LUKMl",
					    "Accept": "application/json"
					  }
					)


					try:
						ret_type = json.loads(response_type.raw_body)

						if "count" in ret_type["syllables"]:
							di[i] = []
							di[i].append(ret_type["syllables"]["count"])
							arr = []
							for k in ret_type["results"]:
								pos = k["partOfSpeech"]
								if (pos) in arr:
									continue
								arr.append(k["partOfSpeech"])
							di[i].append(arr)

					except ValueError:
						pass
					except KeyError:
						pass

		#####################################

		firstLine = 5
		thirdLine = 5
		secondLine = 7

		noun_arr = []
		verb_arr = []
		adverb_arr = []
		adj_arr = []
		conj_arr = []

		for key in di.keys():
			for l in di[key][1]:
				if (l == "adverb"):
					adverb_arr.append(key)
				if (l == "verb"):
					verb_arr.append(key)
				if (l == "adjective"):
					adj_arr.append(key)
				if (l == "noun"):
					noun_arr.append(key)
				if (l == "conjunction"):
					conj_arr.append(key)
		
		# shuffle the lists
		random.shuffle(adverb_arr)
		random.shuffle(verb_arr)
		random.shuffle(adj_arr)
		random.shuffle(noun_arr)
		random.shuffle(conj_arr)

		
		# rand_verb = random.randint(0,len(verb_arr)-1)

		syl_count = 0
		ret_string = ""
		#Getting first line
		while (syl_count < 5):

			one = random.choice(verb_arr)

			#print "One: " + one
			ret_string += one + " "
			syl_count += di[one][0]
			if (syl_count < 5):
				rem = 5 - di[one][0]
				for wo in adj_arr:
					if di[wo][0] <= rem:
						#print "Wo: " + wo
						ret_string += wo + " "
						syl_count += di[wo][0]
						rem = rem - di[wo][0]
						if syl_count < 5:
							for no in noun_arr:
								if di[no][0] < rem:
									#print "no: " + no
									ret_string += no + " "
									syl_count += di[no][0]
									rem = rem - di[no][0]
		#print ret_string

		syl_count = 0
		ret_string2 = ""
		#Getting first line
		while (syl_count < 7):
			one = random.choice(verb_arr)
			#print "One: " + one
			ret_string2 += one + " "
			syl_count += di[one][0]
			if (syl_count < 7):
				rem = 7 - di[one][0]
				for wo in adj_arr:
					if di[wo][0] <= rem:
						#print "Wo: " + wo
						ret_string2 += wo + " "
						syl_count += di[wo][0]
						rem = rem - di[wo][0]
						if syl_count < 7:
							for no in noun_arr:
								if di[no][0] < rem:
									#print "no: " + no
									ret_string2 += no + " "
									syl_count += di[no][0]
									rem = rem - di[no][0]
		#print ret_string2

		syl_count = 0
		ret_string3 = ""
		#Getting first line
		while (syl_count < 5):
			one = random.choice(verb_arr)
			#print "One: " + one
			ret_string3 += one + " "
			syl_count += di[one][0]
			if (syl_count < 5):
				rem = 5 - di[one][0]
				for wo in adj_arr:
					if di[wo][0] <= rem:
						#print "Wo: " + wo
						ret_string3 += wo + " "
						syl_count += di[wo][0]
						rem = rem - di[wo][0]
						if syl_count < 5:
							for no in noun_arr:
								if di[no][0] < rem:
									#print "no: " + no
									ret_string3 += no + " "
									syl_count += di[no][0]
									rem = rem - di[no][0]
		#print ret_string3

		str_haiku = ret_string + "\n" + ret_string2 + "\n" + ret_string3
		print str_haiku
		return str_haiku
		

haiku = haiku()

