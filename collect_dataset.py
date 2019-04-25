import json
import os

def run():
    collected = []
    for file in os.listdir('./edited'):
        filename = os.fsdecode(file)
        
        if not filename.endswith(".json"):
            continue
        
        with open('edited/{}'.format(filename)) as json_data:
            data = json.load(json_data)
            collected.extend(data)
        
        print(len(collected))
        print(type(collected[0]))

    with open("edited/coca_data.json", 'w') as outfile:
        json.dump(collected, outfile, indent=4)
        print("successfully made complete json")
