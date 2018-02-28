import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
from nltk import collocations
from nltk.stem import WordNetLemmatizer
import posConstant as c
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

    precedingList:list = f.listBeforePOS(posList, c.wh)
    print('Preceding: ', precedingList)


    print(f.indexBefore(c.verb, precedingList))
    #shortPosList is a list starting from the noun preceding the wh pronoun ending with the wh pronoun
    #shortPosList = posList[f.retVerbBeforeW(posList, f.retWproNounIndex(posList)+1):(f.retWproNounIndex(posList)+1)]
    #print('Short List: ', shortPosList)

    #return f.hasNoun(shortPosList)

#print(isRelativeClause(input('Enter a string: ')))
print(isRelativeClause("John knows who came to the party"))
#print(isRelativeClause("John is a guy I know who came to the party."))