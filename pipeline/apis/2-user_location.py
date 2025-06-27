#!/usr/bin/env python3
"""
Retrieve and display the location of a GitHub user
"""

import sys
import requests
import time


def get_user_location(url):
    """
    Fetches and returns the location of a GitHub user from the provided API URL
    
    Args:
        url (str): Full GitHub API URL for a user
        
    Returns:
        str: Location string if successful, None for errors
    """
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json().get('location', '')
        elif response.status_code == 403:
            reset_time = int(response.headers.get('X-Ratelimit-Reset', 0))
            current_time = int(time.time())
            minutes = (reset_time - current_time + 59) // 60
            return "Reset in {} min".format(minutes)
        elif response.status_code == 404:
            return "Not found"
        else:
            msg = "Error: Unexpected status code {}".format(response.status_code)
            print(msg)
            return None

    except requests.exceptions.RequestException as e:
        print("Request error: {}".format(e))
        return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <GitHub_API_URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    result = get_user_location(url)

    if result is not None:
        print(result)
