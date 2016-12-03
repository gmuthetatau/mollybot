#imports from everyone's part of the project
from haiku import haiku
from chris import chris
from Summary import summary

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

tasks = [chris, haiku, summary]

def send():
	to = 'tlrwgnr@gmail.com'
	gmail_user = 'bednar.christopher@gmail.com'
	gmail_pwd = 'mmitmucfufouefjf'
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	#header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + self.title + ' \n'
	#msg = header + '\n ' + self.body + '\n\n'

	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Reddit Daily Update"
	msg['From'] = gmail_user
	msg['To'] = to

	html = "<html><head></head><body>"

	for task in tasks:
		# Create the body of the message (a plain-text and an HTML version).
		#text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
		html += "<h2>" + task.title + "</h2>"
		html += "<blockquote>" + task.body + "</blockquote>"
		html += "</br>"

	html += "</body></html>"

	# Record the MIME types of both parts - text/plain and text/html.
	#part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	#msg.attach(part1)
	msg.attach(part2)

	smtpserver.sendmail(gmail_user, to, msg.as_string())
	print 'done!'
	smtpserver.close()


for task in tasks:
	task.run()

send()
