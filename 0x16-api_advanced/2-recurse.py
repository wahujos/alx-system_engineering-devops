#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and
returns a list containing the titles of all
hot articles for a given subreddit
"""

import requests
import sys


def recurse(subreddit, after=None, hot_list=[]):
    """
    returns a list containing the titles of all
    hot articles
    """
    limit = 1
    after = None
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': limit, 'after': after}
    headers = {'User-Agent': 'my_application123'}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        after = data['data']['after']
        if after:
            return recurse(subreddit, after, hot_list)
        else:
            return hot_list
    else:
        return None


if __name__ == "__main__":
    recursive(sys.argv[1], None, [])
