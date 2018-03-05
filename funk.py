def retWproNounIndex(posList:list):
    ind = -1
    for x in posList:
        if x[1][0] == 'W':
            ind = posList.index(x)
    return ind

def retNounBeforeW(posList:list, num:int):
    shortPos = posList[:num]
    ind = -1
    for x in reversed(shortPos):
        if x[1][0] == 'N':
            return shortPos.index(x)
    return ind

def retVerbBeforeW(posList:list, num:int):
    shortPos = posList[:num]
    revList = shortPos
    revList.reverse()
    ind = -1
    for x in revList:
        if x[1][0] == 'V':
            return (len(shortPos)-revList.index(x)-1)
    return ind

def hasNoun(posList:list):
    for x in posList:
        if x[1][0] == 'N':
            return True
    return False

def lemList(token, wnl):
    for x in range(len(token)):
        token[x] = wnl.lemmatize(token[x])
    return token

def hasTo(posList:list):
    for x in posList:
        if x[1][0] == 'T':
            return True
    return False