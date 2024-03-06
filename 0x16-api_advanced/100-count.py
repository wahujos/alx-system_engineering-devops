#!/usr/bin/python3
"""
recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import requests
import sys


def count_words(subreddit, word_list, after=None, counts=None):
    """prints a sorted count of given keys"""
    if counts is None:
        counts = {}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 25, 'after': after} if after else {'limit': 100}
    headers = {'User-Agent': 'my_application123'}
    response = requests.get(url=url, params=params, headers=headers)
    if response.status_code != 200:
        return
    data = response.json()
    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            word = word.lower()
            counts[word] = counts.get(word, 0)
    after = data['data']['after']
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: x[1],
                               reverse=True)
        for word, count in sorted_counts:
            print(f"{word}: {count}")


if __name__ == "__main__":
    """returns a count of the key words"""
    word_list = sys.argv[2].split()
    count_words(sys.argv[1], word_list)
