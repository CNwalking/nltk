import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

file_url = "./ABCNewsArticle/Are we using ventilators too much?.txt"

def get_continuous_chunks(text):
    # byte = text.encode()
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    if continuous_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)

    return continuous_chunk

# open a file
try:
    f = open(file_url, "r")
    story = f.read()
    # two steps to format the article
    temp = story.replace('\\n', '').replace('[', '').replace(']', '')\
        .replace("'", '').replace('"', '').replace("None,", '')
    # end format
    # An optional qualifier (DT),followed by several adjectives(JJ),
    # and then followed by a noun (NN), should form a noun phrase(NP)
    print(get_continuous_chunks(temp))
    for sent in nltk.sent_tokenize(temp):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                print(chunk.label(), ' '.join(c[0] for c in chunk))

finally:
    if f:
        f.close()