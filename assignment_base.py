import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
import json
import os
from nltk.corpus import wordnet as wn

file_url = "./ABCNewsArticle/Are we using ventilators too much?.txt"

def check_words(dict, word):
    # the word in wordnet will concat with '_' in every single word
    true_word = str(word).replace(" ", "_")
    # Check synonyms for each word
    for word_exist in dict:
        # get the sets of Synonyms
        for same_words_set in wn.synsets(word_exist):
            for same_word in same_words_set.lemma_names():
                if true_word == same_word or same_word == str(word).lower() or same_word == str(word).lower().replace("s", ""):
                    # which means they are the same words
                    dict[word_exist] += 1
                    return dict
    dict[word] = 1
    return dict

# open a file
try:
    fileList = os.listdir("./ABCNewsArticle")
    for file in fileList:
        file_position = "./ABCNewsArticle/" + file
        with open(file_position, "r") as f:
            story = f.read()
            # two steps to format the article
            temp = story.replace('\\n', '').replace('[', '').replace(']', '')\
                .replace("'", '').replace('"', '').replace("None,", '')
            # end format
            org_dict = {}
            per_dict = {}
            gpe_dict = {}
            data = {}
            times = 1
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
            # Sort the named entity by desc
            org_dict = sorted(org_dict.items(), key=lambda item: item[1], reverse=True)
            gpe_dict = sorted(gpe_dict.items(), key=lambda item: item[1], reverse=True)
            data["ORGANIZATION"] = org_dict
            data["GPE"] = gpe_dict
            data["PERSON"] = per_dict
            # format data to json
            jsonStr = json.dumps(data)
            print(jsonStr)

finally:
    if f:
        f.close()