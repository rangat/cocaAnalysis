import json
import tagJSON as tj
import pprint
import os
#import shorten as s

#https://jsonlint.com/
#breaks when passed in a sent with multiple wh words

for file in os.listdir('./unread'):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        name = filename[:-5]
        parts = name.split("_")
        
        whWord = parts[0].lower()
        collocates = parts[1].lower()
        prevWord = parts[2].lower()
        print("loaded file: ", filename)
        with open('unread/'+filename) as json_data:
            jList = json.load(json_data)
            
        #processedJSON = s.addConcatTag(jList, whWord, prevWord)
        #start running preprocessing on loaded data, pass in filename
        newJSON = tj.tagList(jList, whWord, collocates, prevWord)

        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(newJSON)

        if not os.path.exists('edited'):
            os.makedirs('edited')
            print("created edited directory")

        with open("edited/edited_"+filename, 'w') as outfile:
            json.dump(newJSON, outfile)
            print("successfully edited ", filename)