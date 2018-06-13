import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
import funk as f
import posConstant as pc

#find the know, find the following wh, find the following verb: concat front and end
def addConcatTag(jsonFile:list, whWord:str, collocates:str, prevWord:str):
    wnl = WordNetLemmatizer()

    for jsonInd in jsonFile:
        sent = jsonInd["sentence"]

        #tokenize the string
        token = word_tokenize(sent)

        #lemmatize the string (get rid of all the word endngs)
        token = f.lemList(token, wnl)

        #tag the list with their parts of speach (returns a list of tuples)
        posList:list = pos_tag(token)

        firstInd = f.indexOfSearchTerm(posList, prevWord, collocates, whWord)
        afterPrevWordList = posList[firstInd:]

        secondInd = f.indexOfPOSAfterSearchTerm(afterPrevWordList, whWord, pc.verb)

        concatList = afterPrevWordList[:secondInd+1]

        concatSent = f.remakeSent(concatList)
        
        jsonInd["shortSent"] = concatSent
        
    return jsonFile

def retConcatList(posList:list, whWord:str, collocates:str, prevWord:str):
    firstInd = f.indexOfSearchTerm(posList, prevWord, collocates, whWord)
    afterPrevWordList = posList[firstInd:]

    secondInd = f.indexOfPOSAfterSearchTerm(afterPrevWordList, whWord, pc.verb)

    concatList = afterPrevWordList[:secondInd+1]
    
    return concatList