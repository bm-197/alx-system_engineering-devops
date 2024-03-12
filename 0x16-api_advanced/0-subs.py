import requests
from sys import argv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}


def number_of_subscribers(subreddit):
    """"Get Subreddit subs number"""
    req = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json", headers=headers, allow_redirects=False)
    if (req.json().get("kind") == 't5'):
        data = req.json().get("data").get("subscribers")
        return data
    else:
        return 0