import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import json
from nltk.corpus import wordnet as wn

file_url = "./ABCNewsArticle/Are we using ventilators too much?.txt"

def check_words(dict, word):
    # the word in wordnet will concat with '_' in every single word
    true_word = str(word).replace(" ", "_")
    # Check synonyms for each word
    for word_exist in dict:
        for same_words_set in wn.synsets(word_exist):
            for word in same_words_set.lemma_names():
                if true_word == word:
                    # which means they are the same words
                    dict[word_exist] += 1
                    return dict
    dict[word] = 1
    return dict

# method in nltk_trucks.py, which used to extract the entities in the article
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
    org_dict = {}
    per_dict = {}
    gpe_dict = {}
    data = {}
    data["ORGANIZATION"] = org_dict
    data["GPE"] = gpe_dict
    data["PERSON"] = per_dict
    times = 1
    entity_sets = get_continuous_chunks(temp)
    print(get_continuous_chunks(temp))
    for sent in nltk.sent_tokenize(temp):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label'):
                word = ' '.join(c[0] for c in chunk)
                word_type = chunk.label()
                if word_type == "ORGANIZATION":
                    org_dict = check_words(org_dict, word)
                if word_type == "GPE":
                    gpe_dict = check_words(gpe_dict, word)
                if word_type == "PERSON":
                    # person name should not be checked
                    per_dict.update({word: times})
                # print(chunk.label(), ' '.join(c[0] for c in chunk))

    jsonStr = json.dumps(data)
    print(jsonStr)

finally:
    if f:
        f.close()