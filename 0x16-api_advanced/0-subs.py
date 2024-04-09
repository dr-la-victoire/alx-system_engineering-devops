#!/usr/bin/python3
"""This module queries the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a sub reddit"""
    url = 'http://reddit.com/r/{}/about.json'.format(subreddit)

    response = requests.get(url)
    if response == 200:
        results = response.json()
        return results.get('data').get('subscribers')
    else:
        return 0
