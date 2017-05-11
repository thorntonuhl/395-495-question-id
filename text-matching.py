import nltk
from nltk.corpus import stopwords
import re


# how this should work...
# input question as string
# extract key words from string
# search for keywords in 'database'
# return top matches
# keep extracting from there...

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

# text = nltk.word_tokenize("What should I do if the head injury is bleeding heavily?\n")
# print  nltk.pos_tag(text)

# perform search on a categorized database... as opposed to general DB
# need to handle 'someone'
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
    # extract keywords
    for tup in tagged_q: #JJ, NN, VB,
        word, pos = tup
        if 'JJ' in pos or 'NN' in pos or 'VB' in pos:
            if word not in stop_words: # to use or not to use stopwords???
                keywords.append(word)

    if 'someone' in keywords:
        keywords.remove('someone')
    # print outputs
    print "TAGGED SENTENCE: {}".format(tagged_q)
    print "KEYWORDS: {}".format(keywords)
    # find matches in DB
    with open('q_list.txt') as text:
        string = text.read()
        text.close()
        matches = []
        for kw in keywords:
            # matches += '\n'.join(re.findall("[^\n]*{0}[^?]*\\?".format(kw), string))
            matches += re.findall("[^\n]*{0}[^?]*\\?".format(kw), string)

    matches = "\n".join(matches)
    # print "MATCHES: {}".format(matches)

    # # PHASE 2
    keyword_len = len(keywords)
    more_matches = []
    if keyword_len > 1:
        for i in range(0,keyword_len-1):
            bigram = "{0} {1}".format(keywords[i],keywords[i+1])
            more_matches += list(set(re.findall("[^\n]*{0}[^?]*\\?".format(bigram), matches)))
        if len(more_matches) == 0:
            return matches.split("\n")
        else:
            return more_matches
        # if no matches, just search for BOTH keywords in each line...
    else:
        return matches.split("\n")

# db = format_db('q_list.txt')
def main():
    question = raw_input("enter question: ")
    find_match(question)

print main()

# print format_db('q_list.txt')