#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import json
    import requests
    import sys

    totalCount = 0
    completedCount = 0
    x = requests.get('https://jsonplaceholder.typicode.com/todos')
    nameReq = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    empName = json.loads(nameReq.text)['name']
    compledTasks = []
    myList = []
    for y in json.loads(x.text):
        if str(y['userId']) == sys.argv[1]:
            myList.append(y)
            if y['completed']:
                completedCount += 1
                compledTasks.append(y['title'])
            totalCount += 1
    print("Employee {} is done with tasks({}/{}):".format(
        empName, completedCount, totalCount))
    for y in compledTasks:
        print("\t {}".format(y))
