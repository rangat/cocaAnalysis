import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
from nltk import collocations
from nltk.stem import WordNetLemmatizer
import funk as f

def isRelativeClause(sent:str):
    wnl = WordNetLemmatizer()

    #tokenize the string
    token = word_tokenize(sent)

    #lemmatize the string (get rid of all the word endngs)
    token = f.lemList(token, wnl)

    #tag the list with their parts of speach (returns a list of tuples)
    posList:list = pos_tag(token)
    print('Tagged sentence: ', posList)

    #shortPosList is a list starting from the noun before the wh pronoun ending with the wh pronoun
    shortPosList = posList[f.retVerbBeforeW(posList, f.retWproNounIndex(posList)+1):(f.retWproNounIndex(posList)+1)]
    print('Short List: ', shortPosList)

    return f.hasNoun(shortPosList)

print(isRelativeClause(input('Enter a string: ')))