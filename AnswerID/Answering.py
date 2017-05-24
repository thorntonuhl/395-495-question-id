from VideoSearch import SearchYouTube
from ImageSearch import SearchImage
import webbrowser, json
from pprint import pprint



VIDEO_CATEGORIES = ["What if", "Should I", "What should I do if", "How do I", "How can I tell if", "Do I", "What do I do if", "Can I give them",
"How do I treat", "When should I call 911?", "Should I try", "How long should I", "How will I know if", "What does"]

IMAGE_CATEGORIES = ["What is", "What are the signs and symptoms of"]

def Answer(question, category, keywords, main_phrase, curr_step):
	answer = {}
	#First gather text
	answer_text = "Here's what you should do"




	has_image = False
	has_video = False
	#Next, return video or image if applicable
	for category in IMAGE_CATEGORIES:
		if category in question:
			has_image = True
			answer["type"] = "image"
			answer["mediaLink"] = (SearchImage(main_phrase))

	if not has_image:
		for category in VIDEO_CATEGORIES:
			if category in question:
				has_video = True
				answer["type"] = "video"
				answer["mediaLink"] = (SearchYouTube(main_phrase))


	if not has_image and not has_video:
		answer["type"] = "none"
		answer["mediaLink"] = "none"

	answer["text"] = answer_text
	return json.dumps(answer, ensure_ascii=False)




