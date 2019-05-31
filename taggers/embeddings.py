import nltk
from nltk import sent_tokenize
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

        obj["clean_sentence"] = None
        
        tok_sents = sent_tokenize(sent)
        for s in tok_sents:
            if whWord.lower() in s.lower() and context.lower() in s.lower():
                sent = s
                obj["clean_sentence"] = s
                break

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

        context_wh, wh_collocate, wh_end = f.get_sets(tagged, context, whWord, collocate)

        verbs_after_wh = []
        for w in wh_end:
            if w[1].startswith("V"):
                verbs_after_wh.append(w[0])

        obj['context_wh'] = context_wh
        obj['wh_collocate'] = wh_collocate
        obj['wh_end'] = wh_end
        
        obj['verbs_after_wh'] = verbs_after_wh

        obj['wh'] = [whWord]

        try:
            if 'JJ' in wh_collocate[1][1]:
                obj['wh'].append(wh_collocate[1][0])
        except:
            pass
        
        obj['phrase'] = context
        obj['mat_verb'] = f.modded_lemma(context)

        if len(wh_collocate) > 1:
            word_after_wh = wh_collocate[1][0]
            pos_after_wh = wh_collocate[1][1]
        else:
            word_after_wh = None
            pos_after_wh = None
        
        obj['word_after_wh'] = word_after_wh

        if pos_after_wh:
            obj['sub_after_wh'] = True if "N" in pos_after_wh or "DT" in pos_after_wh or "JJ" in pos_after_wh or "P" in pos_after_wh else False 
        else:
            obj['sub_after_wh'] = False

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
            elif f.x_in_set("N", context_wh, is_pos=True) or f.x_in_set("DT", context_wh, is_pos=True) or f.x_in_set("JJ", context_wh, is_pos=True) or f.x_in_set("P", context_wh, is_pos=True) or f.x_in_set('CD', context_wh, is_pos=True):
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

        obj['emb_verb'] = f.modded_lemma(verb)
        obj['verb'] = verb
    return jsonList
