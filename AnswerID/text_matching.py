import nltk
from nltk.corpus import stopwords
import re
import csv

from match_helper import match_stems, match_lemmas, get_lemmas_ratio

# use on wikihow.csv, store in dict. Use text-matcher to find matching q, pull up corresponding answer

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

def get_keywords(question):
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
    # print "TAGGED SENTENCE: {}".format(tagged_q)
    # print "KEYWORDS: {}".format(keywords)
    return keywords

def match_w_str(question,keywords,string):
    matches = []
    for kw in keywords:
        # matches += '\n'.join(re.findall("[^\n]*{0}[^?]*\\?".format(kw), string))
        matches += re.findall("[^\n]*{0}[^?]*\\?".format(kw), string, re.IGNORECASE)
    matches = "\n".join(matches)
    # print "MATCHES: {}".format(matches)
    return matches

def find_match(question, keywords, matches):
    if len(matches) == 0:
        return -1
    keyword_len = len(keywords)
    if keyword_len > 1:
        bigram_matches = []
        # check for direct bigram matches in remaining sentences
        for i in range(0,keyword_len-1):
            bigram = "{0} {1}".format(keywords[i],keywords[i+1])
            bigram_matches += list(set(re.findall("[^\n]*{0}[^?]*\\?".format(bigram), matches, re.IGNORECASE)))
        if len(bigram_matches) == 0:
            ret = matches.split("\n")
        else: # if no matches, just search for BOTH keywords in each line...
            ret = bigram_matches
    else: # should we try to find synonyms on keywords?
        ret = matches.split("\n")
    ret = [q.lower() for q in ret]
    # print matches
    if len(ret) == 1:
        # print "only 1 match"
        response = ret[0]
    elif question.lower() in ret:
        # print "direct match"
        response = question.lower()
    else: # enter loop to 'match_stems' for more direct match
        # print "using stems"
        stem_matches = []
        # for q in ret:
        #     # using 'match_stems' NOTE: stemming is poor (e.g. removing 'ed' ending from 'nosebleed', etc.)
        #     # if match_stems(question, q) == True:
        #     #     stem_matches.append(q)
        #     # using simple ratio calculator
        #     print q
        stem_matches = [q for q in ret if get_ratio(keywords, get_keywords(q))]
        if len(stem_matches) == 0:
            stem_matches = [q for q in ret if get_ratio(keywords,get_keywords(q),0.3)]
            if len(stem_matches) == 0:
                stem_matches = [q for q in ret if get_ratio(keywords,get_keywords(q),0.25)]
        # print "Matches: {0}".format(stem_matches)
        # ISSUES: kind of need stemming... (e.g. 'how do i treat a nosebleed', vs 'how do i... nosebleedS')
        if len(stem_matches) == 1:
            response = stem_matches[0]
        elif len(stem_matches) == 0:
            response = ret[0]
        else:
            # print "using lemmas"
            best = -0.1
            bestq = ''
            # print stem_matches
            for q in stem_matches:
                ratio = get_lemmas_ratio(question, q)
                if ratio > best:
                    best = ratio
                    bestq = q
            response = bestq
    if response < 0:
        return -1
    return response

def get_ratio(lst1, lst2, threshold=0.5):
    # takes in two lists of keywords, measures jaccard distance
    ratio = len(set(lst1).intersection(lst2)) / float(len(set(lst1).union(lst2)))
    # print "{0} -- {1}".format(lst1, lst2)
    # print ratio
    return (ratio >= threshold)

def txt_to_str(file):
    with open(file) as f:
        return f.read()

def csv_to_dict(file):
    with open(file) as f:
        reader = csv.reader(f)
        lst = list(reader)[1:]
        d = dict([line[0:2] for line in lst if len(line) > 0])
        d = {q.lower().strip('"'): a for q,a in d.iteritems() if len(a) != 0}
        string = '\n'.join([q for q, a in d.iteritems()])
    return d, string

def main():
    question = raw_input("enter question: ")
    keywords = get_keywords(question)
    first_matches = match_w_str(question,keywords, txt_to_str('new_q_list.txt'))

    return find_match(question,keywords, first_matches)

def text_match_csv(file, question):
    # takes in .csv file to be read
    # returns -1 for error, answer on success. really depends on thoroughness of db..
    keywords = get_keywords(question)
    dict, qstring = csv_to_dict(file)
    first_matches = match_w_str(question,keywords, qstring) #txt_to_str('new_q_list.txt'))
    match = find_match(question, keywords, first_matches)
    if match == -1: #failure
        return match
    else:
        try:
            return dict[match]
        except:
            return ""


#text_match_csv('data/wikihow.csv')
# main()



# make q_list file with wikihow questions... when finding a match just regex the exact match w/ db.. fuck
# print csv_to_dict('data/wikihow.csv')

# match_lemmas('how do i identify a heart attack?', 'how can i tell if someone is having a heart attack?')
# match_lemmas('how do i identify a heart attack?', 'what is a heart attack?')
# get_ratio(get_keywords('how can i tell if someone is having a heart attack?'), get_keywords('what is a heart attack?'))

# use my pos tagger/ keyword extracter, compare keywords to remaining options in DB, use lemma or stem matcher
# from 'sentence-matcher.py' to generate jaccard similarity
    # need modifications to take in a mere LIST of keywords for 1 input, rather than a sentence