#!/usr/bin/python3
""" test """
import json
import requests
import sys


def recurse(subreddit, hot_list=[], after='first'):
    """ test """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': 'youremail@domain.com'
    }
    data = {
        'after': after
    }
    if after == 'first':
        x = requests.get(url, headers=headers, allow_redirects=False)
        if x.status_code == 200:
            for y in json.loads(x.text)['data']['children']:
                hot_list.append(y['data']['title'])
            if json.loads(x.text)['data']['after']:
                return recurse(subreddit, hot_list, json.loads(
                    x.text)['data']['after'])
            else:
                return hot_list
        else:
            return(None)
    else:
        x = requests.get(url, headers=headers,
                         allow_redirects=False, params=data)
        for y in json.loads(x.text)['data']['children']:
            hot_list.append(y['data']['title'])
        if json.loads(x.text)['data']['after']:
            return recurse(subreddit, hot_list, json.loads(
                x.text)['data']['after'])
        else:
            return hot_list
