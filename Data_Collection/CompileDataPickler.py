from nltk import tokenize
import os, csv


content = []

for filename in os.listdir('../Data'):
	with open('../Data/' + filename, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in reader:
			content.append(','.join(row))


#for filename in os.listdir('../Data'):
#	with open("../Data/" + filename, "r") as ins:
#	    for line in ins:
#	        content.append(line)

parsed_answers = []
for line in content:
	line = tokenize.sent_tokenize(line)
	newline = []
	for sentence in line:
		sentence = sentence.split("?,")
		if len(sentence) > 1:
			for part in sentence:
				newline.append(str(part))
			parsed_answers.append(newline)
		else:
			newline.append(sentence)
			parsed_answers.append(str(newline))


print parsed_answers[2029]

