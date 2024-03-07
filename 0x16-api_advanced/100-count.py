#!/usr/bin/python3
'''
This recursive function queries the Reddit API, parses
the title of all hot articles, and prints a sorted
count of given keywords
'''

import requests


def count_words(subreddit, word_list, after_token=None, count_dict=None):
    '''Prints a sorted list along with a count'''

    if count_dict is None:
        count_dict = {}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Alx-User'}

    if after_token:
        params = {'limit': 100, 'after': after_token}
    else:
        params = {'limit': 100}

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        objects = data['data']['children']

        for obj in objects:
            title = obj['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    if word.lower() in count_dict:
                        count_dict[word.lower()] += 1
                    else:
                        count_dict[word.lower()] = 1

        after_token = data['data']['after']
        if after_token:
            return count_words(subreddit, word_list, after_token, count_dict)
        else:
            sorted_counts = sorted(count_dict.items(),
                                   key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f'{word}: {count}')
