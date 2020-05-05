#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import requests
    import sys
    import json
    x = requests.get('https://jsonplaceholder.typicode.com/todos')
    myDict = {}
    nameReq = requests.get('https://jsonplaceholder.typicode.com/users/')
    for emp in json.loads(nameReq.text):
        empName = emp['username']
        myDict[emp['id']] = []
        for y in json.loads(x.text):
            if y['userId'] == emp['id']:
                myDict[emp['id']].append({"task": y['title'], "completed": y['completed'], 'username': empName})
    f = open('todo_all_employees.json', 'w+')
    f.write(json.dumps(myDict))
    f.close
