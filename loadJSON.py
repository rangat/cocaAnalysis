import json
import tagJSON as tj
import pprint
import os

for file in os.listdir('./unread'):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        print("loaded file: ", filename)
        with open('unread/'+filename) as json_data:
            jList = json.load(json_data)
        
        newJSON = tj.tagList(jList)

        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(newJSON)

        if not os.path.exists('edited'):
            os.makedirs('edited')
            print("created edited directory")

        with open("edited/edited_"+filename, 'a') as outfile:
            json.dump(newJSON, outfile)
            print("successfully edited ", filename)