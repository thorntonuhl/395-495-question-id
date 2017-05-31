import json, pickle
from AnswerID.Answering import Answer
from Categorization.auto_add_categories import auto_category
from Categorization.parser import get_keywords
from Categorization.parser import get_phrase_after_category

with open('Data_Collection/content.pickle', 'rb') as handle:
    CONTENT = pickle.load(handle) 

categories = ["who",
    "what if",
    "what do",
    "what are",
    "what does",
    "when",
    "where",
    "how",
    "should",
    "can", "what is", "what are", "whats", "what's"]


def test(question, curr_step, file):
	category = ""
	#get category, keywords, and main phrase from the question
	for cat in categories:
		if cat in question.lower():
			category = cat

	keywords = set()
	words = get_keywords(question)
	for word in words:
		keywords.add(word[0].lower())
	keywords = frozenset(keywords)  
	main_phrase = get_phrase_after_category(question, category).lstrip()
	#Answer question
	answer = Answer(question, category, keywords, main_phrase, curr_step, file, CONTENT)

	#return Answer as a dictionary
	return answer

print test("how do I treat a bullet wound")
#Tests for direct questions in wikihow
print test("Why isn't the child's throat checked for objects before compression is started?", "jib jab", "Data/wikihow.csv")
print test("How do I help a person who is choking in his sleep?", "jib jab", "Data/wikihow.csv")

#Testing for overall functionality
print test("How do I give CPR?", "jib jab", "Data/wikihow.csv")
print test("Regarding my child, who should I be asking to know how to effectively treat them", "child caring","Data/wikihow.csv" )

print test("What do I do with it", "leg is bleeding", "Data/wikihow.csv")
print test("How do I treat a broken leg", "what hurts", "Data/wikihow.csv")


print test("How do I perform CPR", "what hurts", "Data/wikihow.csv")
print test("How do I perform CPR on an adult", "what hurts", "Data/wikihow.csv")

#Nonsense
print test("apple stuck walnut", "leg hurting", "Data/wikihow.csv")
print test("What is the deal with airline food", "leg hurting", "Data/wikihow.csv")
