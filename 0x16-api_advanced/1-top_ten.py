#!/usr/bin/python3
"""
function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit
"""

import requests
import sys


def top_ten(subreddit):
    """the first 10 hot posts listed"""
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'my_application123'}
    response = requests.get(f'{url}?limit=10', headers=headers).json()
    try:
        for res in response.get('data').get('children'):
            print(res.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    """documentation styling"""
    top_ten(sys.argv[1])
