import json
from flask import Flask
from AnswerID.Answering import Answer
from Categorization.auto_add_categories import auto_category
from Categorization.parser import get_keywords
from Categorization.parser import get_phrase_after_category



app = Flask(__name__)

question = "How do I walk my dog?"

@app.route("/")
def hello():

	category = auto_category(question)
	keywords = get_keywords(question)
	main_phrase = get_phrase_after_category(question, category).lstrip()
	answer = Answer(question, category, keywords, main_phrase)

	return str(answer)

if __name__ == "__main__":
    app.run()