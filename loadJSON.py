import json
from taggers import embeddings as te
import pprint
import os

def run():
    for file in os.listdir('./unread'):
        filename = os.fsdecode(file)
        if filename.endswith(".json"):
            name = filename[:-5]
            parts = name.split("_")
            
            whWord = parts[0].lower()
            collocate = parts[1].lower()
            context = parts[2].lower()
            print("loaded file: ", filename)
            with open('unread/'+filename) as json_data:
                jsonList:list = json.load(json_data)

            newJSON:list = te.tagList(jsonList, whWord, collocate, context)

            # Check if dir exists and create it if not
            if not os.path.exists('edited'):
                os.makedirs('edited')
                print("created edited directory")

            # Dump newly formed json into file
            with open("edited/edited_"+filename, 'w') as outfile:
                json.dump(newJSON, outfile, indent=4)
                print("successfully edited ", filename)