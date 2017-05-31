from VideoSearch import SearchYouTube
from ImageSearch import SearchImage
import webbrowser, json, pickle
from pprint import pprint
from text_matching import text_match_csv
from context import substitute
from context import is_deictic


VIDEO_CATEGORIES = ["what if",
    "what do",
    "what are",
    "what does",
    "when",
    "how",
    "should",
    "can"]

IMAGE_CATEGORIES = ["what is", "what are", "where", "whats", "what's", "who"]



def Answer(question, category, keywords, main_phrase, curr_step, file, CONTENT):
	answer = {}
	#Gather text
	answer_text = ""
        original_question = question

	#First, contextualize the question if needed
        print question, curr_step
	question = substitute(question, curr_step)
        print question
	real_question = ""
	print question
        for word in question:
		if type(word) is str or unicode:
                        print word
			real_question += str(word) + " "
                        print real_question
	question = real_question
        question = ''.join(question)
	#Now we check wiki-how csv to see if it exists already in the file
	text_match_attempt = text_match_csv(file, question)
	if text_match_attempt != -1:
		answer_text = text_match_attempt
	#Next we will check for keywords in our scraped content if not found in wiki-how.csv
	if text_match_attempt == -1 or question == "":
		for key in CONTENT:
			if len(frozenset(keywords).intersection(key)) > 2 and len(keywords) > 0:
				#print  str(frozenset(keywords).intersection(key)) + " buffer " +  str(frozenset(keywords)), key
				answer_text = CONTENT[key]
	has_image = False
	has_video = False
	#Next, return video or image if applicable
	print curr_step, is_deictic(original_question)
        if is_deictic(original_question):
		main_phrase = question
        print main_phrase, question
	if category in IMAGE_CATEGORIES or len(question.split()) == 1:
		has_image = True
		answer["type"] = "image"
		answer["mediaLink"] = (SearchImage(main_phrase))

	if not has_image:
		if category in VIDEO_CATEGORIES:
			has_video = True
			answer["type"] = "video"
			answer["mediaLink"] = (SearchYouTube(main_phrase))


	if not has_image and not has_video:
		answer["type"] = "image"
		answer["mediaLink"] = (SearchImage(' '.join(keywords)))

	if answer_text == "":
		answer_text = "Does this help?"
		
	answer["text"] = answer_text
	return json.dumps(answer, ensure_ascii=False)
