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