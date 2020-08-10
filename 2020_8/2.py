import csv
import json
with open('D:\nkbh\fa.csv', newline='') as file:
    csv_reader = csv.reader(file)

ll = []
for index, row in enumerate(csv_reader):
    l = []

    city = row[0]

    huanbi = row[1]
    tongbi = row[2]
    dingji = row[3]
    l.append(city)
    l.append(huanbi)
    l.append(tongbi)
    l.append(dingbi)
    ll.append(l)


with open("fb.json","w",encoding="utf-8") as f:
    f.write(json.dumps(ll))