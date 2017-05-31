import nltk, string

def substitute(question, context):
    # deictic = ["it", "that", "there", "those", "this", "these"]
    singular_deictic = ["it", "it,", "it.", "it?", "it!", "that", "that.", "that,", "that!", "that?", "there", "there.", "there,", "there!", "there?", "this", "this.", "this,", "this?", "this!"]
    plural_deictic = ["those", "those,", "those!", "those.","those?", "these", "these,", "these!", "these?", "these."]
    q = question.lower().encode('ascii','ignore').translate(None, string.punctuation).split(' ')
    deictic = (set(singular_deictic).union(set(plural_deictic))).intersection(set(q))
    if not is_deictic(question):
        return [question]

    tagged_context = nltk.pos_tag(nltk.word_tokenize(context))
    replacements = []
    print tagged_context
    # find replacements
    for d in deictic:
        options = []

        if d in singular_deictic:
            for c in tagged_context:
                if c[1] == "NN" or c[1] == "NNP":
                    options.append(c[0])

        elif d in plural_deictic:
            for c in tagged_context:
                if c[1] == "NNS":
                    options.append(c[0])
        if len(options) == 1:
            replacements.append(options[0])
        else:
            replacements.append(options)
        if not replacements:
            return [question]
    # replace deictic words
    print replacements
    r = 0
    for d in deictic:
        q[q.index(d)] = replacements[r]
        r += 1
    return q

def is_deictic(question):
    singular_deictic = ["it", "it,", "it.", "it?", "it!", "that", "that.", "that,", "that!", "that?", "there", "there.", "there,", "there!", "there?", "this", "this.", "this,", "this?", "this!"]
    plural_deictic = ["those", "those,", "those!", "those.","those?", "these", "these,", "these!", "these?", "these."]
    q = question.lower().encode('ascii','ignore').translate(None, string.punctuation).split(' ')
    deictic = (set(singular_deictic).union(set(plural_deictic))).intersection(set(q))
    if deictic:
        return True
    else:
        return False
print substitute("what is that?", "2. Protect the Eye")
