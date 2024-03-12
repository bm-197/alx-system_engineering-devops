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
    user = {"User-Agent": "Mozilla/10.0/API"}
    url = requests.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), headers=user).json()

    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0
if __name__ == "__main__":
     print("{:d}".format(number_of_subscribers(sys.argv[1])))
