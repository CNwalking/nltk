import nltk
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")

# open a file
try:
    f = open("./test.txt", "r")

    tokens = nltk.word_tokenize(f.read())
    postags = nltk.pos_tag(tokens)
    print(postags)
finally:
    if f:
        f.close()