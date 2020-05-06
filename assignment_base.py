import nltk
import re
nltk.data.path.append("/Users/walking/Project/pythonProject/nltk_data")
from nltk.corpus import wordnet
from nltk.chunk import conlltags2tree, tree2conlltags
file_url = "./ABCNewsArticle/Are we using ventilators too much?.txt"

# open a file
try:
    f = open(file_url, "r")
    story = f.read()
    # two steps to format the article
    temp = story.replace('\\n', '')
    cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]")
    temp = cop.sub(' ', temp)
    # end format
    pos_tags = nltk.pos_tag(nltk.word_tokenize(temp))
    # An optional qualifier (DT),followed by several adjectives(JJ),
    # and then followed by a noun (NN), should form a noun phrase(NP)
    pattern = 'NP:{<DT>？<JJ> * <NN>}'
    cp = nltk.RegexpParser(pattern)
    # get the blocks
    cs = cp.parse(pos_tags)
    # change to IOB tags(the standard way to represent the structure of blocks in a file)
    iob_tag = tree2conlltags(cs)
    print(iob_tag)

    # ne_tree = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(temp)))
    # print(ne_tree)




finally:
    if f:
        f.close()