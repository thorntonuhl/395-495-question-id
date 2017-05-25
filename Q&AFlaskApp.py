import json
from flask import Flask, request
from AnswerID.Answering import Answer
from Categorization.auto_add_categories import auto_category
from Categorization.parser import get_keywords
from Categorization.parser import get_phrase_after_category
from flask_cors import CORS, cross_origin



app = Flask(__name__)

# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
# app.config['CORS_HEADERS'] = 'Content-Type'
#
# cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

# @app.route('/foo', methods=['POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# def foo():
#     return request.json['inputVar']


@app.route("/", methods=['POST', 'GET'])
def hello():
	if request.method == 'GET':
		return 'hello there'
	data = json.load(request.get_json())
	print data

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
    app.run(host='0.0.0.0', port = 5000)
