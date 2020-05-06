import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk.corpus import wordnet as wn

word_sets = wn.synsets('china')
print('similar words set:', word_sets)
print('similar words set contains:', [set.lemma_names() for set in word_sets])
print('similar words set details:', [set.definition() for set in word_sets])
print('similar words set examples:', [set.examples() for set in word_sets])
