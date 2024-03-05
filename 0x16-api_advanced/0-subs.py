#!/usr/bin/python3
"""
function that queries the Reddit API and
returns the number of subscribers
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """Returns number of subscibers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Lizzie"}
    resp = requests.get(url, headers)
    if resp.status_code == 200:
        subreddit_data = resp.json()
        no_of_subscribers = subreddit_data.get("data").get("subscribers")
        return no_of_subscribers
    else:
        return 0


if __name__ == "__main__":
    """Documentation to fulfill all requirements"""
    number_of_subscribers(sys.argv[1])
