#!/usr/bin/env python3

# https://unsplash.com/search/photos/puzzle

import csv, re, subprocess
from urllib import request

class DictEnum():
	data = {}

	def __init__(self, data):
		for pointer in range(len(data)):
			self.data[data[pointer]] = pointer

	def __getattr__(self, name):
		return self.data[name]

puzzleLimit = 100

print("<!DOCTYPE html><html><head><title>The Unofficial Stack Exchange Puzzle Book</title><style>ul {margin-left: 1em;} div {page-break-after: always;} img {max-width: 100%;} .spoiler {transform: rotate(180deg);} body {max-width: 50em; margin: 0 auto; background: #f4f4f4; color: #111111;}</style></head><body><h1>Acknowledgements</h1><p>I would like to thank the <a href=\"https://puzzling.stackexchange.com/\">puzzling.stackexchange.com</a> community for writing these puzzles, <a href=\"https://stackexchange.com\">stackexchange.com</a> for providing the data, and <a href=\"https://creativecommons.org/\">creativecommons.org</a> for making this possible. Like the puzzles within, this is licensed under the CC BY-SA 3.0 license. This book was created using <a href=\"https://data.stackexchange.com\">data.stackexchange.com</a> to gather data, <a href=\"https://www.python.org/\">python</a> to parse and structure the data, and <a href=\"https://pandoc.org/MANUAL.html\">pandoc</a> to typeset as pdf.</p><p>And thank you, the reader for reading this 'book'. I hope you enjoy the puzzles. If you wish to contribute to this book, it can be found on <a href=\"https://github.com/mattconsto/puzzle-book\">github.com/mattconsto/puzzle-book</a>.</p><p>Happy puzzling!</p>\n")

headers = DictEnum(["Id", "URL", "Score", "ViewCount", "AnswerCount", "FavoriteCount", "Title", "Tags", "Body", "CreationDate", "OwnerUserId", "DisplayName", "Reputation", "Gold", "Silver", "Bronze", "AnswerId", "AnswerScore", "AnswerBody", "AnswerCreationDate", "AnswerOwnerId", "AnswerDisplayName", "AnswerReputation", "AnswerGold", "AnswerSilver", "AnswerBronze"])

index = {}

with open("data.csv") as handle:
	reader = csv.reader(handle, delimiter = ",", quotechar = "\"")
	ignored = next(reader, None)
	# @Improvement Check headers

	print("<div>\n\n<h1>Puzzles</h1>\n")

	count = 0
	for row in reader:
		body = row[headers.Body]
		mapping = {
			'<H5>':'<H6>', '</H5>':'</H6>', '<h5>':'<h6>', '</h5>':'</h6>',
			'<H4>':'<H5>', '</H4>':'</H5>', '<h4>':'<h5>', '</h4>':'</h5>',
			'<H3>':'<H4>', '</H3>':'</H4>', '<h3>':'<h4>', '</h3>':'</h4>',
			'<H2>':'<H3>', '</H2>':'</H3>', '<h2>':'<h3>', '</h2>':'</h3>',
			'<H1>':'<H2>', '</H1>':'</H2>', '<h1>':'<h2>', '</h1>':'</h2>',
		}
		for k, v in mapping.items():
			body = body.replace(k, v)

		# Download images
		def replacement(match):
			url = match.group(1)
			filename = url[url.rfind("/")+1:]
			request.urlretrieve(url, "images/" + filename)
			if filename[filename.rfind(".")+1:] == "gif":
				subprocess.check_call(["convert", "images/" + filename + "[0]", "images/" + filename[:filename.rfind(".")] + ".png"]);
				filename = filename[:filename.rfind(".")] + ".png"
			return "<img src=\"images/" + filename + "\""

		body = re.sub(r'<img src="(http.+?\.[a-zA-Z]+)"', replacement, body)

		print("<h2><a name=\"question%s\"></a><a href=\"%s\">%s</a></h2>\n\n<p class=\"subtitle\">%s votes, asked by <a href=\"https://puzzling.stackexchange.com/users/%s\">%s#%s</a>, answered by <a href=\"https://puzzling.stackexchange.com/users/%s\">%s#%s</a></p>\n\n%s\n<a href=\"#solution%s\">Go to Solution</a>\n\n<hr /><hr />\n" % (row[headers.Id], row[headers.URL], row[headers.Title], row[headers.Score], row[headers.OwnerUserId], row[headers.DisplayName], row[headers.OwnerUserId], row[headers.AnswerOwnerId], row[headers.AnswerDisplayName], row[headers.AnswerOwnerId], body, row[headers.Id]))

		count += 1
		if count >= puzzleLimit:
			break

		# Generate index
		tags = [tag[1:-1] for tag in re.findall(r'<[a-z0-9\-_]+>', row[headers.Tags])]
		for tag in tags:
			if not tag in index:
				index[tag] = []
			index[tag].append(row[headers.Id])

