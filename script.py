import csv
import json
from pprint import pprint

commands = {'commands': []}
for i in range (1,4):
    user = 'user'+str(i)
    with open(user) as f:
        reader = csv.reader(f)
        for row in reader:
            flag = None
            for command in commands ['commands']:
                if command['module']==row[0] and command['name']==row[1] and command['function']==row[2]:
                    flag = command
            if flag is None:
                commands['commands'].append({ 'param': [{'user':user}], 'module':row[0], 'name':row[1], 'function' : row[2]})
            else:
                flag['param'].append({'user':user})
f = open('final','w+')
f.write(json.dumps(commands))
