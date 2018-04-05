def listBeforePOS(posList:list, POS:str):
    for x in posList:
        if x[1][0] == POS:
            return posList[:posList.index(x)+1]
    return posList

def listAfterPOS(posList:list, POS:str):
    for x in posList:
        if x[1][0] == POS:
            return posList[posList.index(x):]
    return posList

def hasNoun(posList:list):
    for x in posList:
        if x[1][0] == 'N':
            return True
    return False

def listBefore(shortList:list, POS:str):
    revList = shortList[:]
    revList.reverse()
    for x in revList:
        if x[1][0] == POS:
            return shortList[len(shortList)-1-revList.index(x):]
    return None

def lemList(token, wnl):
    for x in range(len(token)):
        token[x] = wnl.lemmatize(token[x])
    return token

def hasPOS(posList:list, POS:str):
    for x in posList:
        if x[1][0] == POS:
            return True
    return False

def returnPOSWord(posList:list, POS:str):
    for x in posList:
        if x[1][0] == POS:
            return x[1]
    return None

def remakeSent(posList:list):
    sent = ''
    for x in posList:
        sent = sent + x[0] + " "
    return sent

def hasMultplePOS(posList:list, POS:str):
    counter = 0
    for x in posList:
        if x[1][0] == POS:
            counter += 1
    
    if counter > 1:
        return True
    else: 
        return False

def countToNextWord(posList:list, word):
    wordNum = 0
    for wordNum in range(len(posList)):
        if posList[wordNum][0] == word:
            return wordNum
        wordNum += 1
    return wordNum

def indexOfSearchTerm(posList:list, searchTerm:str, nextWord:str):
    wordNum = 0
    for wordNum in range(len(posList)):
        if posList[wordNum][0] == searchTerm and (countToNextWord(posList[wordNum:], nextWord) < 6):
            return wordNum
        wordNum += 1
    return wordNum

def indexOfPOSAfterSearchTerm(posList:list, word:str, POS:str):
    wordNum = countToNextWord(posList, word)
    wordNum+=1
    while wordNum < len(posList):
        if posList[wordNum][1][0] == POS:
            return wordNum
        wordNum += 1
    return 0