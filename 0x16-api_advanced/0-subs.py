#!/usr/bin/python3
"""This module queries the Reddit API to get the number of subs a subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribbers a subreddit has"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Chrome/58.0.3029.110 Safari/537.3'}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subs = data['data']['subscribers']
        return subs
    except Exception:
        return 0
