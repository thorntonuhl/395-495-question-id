import json, pickle
from flask import Flask, request
from AnswerID.Answering import Answer
from Categorization.auto_add_categories import auto_category
from Categorization.parser import get_keywords
from Categorization.parser import get_phrase_after_category
from flask_cors import CORS, cross_origin


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



app = Flask(__name__)
CORS(app)

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
	data = request.get_json()

	#extract question and title of current step from payload
	question = data["userText"]
        innerIndex = data["innerIndex"]
        print question
        try:
	    curr_step = data["step"]["substeps"][innerIndex]["text"]
        except:
            curr_step = data["step"]["text"]

	category = ""
	#get category, keywords, and main phrase from the question
	has_category = False
	for cat in categories:
		if cat in question.lower():
			has_category = True
			category = cat
	if not has_category:
		answer = {}
		answer["text"] = "Sorry, I couldn't understand"
		answer["type"] = ""
		answer["mediaLink"] = ""
		return json.dumps(answer, ensure_ascii=False)

	keywords = set()
	words = get_keywords(question)
	for word in words:
		keywords.add(word[0].lower())
	keywords = frozenset(keywords)  
	main_phrase = get_phrase_after_category(question, category).lstrip()
	#Answer question
	answer = Answer(question, category, keywords, main_phrase, curr_step, "Data/wikihow.csv", CONTENT)

	#return Answer as a dictionary
	return answer



if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)
