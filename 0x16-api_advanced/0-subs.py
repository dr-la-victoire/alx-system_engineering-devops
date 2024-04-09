#!/usr/bin/python3
"""This module queries the Reddit API to get the number of subs a subreddit"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribbers a subreddit has"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Chrome/98.0.4758.102'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json().get('data')
        results = data.get('subscribers')
        return results
    except Exception:
        return 0
