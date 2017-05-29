from VideoSearch import SearchYouTube
from ImageSearch import SearchImage
import webbrowser, json, pickle
from pprint import pprint
from text_matching import text_match_csv
from context import substitute


VIDEO_CATEGORIES = ["who",
    "what if",
    "what do",
    "what are",
    "what does",
    "when",
    "how",
    "should",
    "can"]

IMAGE_CATEGORIES = ["what is", "what are", "where", "whats", "what's"]



def Answer(question, category, keywords, main_phrase, curr_step, file, CONTENT):
	answer = {}
	#Gather text
	answer_text = ""

	#First, contextualize the question if needed
	question = ' '.join(substitute(question, curr_step))
	#Now we check wiki-how csv to see if it exists already in the file
	text_match_attempt = text_match_csv(file, question)
	if text_match_attempt != -1:
		answer_text = text_match_attempt
	#Next we will check for keywords in our scraped content if not found in wiki-how.csv
	if text_match_attempt == -1 or question == "":
		for key in CONTENT:#sentence[0] is keywords, sentence[1] is actual sentence
			if len(frozenset(keywords).intersection(key)) == len(frozenset(keywords)) and len(keywords) > 0 and abs(len(frozenset(keywords))- len(key)) < 3:
				print  str(frozenset(keywords).intersection(key)) + " buffer " +  str(frozenset(keywords)), key
				answer_text = CONTENT[key]
	has_image = False
	has_video = False
	#Next, return video or image if applicable
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
		answer["type"] = "none"
		answer["mediaLink"] = "none"

	if answer_text == "":
		answer_text = "Sorry, does this help?"
		
	answer["text"] = answer_text
	return json.dumps(answer, ensure_ascii=False)
