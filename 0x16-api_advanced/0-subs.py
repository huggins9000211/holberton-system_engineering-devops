#!/usr/bin/python3
""" test """
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ test """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'
    }
    x = requests.get(url, headers=headers, allow_redirects=False)
    if x.status_code == 200:
        return(json.loads(x.text)['data']['subscribers'])
    else:
        return(0)
