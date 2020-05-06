import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree


def get_continuous_chunks(text):
    # byte = text.encode()
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    # print(chunked)
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

try:
    f = open("./trucks.txt", "r")

    txt = f.read()
    print(get_continuous_chunks(txt))

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                print(chunk.label(), ' '.join(c[0] for c in chunk))

finally:
    if f:
        f.close()

