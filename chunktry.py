import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
from nltk import collocations



sentence1 = ("John knows who came to the party.")
sentence2 = ("John is a guy I know who came to the party.")
sentence3 = ("I know a guy who came to the party.")


token1 = word_tokenize(sentence1)
token2 = word_tokenize(sentence2)
token3 = word_tokenize(sentence3)

pos1 = pos_tag(token1)

pos2 = pos_tag(token2)

pos3 = pos_tag(token3)

 
print('token1: ')
print(token1)
print('token2: ')
print(token2)
print('token3: ')
print(token2)

print('pos1: ')
print(pos1)
print("pos: 2")
print(pos2)
print("pos: 3")
print(pos3)

print(pos2[0])