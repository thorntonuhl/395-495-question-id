import nltk
from nltk.corpus import stopwords


# pre-process for contractions and singular/plural
def get_category(question, categories = [
            "Who",
            "What if",
            "What is",
            "What are"
            "What do",
            "What are",
            "What does",
            "When",
            "Where",
            "How",
            "Should",
            "Can",
            # no why
]):
    tag = -1
    counter = 0
    #While loop for n question substrings
    while counter < len(question):
        #If substring in category question list
        if question[0:counter] in categories:
            tag_finder = 0
            #If we have the question category, tag it
            #Initial tag = index in question list
            while tag_finder < len(categories):
                if question[0:counter] == categories[tag_finder]:
                    tag = tag_finder
                    tag_finder = len(categories) + 1
                else:
                    tag_finder = tag_finder + 1
            counter = len(question) + 1
        else:
            #If we're at the very end and it hasn't been found, kill function
            if counter == len(question) - 1:
                print question , "***Question form not found***\n"
                return "Uncategorized"

            #Otherwise just hit next substring
            counter = counter + 1
    # print "Question:" , question , "Question form: \""+ categories[tag]+ "________?\"\n"
    return categories[tag]

def get_keywords(question):
    stop_words = set(stopwords.words('english'))

    text = nltk.word_tokenize(question)
    tagged_q = nltk.pos_tag(text)
    keywords = []
    for tup in tagged_q: #JJ, NN, VB,
        word, pos = tup
        if 'JJ' in pos or 'NN' in pos or 'VB' in pos:
            if word not in stop_words: # to use or not to use stopwords???
                keywords.append((word,pos))
    # print "TAGGED SENTENCE: {}".format(tagged_q)
    # print "KEYWORDS: {}".format(keywords)
    return keywords

def get_phrase_after_category(question, category):
    try:
        return question.split(category, 1)[1]
    except:
        return question


#while True:
#    question = raw_input(">> ")
#    c = get_category(question)
#    k = get_keywords(question)
#    print "CATEGORY: ", c
#    print "KEYWORDS: ", k
print set(get_keywords("What is a femur")).intersection([('femur', 'NN')])