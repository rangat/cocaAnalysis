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
    #[('John', 'NNP'), ('know', 'VBP'), ('a', 'DT'), ('guy', 'NN'), ('who', 'WP'), ('came', 'VBD'), ('to', 'TO'), ('the', 'DT'), ('party', 'NN')]
    posList:list = pos_tag(token)
    print('Tagged sentence: ', posList)

    precedingList:list = f.listBeforePOS(posList, c.wh)
    print('Preceding: ', precedingList)

    #shortPosList is a list starting from the noun preceding the wh pronoun ending with the wh pronoun
    shortPosList = f.listBefore(precedingList, c.verb)
    print('Short List: ', shortPosList)

    return f.hasNoun(shortPosList)

def isRelClause(posList:list):
    precedingList:list = f.listBeforePOS(posList, c.wh)
    #print('Preceding: ', precedingList)

    #shortPosList is a list starting from the noun preceding the wh pronoun ending with the wh pronoun
    shortPosList = f.listBefore(precedingList, c.verb)
    #print('Short List: ', shortPosList)

    return f.hasNoun(shortPosList)

#print(isRelativeClause(" The moon is a star who lost her shine."))
#print(isRelativeClause(input('Enter a string: ')))
#print(isRelativeClause("John knows a guy who came to the party"))
#print(isRelativeClause("John is a guy I know who came to the party."))
#print(isRelativeClause(" 's harmful if we let it be harmful. You know, it was Aristotle who said: focus on what you can control, and you can get a lot"))
print(isRelativeClause('the things that makes the danger real is that they know a middle-aged local man who ran a small side business who was beheaded with a serrated knife to enhance his'))