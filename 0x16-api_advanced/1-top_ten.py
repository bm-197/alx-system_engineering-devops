#!/usr/bin/python3
""" Queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit. """

def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    user = {"User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/bm-197)"}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
