import nltk
from nltk.corpus import stopwords
import re
from match_helper import match_stems, match_lemmas, get_lemmas_ratio


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

def get_keywords(question):
    text = nltk.word_tokenize(question.lower())
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
    # print "TAGGED SENTENCE: {}".format(tagged_q)
    # print "KEYWORDS: {}".format(keywords)
    return keywords

def match_w_file(question,keywords,file):
    matches = []
    with open(file) as text:
        string = text.read()
        text.close()
        for kw in keywords:
            # matches += '\n'.join(re.findall("[^\n]*{0}[^?]*\\?".format(kw), string))
            matches += re.findall("[^\n]*{0}[^?]*\\?".format(kw), string)

    matches = "\n".join(matches)
    # print "MATCHES: {}".format(matches)
    return matches

def find_match(question, keywords, matches):
    keyword_len = len(keywords)
    if keyword_len > 1:
        bigram_matches = []
        # check for direct bigram matches in remaining sentences
        for i in range(0,keyword_len-1):
            bigram = "{0} {1}".format(keywords[i],keywords[i+1])
            bigram_matches += list(set(re.findall("[^\n]*{0}[^?]*\\?".format(bigram), matches)))
        if len(bigram_matches) == 0:
            ret = matches.split("\n")
        else: # if no matches, just search for BOTH keywords in each line...

            ret = bigram_matches
    else: # should we try to find synonyms on keywords?
        ret = matches.split("\n")
    ret = [q.lower() for q in ret]
    # print ret
    if len(ret) == 1:
        print "only 1 match"
        response = ret[0]
    elif question.lower() in ret:
        print "direct match"
        response = question.lower()
    else: # enter loop to 'match_stems' for more direct match
        print "using stems"
        stem_matches = []
        for q in ret:
            # using 'match_stems' NOTE: stemming is poor (e.g. removing 'ed' ending from 'nosebleed', etc.)
            # if match_stems(question, q) == True:
            #     stem_matches.append(q)
            # using simple ratio calculator
            if get_ratio(keywords, get_keywords(q)):
                stem_matches.append(q)
        print "Matches: {0}".format(stem_matches)
        # ISSUES: kind of need stemming... (e.g. 'how do i treat a nosebleed', vs 'how do i... nosebleedS')
        if len(stem_matches) == 1:
            response = stem_matches[0]
        else:
            print "using lemmas"
            best = -0.1
            for q in stem_matches:
                if get_lemmas_ratio(question, q) > best:
                    best = q
            response = best
    print "Identified question:"
    if response < 0:
        return "No match found"
    return response

def get_ratio(lst1, lst2, threshold=0.5):
    # takes in two lists of keywords, measures jaccard distance
    ratio = len(set(lst1).intersection(lst2)) / float(len(set(lst1).union(lst2)))
    # print "{0} -- {1}".format(lst1, lst2)
    # print ratio
    return (ratio >= threshold)

def main():
    question = raw_input("enter question: ")
    keywords = get_keywords(question)
    first_matches = match_w_file(question,keywords,'new_q_list.txt')

    return find_match(question,keywords, first_matches)

print main()

# match_lemmas('how do i identify a heart attack?', 'how can i tell if someone is having a heart attack?')
# match_lemmas('how do i identify a heart attack?', 'what is a heart attack?')
# get_ratio(get_keywords('how can i tell if someone is having a heart attack?'), get_keywords('what is a heart attack?'))

# use my pos tagger/ keyword extracter, compare keywords to remaining options in DB, use lemma or stem matcher
# from 'sentence-matcher.py' to generate jaccard similarity
    # need modifications to take in a mere LIST of keywords for 1 input, rather than a sentence