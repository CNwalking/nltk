import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk.corpus import wordnet as wn

set = ['beautiful', 'bad', 'dad', 'close', 'monkey', 'good']
word = 'super'
def get_most_similar(search_word, word_set):
    result = ""
    similarity = 0
    for word in word_set:
        search_words = wn.synsets(search_word)
        words = wn.synsets(word)
        similarity_now = max([0 if search_word.path_similarity(word) == None
         else search_word.path_similarity(word) for search_word in search_words
         for word in words])
        if similarity < similarity_now:
            result = word
    return result
print(get_most_similar(word, set))