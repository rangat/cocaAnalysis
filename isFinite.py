import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
from nltk import collocations
from nltk.stem import WordNetLemmatizer
import posConstant as c
import funk as f

def isInfinite(sent:str):
    wnl = WordNetLemmatizer()

    #tokenize the string
    token = word_tokenize(sent)
   
    #lemmatize the string (get rid of all the word endngs)
    token = f.lemList(token, wnl)

    #tag the list with their parts of speach (returns a list of tuples)
    posList:list = pos_tag(token)
    #print('Tagged sentence: ', posList)

    #shortPosList is a list starting from the wh pronoun to the verb after it
    shortPosList = f.listAfterPOS(posList, c.wh)
    segment = f.listBeforePOS(shortPosList, c.verb)
    
    #print('Segment: ', segment)

    return f.hasPOS(segment, c.det)


#return true if there is a determiner between the wh pronoun and the following verb
def isInFin(posList:list):
    #shortPosList is a list starting from the wh pronoun to the verb after it
    shortPosList = f.listAfterPOS(posList, c.wh)
    segment = f.listBeforePOS(shortPosList, c.verb)
    #print('Segment: ', segment)
    return f.hasPOS(segment, c.det)

def retModal(posList:list):
    shortPosList = f.listAfterPOS(posList, c.wh)
    segment = f.listBeforePOS(shortPosList, c.verb)
    if isInFin(posList):
        return f.returnPOSWord(segment, c.modal)
    return 'None'

#print("Is the verb infinite?")
#print(isInfinite("John knows where to found coffee"))

#Modals: [can, might, must, should, could, would, ~will] 