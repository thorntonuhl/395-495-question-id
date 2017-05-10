import nltk
from nltk.corpus import stopwords
import re

# how htis should work...
# input question as string
# extract key words from string
# search for keywords in 'database'
# return top matches
# keep extracting from there...

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# pos tag question
# make copy of question
# remove stop words
# extract nouns / compound nouns/ verbs/ adjectives?
#   put in array
# iteratively regex.search each term on database
# return list of narrowed DB results
# somehow narrow it down more...

# text = nltk.word_tokenize("What should I do if the head injury is bleeding heavily?\n")
# print  nltk.pos_tag(text)

stop_words = set(stopwords.words('english'))
def format_db(file):
    db = []
    with open(file) as text:
        for line in text:
            db.append(line)
    return db


def find_match(question):
    text = nltk.word_tokenize(question)
    tagged_q = nltk.pos_tag(text)
    keywords = []
    for tup in tagged_q: #JJ, NN, VB,
        word, pos = tup
        if 'JJ' in pos or 'NN' in pos or 'VB' in pos:
            if word not in stop_words: # to use or not to use stopwords???
                keywords.append(word)
    print "TAGGED SENTENCE: {}".format(tagged_q)
    print "KEYWORDS: {}".format(keywords)
    text = open('q_list.txt')
    string = text.read()
    text.close()
    matches = []
    for kw in keywords:
        matches += re.findall("[^\n]*{0}[^?]*\\?".format(kw), string)
    print "MATCHES: {}".format(matches)
    return 0

db = format_db('q_list.txt')
def main():
    question = raw_input("enter question: ")
    find_match(question)
main()


# print format_db('q_list.txt')