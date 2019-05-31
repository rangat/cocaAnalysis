import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk import pos_tag
from nltk import RegexpParser
from nltk import collocations
from nltk.stem import WordNetLemmatizer
import pprint as pprint

import funk as f

def tagList(jsonList:list, whWord:str, collocate:str, context:str):
    for obj in jsonList:
        if not obj["sentence"] or obj["sentence"] == "": # Skip conditions
            continue

        sent = obj["sentence"]
        #iterate through list reversed, find the verb first and then the wh

        obj["clean_sentence"] = None

        tok_sents = sent_tokenize(sent)
        for s in tok_sents:
            if whWord.lower() in s.lower() and context.lower() in s.lower():
                sent = s
                obj["clean_sentence"] = s
                break
        
        tagged = pos_tag(word_tokenize(sent))

        clauseType = None
        modal = None
        verb = None
        
        modals = ['can', 'could', 'may', 'might', 'shall', 'should', 'will', 'would', 'must']

        obj['wh'] = whWord
        obj['phrase'] = context

        start_wh = f.start_to_wh(tagged, whWord)

        if f.x_in_set("N", start_wh, is_pos=True) or f.x_in_set("DT", start_wh, is_pos=True) or f.x_in_set("JJ", start_wh, is_pos=True) or f.x_in_set("P", start_wh, is_pos=True) or f.x_in_set("CD", start_wh, is_pos=True):
                clauseType = "Relative Clause"
        
        obj['clauseType'] = clauseType
    return jsonList