import nltk, string

def substitute(question, context):
    # deictic = ["it", "that", "there", "those", "this", "these"]
    print question
    singular_deictic = ["it","it!","it?", "it,","it.", "that", "that!", "that?", "that.", "that,", "there", "there!", "there?", "there,", "there.", "this", "this!", "this?", "this.", "this,"]
    plural_deictic = ["those", "these", "those?", "these?", "those,", "these,", "these.", "those.", "these!", "those!"]
    if type(question) is str:
        q = question.lower().translate(None, string.punctuation).split(' ')
    else:
        q = question.lower().translate(string.punctuation).split(' ')
    deictic = (set(singular_deictic).union(set(plural_deictic))).intersection(set(q))
    if not deictic:
        return [question. "?"]

    tagged_context = nltk.pos_tag(nltk.word_tokenize(context))
    replacements = []
    # find replacements
    for d in deictic:
        options = []

        if d in singular_deictic:
            for c in tagged_context:
                if c[1] == "NN":
                    options.append(c[0])

        elif d in plural_deictic:
            for c in tagged_context:
                if c[1] == "NNS":
                    options.append(c[0])

        if len(options) == 1:
            replacements.append(options[0])
        else:
            replacements.append(options)

    # replace deictic words
    r = 0
    for d in deictic:
        q[q.index(d)] = replacements[r]
        r += 1

    return " ".join(str(x) for x in q) + "?"
