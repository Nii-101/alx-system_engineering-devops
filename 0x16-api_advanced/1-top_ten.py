#!/usr/bin/python3
'''
This function queries the Reddit API and prints the
titles of the first 10 hot posts
'''

import requests


def top_ten(subreddit):
    '''Returns top ten posts titles'''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Alx-User'}
    params = {'limit': 10}
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        objects = data['data']['children']
        for obj in objects:
            print(obj['data']['title'])
    else:
        print('None')
