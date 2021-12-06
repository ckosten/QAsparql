import json
import csv
import re
f = open('output/spider_gold.json')
#data= csv.reader(f, delimiter=',')
data = json.load(f)
data= data[:400]
def newTable(data):
    all_tables = []
    i= 0
    new_tables= {"id":"",
                 "question":"",
                 "sparql_query":""
                 }
    for row in data:
        i += 1
        new_tables["id"] = (str(i))
        new_tables["question"] = row[2]
        new_tables["sparql_query"] = row[4]
        all_tables.append(new_tables.copy())
    with open("data/SPIDER/linked_answer.json", 'w') as new_file:
        json.dump([all_tables], new_file, indent=4)  # indent formats it into a nice cute json
#newTable(data)



for i, query in enumerate(data):
    all_tables= []
    new_tables = {"correct": True,
                  "query": "",
                  "target_variable": ""}
    uris = re.findall(r'(?=\?).*?(?<=\.)', query['query'])
    for uri in uris:
        alias = re.findall(r'(?=\?t).*?(?=\s)', uri)
        if '{' in uri:
            uri = uri.split('{ ', 1)
            uri = uri[1]
        elif '=' in uri or '>' in uri or '<' in uri or '!=' in uri:
            continue
        new_tables["query"] = uri
        if len(alias) ==0:
            alias = '?t1'
        else:
            new_tables["target_variable"] = alias[0]
        all_tables.append(new_tables.copy())
    data[i]['generated_queries']= all_tables
with open("output/spider_gold_gen_queries_test.json", 'w') as new_file:
    json.dump([data], new_file, indent=4)