with open("data.csv") as handle:
	reader = csv.reader(handle, delimiter = ",", quotechar = "\"")
	ignored = next(reader, None)
	# @Improvement Check headers

	print("\n</div><div>\n<h1>Solutions</h1>\n")

	count = 0
	for row in reader:
		body = row[headers.AnswerBody]
		mapping = {
			'<H5>':'<H6>', '</H5>':'</H6>', '<h5>':'<h6>', '</h5>':'</h6>',
			'<H4>':'<H5>', '</H4>':'</H5>', '<h4>':'<h5>', '</h4>':'</h5>',
			'<H3>':'<H4>', '</H3>':'</H4>', '<h3>':'<h4>', '</h3>':'</h4>',
			'<H2>':'<H3>', '</H2>':'</H3>', '<h2>':'<h3>', '</h2>':'</h3>',
			'<H1>':'<H2>', '</H1>':'</H2>', '<h1>':'<h2>', '</h1>':'</h2>',
		}
		for k, v in mapping.items():
			body = body.replace(k, v)

		# Download images
		def replacement(match):
			url = match.group(1)
			filename = url[url.rfind("/")+1:]
			request.urlretrieve(url, "images/" + filename)
			if filename[filename.rfind(".")+1:] == "gif":
				subprocess.check_call(["convert", "images/" + filename + "[0]", "images/" + filename[:filename.rfind(".")] + ".png"]);
				filename = filename[:filename.rfind(".")] + ".png"
			return "<img src=\"images/" + filename + "\""

		body = re.sub(r'<img src="(http.+?\.[a-zA-Z]+)"', replacement, body)

		print("<h2><a name=\"solution%s\"></a><a href=\"%s\">%s</a></h2>\n\n<p class=\"subtitle\">%s Votes, asked by <a href=\"https://puzzling.stackexchange.com/users/%s\">%s#%s</a>, answered by <a href=\"https://puzzling.stackexchange.com/users/%s\">%s#%s</a></p>\n\n%s\n<a href=\"#question%s\">Return to Question</a>\n\n<hr /><hr />\n" % (row[headers.Id], row[headers.URL], row[headers.Title], row[headers.Score], row[headers.OwnerUserId], row[headers.DisplayName], row[headers.OwnerUserId], row[headers.AnswerOwnerId], row[headers.AnswerDisplayName], row[headers.AnswerOwnerId], body, row[headers.Id]))

		count += 1
		if count >= puzzleLimit:
			break

print("\n</div><div>\n<h1>Index</h1>\n<ul>")

for tag in sorted(index.keys()):
	first = True
	concat = ""
	for i in index[tag]:
		if first:
			first = False
		else:
			concat += ", "
		concat += "<a href=\"question%s\">Q%s</a>" % (i, i)
	print("<li>%s: %s.</li>" % (tag.title(), concat))

print("</ul>\n</div><div>\n</body></html>")
