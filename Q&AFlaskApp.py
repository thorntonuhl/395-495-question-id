import json
from flask import Flask
from AnswerID.Answering import Answer
from Categorization.auto_add_categories import auto_category
from Categorization.parser import get_keywords
from Categorization.parser import get_phrase_after_category



app = Flask(__name__)



@app.route("/")
def hello():

	SRC = "fattypayload.json"

	#load the parser's payload
	with open(SRC) as data_file:    
	    data = json.load(data_file)

	#extract question and title of current step from payload
	question = data["userText"]
	curr_step = data["step"]["text"]


	#get category, keywords, and main phrase from the question
	category = auto_category(question)
	keywords = get_keywords(question)
	main_phrase = get_phrase_after_category(question, category).lstrip()

	#Answer question
	answer = Answer(question, category, keywords, main_phrase, curr_step)

	#return Answer as a dictionary
	return answer

if __name__ == "__main__":
    app.run()