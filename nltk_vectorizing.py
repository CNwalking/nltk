import nltk
import os
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk import bigrams
from nltk import collections

txt_total = []
try:
    fileList = os.listdir("./terrorism data")
    for file in fileList:
        file_position = "./terrorism data/" + file
        with open(file_position, "r") as f:
            data = f.read()
            txt_total += [data]
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(str(txt_total))
    tokens = nltk.word_tokenize(str(text))
    tokens = [token.lower() for token in tokens if len(token) > 1]
    bi_tokens = bigrams(tokens)
    print(collections.Counter(bi_tokens).most_common()[0])
    text_tokens = nltk.text.Text(bi_tokens)
    print(text_tokens.collocations())
    print(text_tokens.concordance('''"'of", "'the"'''))
finally:
    f.close()