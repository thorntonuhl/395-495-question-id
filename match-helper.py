# resource: Bommarito Consulting LLC: Approximate Sentence Matching in Python
# Imports
import nltk.corpus
from nltk import wordpunct_tokenize
import nltk.stem.snowball
from nltk.corpus import wordnet
import string

# nltk.download('all')

# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def get_wordnet_pos(pos_tag):
    if pos_tag[1].startswith('J'):
        return (pos_tag[0], wordnet.ADJ)
    elif pos_tag[1].startswith('V'):
        return (pos_tag[0], wordnet.VERB)
    elif pos_tag[1].startswith('N'):
        return (pos_tag[0], wordnet.NOUN)
    elif pos_tag[1].startswith('R'):
        return (pos_tag[0], wordnet.ADV)
    else:
        return (pos_tag[0], wordnet.NOUN)

# Create tokenizer and stemmer
lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

def match_lemmas(a, b, threshold=0.5):
    """Check if a and b are matches."""
    pos_a = map(get_wordnet_pos, nltk.pos_tag(wordpunct_tokenize(a)))
    pos_b = map(get_wordnet_pos, nltk.pos_tag(wordpunct_tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_b \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]

    # Calculate Jaccard similarity
    print pos_a, pos_b
    print lemmae_a, lemmae_b

    ratio = len(set(lemmae_a).intersection(lemmae_b)) / float(len(set(lemmae_a).union(lemmae_b)))
    print ratio
    return (ratio >= threshold)




stemmer = nltk.stem.snowball.SnowballStemmer('english')

def match_stems(a, b, threshold=0.5):
    """Check if a and b are matches."""
    tokens_a = [token.lower().strip(string.punctuation) for token in wordpunct_tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    tokens_b = [token.lower().strip(string.punctuation) for token in wordpunct_tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    stems_a = [stemmer.stem(token) for token in tokens_a]
    stems_b = [stemmer.stem(token) for token in tokens_b]

    print stems_a, stems_b
    # Calculate Jaccard similarity
    ratio = len(set(stems_a).intersection(stems_b)) / float(len(set(stems_a).union(stems_b)))
    print ratio
    return (ratio >= threshold)

# a = "asthma symptoms?"
# b = "What is asthma?"
# c = "Very long ago in the eighteenth century, many scholars regarded man as merely a clockwork automaton."
# d = "In the eighteenth century it was often convenient to regard man as a clockwork automaton."
# print match_stems(a, b)