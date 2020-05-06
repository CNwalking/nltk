corpus = ['king is a strong man',
          'queen is a wise woman',
          'boy is a young man',
          'girl is a young woman',
          'prince is a young king',
          'princess is a young queen',
          'man is strong',
          'woman is pretty',
          'prince is a boy will be king',
          'princess is a girl will be queen']

import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk import ne_chunk, pos_tag, word_tokenize
# Define a method to remove stop words

def remove_stop_words(corpus):
    stop_words = ['is', 'a', 'will', 'be']
    results = []
    for text in corpus:
        tmp = text.split(' ')
        for stop_word in stop_words:
            if stop_word in tmp:
                tmp.remove(stop_word)
        word_need=[]
        tokens = ne_chunk(pos_tag(word_tokenize(text)))
        for i in tokens:
            if i[1]=='NN' or i[1] == 'VB':
                word_need.append(i[0])
        for word_exist in tmp:
            if word_exist not in word_need:
                tmp.remove(word_exist)
        results.append(" ".join(tmp))
    print(results)

corpus = remove_stop_words(corpus)

