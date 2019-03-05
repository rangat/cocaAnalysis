import json
import os

def run():
    collected = []
    for file in os.listdir('./edited'):
        filename = os.fsdecode(file)
        
        if not filename.endswith(".json"):
            continue
        
        with open('edited/{}'.format(filename)) as json_data:
            collected.extend(json.load(json_data))

    with open("edited/coca_data.json", 'w') as outfile:
        json.dump(collected, outfile)
        print("successfully made complete json")
