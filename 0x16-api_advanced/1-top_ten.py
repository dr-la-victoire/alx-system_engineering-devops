#!/usr/bin/python3
"""This module queries the Reddit API to get the 10 hot posts of a subreddit"""
import requests

def top_ten(subreddit):
    """Prints the number of subscribbers a subreddit has"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    listings = {'limit': 10}
    response = requests.get(url, headers=headers, params=listings)
    data = response.json()
    try:
        results = data.get('data').get('children')

        for post in results:
            print(post.get('data').get('title'))
    except Exception:
        print('None')
