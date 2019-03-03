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
        modal = None
        verb = None

        modals = ['can', 'could', 'may', 'might', 'shall', 'should', 'will', 'would', 'must']
        
        # Know to wh (SET A)
        #context_wh:list = f.get_set_context_wh(tagged, context, whWord)
        
        # Wh to verb (SET B)
        #wh_collocate:list = f.get_set_wh_collocate(tagged, whWord, collocate)

        context_wh, wh_collocate = f.get_sets(tagged, context, whWord, collocate)

        obj['context_wh'] = str(context_wh)
        obj['wh_collocate'] = str(wh_collocate)

        try:
            if 'you know,' in sent:
                clauseType = "You Know"
            elif f.x_in_set(".", context_wh, is_pos=True) or f.x_in_set(".", wh_collocate, is_pos=True) or f.x_in_set("#", context_wh, is_pos=True) or f.x_in_set("#", wh_collocate, is_pos=True) or f.x_in_set('``', context_wh, is_pos=True) or f.x_in_set(",", context_wh, is_pos=True):
                clauseType = "Skipped"
            # Check if the clause is useless to us
            elif f.x_in_set("(", context_wh, is_pos=True) or f.x_in_set(")", context_wh, is_pos=True) or f.x_in_set("(", wh_collocate, is_pos=True) or f.x_in_set(")", wh_collocate, is_pos=True):
                clauseType = "Parens"
            elif f.x_in_set("V", context_wh, is_pos=True):
                clauseType = "Other"
            # IF NP exists in SET A - Relative Clause
            elif f.x_in_set("N", context_wh, is_pos=True):
                clauseType = "Relative Clause"
            # ELSE IF "to" exists in SET B - Non-Finite
            elif f.x_in_set("to", wh_collocate, is_pos=False):
                clauseType = "Non-Finite"
                verb = f.get_pos_word_in_set(wh_collocate, 'V')
            # ELSE IF "gap" exists in either set - :
            elif f.x_in_set(":", context_wh, is_pos=True) or f.x_in_set(":", wh_collocate, is_pos=True):
                clauseType = ":"
            # ELSE IF modal exists in SET B - Modal
            elif f.x_in_set(modals, wh_collocate, is_pos=False):
                clauseType = "Modal"
                modal = f.get_pos_word_in_set(wh_collocate, 'M')
                verb = f.get_pos_word_in_set(wh_collocate, 'V')
            # ELSE - Finite
            else:
                clauseType = "Finite"
                verb = f.get_pos_word_in_set(wh_collocate, 'V')
        except:
            print("BROKE HERE: ")
            print(obj["resNumber"])
            print(sent)
            print(tagged)
            print(context_wh)
            break
        
        obj['clauseType'] = clauseType
        obj['modal'] = modal
        obj['verb'] = verb
    
    return jsonList
