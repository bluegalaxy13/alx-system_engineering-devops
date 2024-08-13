#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                   Default is an empty list.
        after (str, optional): Token used for pagination.
                               Default is an empty string.
        count (int, optional): Current count of retrieved posts. Default is 0.

    Returns:
        list: A list of post titles from the hot section of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for post in results.get("children", []):
        hot_list.append(post.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, after, count)
    
    return hot_list if hot_list else None
