import itertools, pickle


VIDEO_CATEGORIES = ["What if", "Should I", "What should I do if", "How do I", "How can I tell if", "Do I", "What do I do if", "Can I give them",
"How do I treat", "When should I call 911?", "Should I try", "How long should I", "How will I know if", "What does", "What do", "When", "How", "Should", "Can"]

IMAGE_CATEGORIES = ["What is", "Signs and symptoms of", "Who", "What are", "What does", "Where"]

NEW_VIDEO_CATEGORIES = []

NEW_IMAGE_CATEGORIES = []


for i in VIDEO_CATEGORIES:
	if len(i.replace(" ", "")) < 20:
		NEW_VIDEO_CATEGORIES.append(map(''.join, itertools.product(*((c.upper(), c.lower()) for c in i))))
	else:
		NEW_VIDEO_CATEGORIES.append(i)

for i in IMAGE_CATEGORIES:
	if len(i.replace(" ", "")) < 20:
		NEW_IMAGE_CATEGORIES.append(map(''.join, itertools.product(*((d.upper(), d.lower()) for d in i))))
	else:
		NEW_IMAGE_CATEGORIES.append(i)

NEW_VIDEO_CATEGORIES = [val for sublist in NEW_VIDEO_CATEGORIES for val in sublist]
NEW_IMAGE_CATEGORIES = [val for sublist in NEW_IMAGE_CATEGORIES for val in sublist]


Vid_cats = list(set(NEW_VIDEO_CATEGORIES))
Vid_Dict = {}


img_cats = list(set(NEW_IMAGE_CATEGORIES))
img_Dict = {}

for i in Vid_cats:
	Vid_Dict[i] = 1


for i in img_cats:
	img_Dict[i] = 1


with open('video_img_categories.pickle', 'wb') as handle:
    pickle.dump([Vid_Dict, img_Dict], handle, protocol=pickle.HIGHEST_PROTOCOL)

