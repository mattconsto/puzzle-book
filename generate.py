#!/usr/bin/env python3

# https://unsplash.com/search/photos/puzzle

import csv, re

class DictEnum():
	data = {}

	def __init__(self, data):
		for pointer in range(len(data)):
			self.data[data[pointer]] = pointer

	def __getattr__(self, name):
		return self.data[name]

puzzleLimit = 50

print("<!DOCTYPE html><html><head><title>The Unofficial Stack Exchange Puzzle Book</title><style>ul {margin-left: 1em;} div {page-break-after: always;} img {max-width: 100%;} .spoiler {transform: rotate(180deg);} body {max-width: 50em; margin: 0 auto; background: #f4f4f4; color: #111111;}</style></head><body><h1>Acknowledgements</h1><p>I would like to thank the [puzzling.stackexchange.com](https://puzzling.stackexchange.com/) community for writing these puzzles, [stackexchange.com](https://stackexchange.com) for providing the data, and [creativecommons.org](https://creativecommons.org/) for making this possible. This book, like the puzzles within is licensed under the CC BY-SA 3.0 license.</p><p>This book was created using (data.stackexchange.com)[https://data.stackexchange.com] to gather data, [python](https://www.python.org/) to parse and structure the data, and [pandoc](https://pandoc.org/MANUAL.html) to typeset as pdf.</p><p>And lastly, thank you, the reader for reading this 'book'. I hope you enjoy the puzzles. If you wish to contribute to this book, it can be found on [my Github](https://github.com/mattconsto/puzzle-book).</p>\n")

headers = DictEnum(["Id", "URL", "Score", "ViewCount", "AnswerCount", "FavoriteCount", "Title", "Tags", "Body", "CreationDate", "OwnerUserId", "DisplayName", "Reputation", "Gold", "Silver", "Bronze", "AnswerId", "AnswerScore", "AnswerBody", "AnswerCreationDate", "AnswerOwnerId", "AnswerDisplayName", "AnswerReputation", "AnswerGold", "AnswerSilver", "AnswerBronze"])

with open("data.csv", encoding = "utf-8") as handle:
	reader = csv.reader(handle, delimiter = ",", quotechar = "\"")
	ignored = next(reader, None)
	# @Improvement Check headers

	print("<div><h1>Contents</h1>\n<p>Questions are sorted by score</p>\n<ul>")

	count = 0
	for row in reader:
		print("<li>%s: <a href=\"#question%s\">%s</a></li>" % (row[headers.Score], row[headers.Id], row[headers.Title]))

		count += 1
		if count >= puzzleLimit:
			break

with open("data.csv") as handle:
	reader = csv.reader(handle, delimiter = ",", quotechar = "\"")
	ignored = next(reader, None)
	# @Improvement Check headers

	print("</ul>\n</div><div>\n\n<h1>Puzzles</h1>\n")

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

		# body = re.sub(r'<blockquote class="spoiler">(.*)</blockquote>', r'KwoC9R4okhg5qP1VqFU2spoileropenC7zVHSK1ZM3Jvkg9atqK<blockquote>\1</blockquote>KwoC9R4okhg5qP1VqFU2spoilercloseC7zVHSK1ZM3Jvkg9atqK', body, flags=re.MULTILINE|re.DOTALL)

		print("<h2><a name=\"question%s\">%s</a>: <a href=\"%s\">%s</a></h2>\n\n<p class=\"subtitle\">Asked by <a href=\"https://puzzling.stackexchange.com/users/%s\">%s#%s</a>, answered by <a href=\"https://puzzling.stackexchange.com/users/%s\">%s#%s</a></p>\n\n%s\n<a href=\"#solution%s\">Go to Solution</a>\n\n<hr />\n" % (row[headers.Id], row[headers.Score], row[headers.URL], row[headers.Title], row[headers.OwnerUserId], row[headers.DisplayName], row[headers.OwnerUserId], row[headers.AnswerOwnerId], row[headers.AnswerDisplayName], row[headers.AnswerOwnerId], body, row[headers.Id]))

		count += 1
		if count >= puzzleLimit:
			break

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

		# body = re.sub(r'<blockquote class="spoiler">(.*)</blockquote>', r'KwoC9R4okhg5qP1VqFU2spoileropenC7zVHSK1ZM3Jvkg9atqK<blockquote>\1</blockquote>KwoC9R4okhg5qP1VqFU2spoilercloseC7zVHSK1ZM3Jvkg9atqK', body, flags=re.MULTILINE|re.DOTALL)

		print("<h2><a name=\"solution%s\">%s</a>: <a href=\"%s\">%s</a></h2>\n\n<p class=\"subtitle\">Asked by <a href=\"https://puzzling.stackexchange.com/users/%s\">%s#%s</a>, answered by <a href=\"https://puzzling.stackexchange.com/users/%s\">%s#%s</a></p>\n\n%s\n<a href=\"#question%s\">Return to Question</a>\n\n<hr />\n" % (row[headers.Id], row[headers.Score], row[headers.URL], row[headers.Title], row[headers.OwnerUserId], row[headers.DisplayName], row[headers.OwnerUserId], row[headers.AnswerOwnerId], row[headers.AnswerDisplayName], row[headers.AnswerOwnerId], body, row[headers.Id]))

		count += 1
		if count >= puzzleLimit:
			break

	print("</div></body></html>")
