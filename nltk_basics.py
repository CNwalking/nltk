import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk import sent_tokenize, word_tokenize, pos_tag
text = "Text and Vision Intelligence is a course that deal with interpreting texts and images computationally. This has become increasingly important in " \
       "the last decade due to a large amount of texts and images online as well offline."
print(sent_tokenize(text))
print(word_tokenize(text))
print(pos_tag(word_tokenize(text)))
