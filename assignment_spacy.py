import nltk
import re
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
import spacy
from spacy import displacy
from IPython.display import display, HTML
import matplotlib.pyplot as plt
file_url = "./ABCNewsArticle/Are we using ventilators too much?.txt"

# nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('en')
# open a file
try:
    f = open(file_url, "r")
    story = f.read()
    # two steps to format the article
    temp = story.replace('\\n', '')
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
    temp = cop.sub(' ', temp)
    # end format
    print(temp)
    displacy.render(nlp(temp), style='ent', jupyter=True)
finally:
    if f:
        f.close()