#!/usr/bin/env python3

import csv

class DictEnum():
	data = {}

	def __init__(self, data):
		for pointer in range(len(data)):
			self.data[data[pointer]] = pointer

	def __getattr__(self, name):
		return self.data[name]

puzzleLimit = 50

print("<style>.spoiler {background: #ccc; color: transparent;} .spoiler:hover {color: black;}</style>")

print("The (Unoffical) Stack Exchange Puzzle Book\n==========================================\n\n\n* %d of the best puzzles and solutions submitted to puzzling.SE.\n* Arranged by [Matthew Consterdine](https://consto.uk/).\n* [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).\n\n***\n" % puzzleLimit)

headers = DictEnum(["Id", "URL", "Score", "ViewCount", "AnswerCount", "FavoriteCount", "Title", "Tags", "Body", "CreationDate", "OwnerUserId", "DisplayName", "Reputation", "Gold", "Silver", "Bronze", "AnswerId", "AnswerScore", "AnswerBody", "AnswerCreationDate", "AnswerOwnerId", "AnswerDisplayName", "AnswerReputation", "AnswerGold", "AnswerSilver", "AnswerBronze"])

with open("data.csv") as handle:
	reader = csv.reader(handle, delimiter = ",", quotechar = "\"")
	ignored = next(reader, None)
	# @Improvement Check headers

	print("# Contents\n")

	count = 0
	for row in reader:
		# @Improvement replace h2>h3, h3>h4 and so on to respect ordering
		print("* %s Votes - [%s](#question%s)" % (row[headers.Score], row[headers.Title], row[headers.Id]))

		count += 1
		if count >= puzzleLimit:
			break

with open("data.csv") as handle:
	reader = csv.reader(handle, delimiter = ",", quotechar = "\"")
	ignored = next(reader, None)
	# @Improvement Check headers

	print("\n***\n\n# Puzzles\n")

	count = 0
	for row in reader:
		# @Improvement replace h2>h3, h3>h4 and so on to respect ordering
		print("## <a name=\"question%s\"></a>%s Votes - [%s](%s)\n\n~~Asked by [%s (%srep)](https://puzzling.stackexchange.com/users/%s) on %s~~\n\n~~Answered by [%s (%srep)](https://puzzling.stackexchange.com/users/%s) on %s~~\n\n%s\n[Go to Solution](#solution%s)\n\n***\n" % (row[headers.Id], row[headers.Score], row[headers.Title], row[headers.URL], row[headers.DisplayName], row[headers.Reputation], row[headers.OwnerUserId], row[headers.CreationDate], row[headers.AnswerDisplayName], row[headers.AnswerReputation], row[headers.AnswerOwnerId], row[headers.AnswerCreationDate], row[headers.Body], row[headers.Id]))

		count += 1
		if count >= puzzleLimit:
			break

with open("data.csv") as handle:
	reader = csv.reader(handle, delimiter = ",", quotechar = "\"")
	ignored = next(reader, None)
	# @Improvement Check headers

	print("# Solutions\n")

	count = 0
	for row in reader:
		print("## <a name=\"solution%s\"></a>%s Votes - [%s](%s)\n\n~~Asked by [%s (%srep)](https://puzzling.stackexchange.com/users/%s) on %s~~\n\n~~Answered by [%s (%srep)](https://puzzling.stackexchange.com/users/%s) on %s~~\n\n%s\n[Return to Question](#question%s)\n\n***\n" % (row[headers.Id], row[headers.Score], row[headers.Title], row[headers.URL], row[headers.DisplayName], row[headers.Reputation], row[headers.OwnerUserId], row[headers.CreationDate], row[headers.AnswerDisplayName], row[headers.AnswerReputation], row[headers.AnswerOwnerId], row[headers.AnswerCreationDate], row[headers.AnswerBody], row[headers.Id]))

		count += 1
		if count >= puzzleLimit:
			break

	print("Thanks for reading!")
