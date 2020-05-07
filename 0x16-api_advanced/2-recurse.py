#!/usr/bin/python3
""" test """
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ test """
    url = 'https://www.reddit.com/r/{}/about.json'.format(sys.argv[1])
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'
    }
    x = requests.get(url, headers=headers, allow_redirects=False)
    print(x.text)
    if x.status_code == 200:
        return(json.loads(x.text)['data']['subscribers'])
    else:
        return(0)

number_of_subscribers('funny')