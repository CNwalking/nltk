import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk.corpus import wordnet as wn

word_sets = wn.synsets('china')
print('similar words set:', word_sets)
print('similar words set contains:', [set.lemma_names() for set in word_sets])
# output of contains: [['China', "People's_Republic_of_China", 'mainland_China',
# 'Communist_China', 'Red_China', 'PRC', 'Cathay'], ['china'], ['Taiwan', 'China',
# 'Nationalist_China', 'Republic_of_China'], ['chinaware', 'china']]
print('similar words set details:', [set.definition() for set in word_sets])
print('similar words set examples:', [set.examples() for set in word_sets])

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

test_dict = {}
test_dict = check_words(test_dict, "china")
print("1111", test_dict)
test_dict = check_words(test_dict, "Nationalist China")
print("2222", test_dict)