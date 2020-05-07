#!/usr/bin/python3
""" test """
import json
import requests
import sys


def top_ten(subreddit):
    """ test """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'
    }
    x = requests.get(url, headers=headers, allow_redirects=False)
    
    if x.status_code == 200:
        for y in range(0, 10):
            print(json.loads(x.text)['data']['children'][y]['data']['title'])
    else:
        print('None')
