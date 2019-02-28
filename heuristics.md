# Heuristics for Analysis
### Example Sentence:

* "Well, just before all of this happened, we know that K.T. McFarland, who was Flynn's deputy, she's a former Fox News contributor, she had"

* "Nobody within the show is surprised either, because we've reached the point at which everybody on the show knows and sees exactly who Frank Underwood is."

    ``` python 
    [('Nobody', 'NN'), ('within', 'IN'), ('the', 'DT'), ('show', 'NN'), ('is', 'VBZ'), ('surprised', 'VBN'), ('either', 'RB'), (',', ','), ('because', 'IN'), ('we', 'PRP'), ("'ve", 'VBP'), ('reached', 'VBN'), ('the', 'DT'), ('point', 'NN'), ('at', 'IN'), ('which', 'WDT'), ('everybody', 'NN'), ('on', 'IN'), ('the', 'DT'), ('show', 'NN'), ('knows', 'VBZ'), ('and', 'CC'), ('sees', 'VBZ'), ('exactly', 'RB'), ('who', 'WP'), ('Frank', 'NNP'), ('Underwood', 'NNP'), ('is', 'VBZ'), ('.', '.')]
    ```
    ``` python
    ('knows', 'VBZ'), ('and', 'CC'), ('sees', 'VBZ'), ('exactly', 'RB'), ('who', 'WP')
    ```
* knows to see exactly who

### **Types of the word know:** *know, knows, knew*
``` python
know = ['know', 'knows', 'knew']
```

#### Two sets we must look at

1. **Set A:** *'know-wh'* between know & who
2. **Set B:** *'wh-v'* between who & following verb

``` python
clauseType = None
modals = ['can', 'could', 'may', 'might', 'shall', 'should', 'will', 'would', 'must']

if V exists between know-wh:
    clauseType = "Other"
elif NP exists between know-wh:
    clauseType = "Relative Clause"
elif 'to' exists between who-v:
    clauseType = "Non-Finite"
elif modal exists between who-v:
    clauseType = "Modal"
else:
    clauseType = "Finite"
```

#### TODO

1. **If the open and closing parens exist in "know-who" then don't tag as "parens"**
2. **Start looking at know-where**

## Other Collocations to Scrape

* know - who
* know - where
* predict - who
* predict - where
* surprise - who
* surprise - where
* tell - who
* tell - where
