import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
from nltk import collocations
from nltk.stem import WordNetLemmatizer
import pprint as pprint

import funk as f

# My functions:

# who - verb - know
def tagList(jsonList:list, whWord:str, collocate:str, context:str):
    for obj in jsonList:
        if not obj["sentence"] or obj["sentence"] == "": # Skip conditions
            continue
        
        # Save the sentance to a var
        sent = obj["sentence"]

        # Tokenize sentence and tag parts of speech
        tagged = pos_tag(word_tokenize(sent))

        clauseType = None

        modals = ['can', 'could', 'may', 'might', 'shall', 'should', 'will', 'would', 'must']
        
        # Know to wh (SET A)
        context_wh:list = f.get_set_context_wh(tagged, context, whWord)
        
        # Wh to verb (SET B)
        wh_collocate:list = f.get_set_wh_collocate(tagged, whWord, collocate)

        # IF NP exists in SET A - Relative Clause
        if f.x_in_set("N", context_wh, is_pos=True):
            clauseType = "Relative Clause"
        # ELSE IF "to" exists in SET B - Non-Finite
        elif f.x_in_set("to", wh_collocate, is_pos=False):
            clauseType = "Non-Finite"
        # ELSE IF modal exists in SET B - Modal
        elif f.x_in_set(modals, wh_collocate, is_pos=False):
            clauseType = "Modal"
        # ELSE - Finite
        else:
            clauseType = "Finite"

        obj['clauseType'] = clauseType
    
    return jsonList



        