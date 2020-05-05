#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import json
    import requests
    import sys

    totalCount = 0
    completedCount = 0
    x = requests.get('https://jsonplaceholder.typicode.com/todos')
    compledTasks = []
    myDict = {int(sys.argv[1]): []}
    myList = []
    for y in json.loads(x.text):
        if str(y['userId']) == sys.argv[1]:
            nameReq = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}'.format(
                    y['userId']))
            empName = json.loads(nameReq.text)['username']
            myDict[y['userId']].append(
                {"task": y['title'], "completed": y[
                    'completed'], 'username': empName})
    f = open('{}.json'.format(sys.argv[1]), 'w+')
    f.write(json.dumps(myDict))
    f.close
