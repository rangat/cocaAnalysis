import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
from nltk import collocations
from nltk.stem import WordNetLemmatizer



sentence1 = ("John knows who came to the party.")
sentence2 = (" John is a guy I know who came to the party.")
sentence3 = (" I know a guy who came to the party.")

token1 = word_tokenize(sentence1)
token2 = word_tokenize(sentence2)
token3 = word_tokenize(sentence3)


wnl = WordNetLemmatizer()

for x in range(len(token1)):
    token1[x] = wnl.lemmatize(token1[x])

print(token1)
#print(wnl.lemmatize("knows"))

print(wnl.lemmatize(token1[1]))

pos1 = pos_tag(token1)
pos2 = pos_tag(token2)
pos3 = pos_tag(token3)

print(pos1) 

print(([item for item in pos1 if 'WP' in item]))
print(type([item for item in pos1 if 'WP' in item]))

print(pos1.index((['who', 'WP'])))
#print(pos1(pos1.index(('who', 'WP'))-1))
