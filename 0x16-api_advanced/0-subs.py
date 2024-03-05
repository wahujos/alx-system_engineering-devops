#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """Returns number of subscibers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "my_application123"}
    resp = requests.get(url, headers);
    if resp.status_code == 200:
        data = resp.json()
        no_of_subscribers = data["data"]["subscribers"]
        return no_of_subscribers
    else:
        return 0
