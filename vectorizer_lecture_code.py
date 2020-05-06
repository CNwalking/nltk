"""Convert words to vectores tha can be used with classifiers"""

from sklearn.feature_extraction.text import CountVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog."]
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
print(vectorizer.vocabulary_)
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print(vector.shape)
print(vector.toarray())
print(vectorizer.vocabulary_)

#Try another sentence
text2 = ["the quick puppy"]
vector = vectorizer.transform(text2)
print(vector.toarray())

"""BOW model is not very effeictive. represents presence or absence of a token in a document.
Lets keep count of tokens in a document

Using TFIDF instead of BOW, TFIDF also takes into account the frequency instead of just the occurance.
calculated as:
Term frequency = (Number of Occurrences of a word)/(Total words in the document) : normalizes based on the size of the document.
IDF(word) = Log((Total number of documents)/(Number of documents containing the word)) : reduces the impact  words that are common across documents, eg. the.
TF-IDF is the product of the two."""


# from sklearn.feature_extraction.text import TfidfVectorizer
# # list of text documents
# text = ["The quick brown fox jumped over the lazy dog.",
# 		"The dog.",
# 		"The fox"]
# # create the transform
# vectorizer = TfidfVectorizer()
# # tokenize and build vocab
# vectorizer.fit(text)
# # summarize
# print(vectorizer.vocabulary_)
# print(vectorizer.idf_)
# # encode document
# vector = vectorizer.transform([text[1]])
# # summarize encoded vector
# print(vector.shape)
# print(vector.toarray())

""" Extracting n grams from text """
# import  nltk
#
# text = nltk.word_tokenize("The quick brown fox jumped on the dog")
# def find_bigrams(input_list):
#   bigram_list = []
#   for i in range(len(input_list)-1):
#       bigram_list.append((input_list[i], input_list[i+1]))
#
#   return bigram_list
# #get individual items from the bigram
# bigrams = find_bigrams(text)
# print(bigrams)
# print(bigrams[0].__getitem__(0))
# print(bigrams[0].__getitem__(1))
# #Now write a function to generate trigrams.
"""using the nltk ngrams function"""

# from nltk import ngrams
# sentence = 'The quick brown fox jumped over the dog.'
# n = 6
# sixgrams = ngrams(sentence.split(), n)
# ngrams = []
# for grams in sixgrams:
#   ngrams.append(grams)
# print(ngrams)