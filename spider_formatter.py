import json
import csv

f = open('data/SPIDER/TrainPairs.csv')
data= csv.reader(f, delimiter=',')

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
newTable(data)
