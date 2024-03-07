#!/usr/bin/python3
'''
module for function to query the Reddit API
'''

import requests
from sys import argv

def number_of_subscribers(subreddit):
    '''
    returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    '''
    user = {"User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/bm-197)"}
    url = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=user).json()

    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0
if __name__ == "__main__":
     print("{:d}".format(number_of_subscribers(sys.argv[1])))
