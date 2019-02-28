import json
import os
import funk as f
import posConstant as c 

import nltk
from nltk import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()

#find the know, find the following wh, find the following verb: concat front and end

for file in os.listdir('./unprocessed'):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        print("loaded file: ", filename)
        with open('unprocessed/'+filename) as json_data:
            jList = json.load(json_data)
        
        #print(type(jList))

        newJSON = []

        #print(type(newJSON))
        
        i=0
        while i < len(jList)-1:
            sent = jList[i]["sentence"]
        
            #tokenize the string
            token = word_tokenize(sent)
            #lemmatize the string   (get rid of all the word endngs)
            token = f.lemList(token, wnl)
            #tag the list with their parts of speach (returns a list of tuples)
            posList:list = pos_tag(token)
            
            if f.hasMultplePOS(posList, c.wh):
                #move json objects to new file
                newJSON.append(jList.pop(i))
                jList.pop(i)
            i += 1
        
        if not os.path.exists('processed'):
            os.makedirs('processed')
            print("created processed directory")

        with open("processed/processed_exclude_"+filename, 'a') as outfile:
            json.dump(newJSON, outfile)
            #print("successfully processed ", filename)
        with open("processed/processed_"+filename, 'a') as outfile:
            json.dump(jList, outfile)