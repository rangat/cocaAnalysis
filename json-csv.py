import json
import csv

fname = input("What's the file name? ")

data = None
headers = []

with open(fname, "r") as j:
    print("Loading Data")
    data = json.load(j)
    headers = list(data[0].keys())

real_name = fname.split("/")[-1][:-5]
print(real_name)

with open(real_name+".csv", "w") as c:
    writer = csv.DictWriter(c, fieldnames=headers)
    writer.writeheader()
    cnt=0
    for d in data:
        if cnt%100==0:
            print(cnt)
        cnt+=1
        writer.writerow(d)