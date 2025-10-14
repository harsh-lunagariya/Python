import json
lst = []

with open('dev.json','r') as f:
    dev = json.load(f)

merge = dev.copy()

with open('prod.json','r') as f:
    prod = json.load(f)
    lst.append(prod)

with open('staging.json','r') as f:
    staging = json.load(f)
    lst.append(staging)

for i in lst:
    for j in i.keys():
        if j=='cache':
            merge[j] = list(set(i[j]).union(set(merge[j])))
            continue
        for k in i[j].keys():
            if j=='database' and k=='port':
                merge[j][k] = int(i[j][k])
                continue
            merge[j][k] = i[j][k]

with open('merge.json','w') as f:
    json.dump(merge,f,indent=4)