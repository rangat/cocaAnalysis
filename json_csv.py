import json
import csv
import os

def run():
    for file in os.listdir('./edited'):
        fname = os.fsdecode(file)
        
        if not fname.endswith('.json'): continue
        
        print("Converting {} to CSV".format(fname))

        data = None
        headers = []

        with open('./edited/{}'.format(fname), "r") as j:
            print("\nLoading Data")
            data = json.load(j)
            headers = list(data[0].keys())

        real_name = fname.split("/")[-1][:-5]
        print(real_name)

        if not os.path.exists('./csv'):
            os.makedirs('./csv')
            print("created edited directory")

        with open("./csv/{}.csv".format(real_name), "w") as c:
            writer = csv.DictWriter(c, fieldnames=headers)
            writer.writeheader()
            cnt=0
            for d in data:
                # if cnt%100==0:
                #     print(cnt)
                cnt+=1
                writer.writerow(d)
            print("Wrote {}.csv".format(real_name))