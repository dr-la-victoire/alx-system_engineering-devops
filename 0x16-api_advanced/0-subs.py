#!/usr/bin/python3
"""This module works with the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """This function gets the total number of subscribers to a subreddit"""
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 
            'Mozilla/5.0 (X11; Linux i686; rv:124.0) Firefox/124.0'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data['data']['subscribers']
