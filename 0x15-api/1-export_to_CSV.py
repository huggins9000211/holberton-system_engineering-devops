#!/usr/bin/python3
""" test """
if __name__ == "__main__":
    import requests
    import sys
    import json
    x = requests.get('https://jsonplaceholder.typicode.com/todos')
    nameReq = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    empName = json.loads(nameReq.text)['username']
    f = open('{}.csv'.format(sys.argv[1]), 'a')
    for y in json.loads(x.text): 
        if str(y['userId']) == sys.argv[1]:
            f.write('"{}","{}","{}","{}"\n'.format(sys.argv[1], empName, y['completed'], y['title']))
    f.close()
