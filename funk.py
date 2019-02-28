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

def indexOfSearchTerm(posList:list, searchTerm:str, collocates:str, nextWord:str):
    wordNum = 0
    for wordNum in range(len(posList)):
        #if the word matches the search term, the pos matches the collocates and nextWord is within 6 words of the word
        if (posList[wordNum][0] == searchTerm) and (posList[wordNum][1][0] == collocates[0]) and (countToNextWord(posList[wordNum:], nextWord) < 6):
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


def get_set_context_wh(tagged_sent:list , context:str, wh:str):
    get = False
    ret_list = []
    for tag in tagged_sent:
        if tag[0].lower() == context.lower():
            get = True
        if get:
            ret_list.append(tag)
        if tag[0].lower() == wh.lower() and get:
            break
    
    return ret_list if ret_list != [] else None

def get_set_wh_collocate(tagged_sent:list, wh:str, collocate:str):
    get = False
    ret_list = []
    for tag in tagged_sent:
        if tag[0].lower() == wh.lower():
            get = True
        if get:
            ret_list.append(tag)
        if tag[1][0].lower() == collocate[0].lower() and get:
            break
    return ret_list if ret_list != [] else None

def x_in_set(x, pos_set:list, is_pos=True):
    for pair in pos_set:
        word = pair[0].lower()
        pos = pair[1].lower()

        if type(x) == list:
            for item in x:
                if is_pos and pos[0] == item[0].lower():
                    return True
                elif not is_pos and word == item.lower():
                    return True
        else:
            if is_pos and pos[0]== x[0].lower():
                return True
            elif not is_pos and word == x.lower():
                return True
    return False

# from nltk import word_tokenize
# from nltk import pos_tag

# tagged = pos_tag(word_tokenize('You know, there are those who say, we heard shots coming from other directions, the so-called grassy knoll theory and all that.'))

# print(get_set_wh_collocate(tagged, 'who', 'VERB'))

# print(get_set_context_wh(tagged, 'know', 'who'))