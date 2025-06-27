#!/usr/bin/env python3
"""
Retrieve and display information about the next SpaceX launch
"""

import requests
import sys


def fetch_data(url):
    """
    Fetches data from a URL with error handling

    Args:
        url (str): URL to fetch

    Returns:
        dict/list: JSON response data or None on error
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data: {}".format(e))
        return None


def get_next_launch():
    """
    Retrieves and processes SpaceX launch data to find the next launch
    
    Returns:
        tuple: (name, date_local, rocket_name, launchpad_name, locality)
    """
    # Fetch upcoming launches
    launches = fetch_data("https://api.spacexdata.com/v5/launches/upcoming")
    if not launches:
        return None

    # Find the soonest launch (minimum date_unix)
    soonest = None
    for launch in launches:
        try:
            date_unix = launch['date_unix']
            if soonest is None or date_unix < soonest['date_unix']:
                soonest = launch
        except KeyError:
            continue

    if not soonest:
        return None

    # Fetch rocket details
    rocket = fetch_data(
        "https://api.spacexdata.com/v4/rockets/{}".format(soonest['rocket'])
    )
    rocket_name = rocket['name'] if rocket else "Unknown Rocket"

    # Fetch launchpad details
    launchpad = fetch_data(
        "https://api.spacexdata.com/v4/launchpads/{}".format(
            soonest['launchpad']
        )
    )
    if launchpad:
        launchpad_name = launchpad['name']
        locality = launchpad['locality']
    else:
        launchpad_name = "Unknown Launchpad"
        locality = "Unknown Locality"

    return (
        soonest['name'],
        soonest['date_local'],
        rocket_name,
        launchpad_name,
        locality
    )


if __name__ == '__main__':
    next_launch = get_next_launch()
    if next_launch:
        name, date_local, rocket, pad, locality = next_launch
        print("{} ({}) {} - {} ({})".format(
            name, date_local, rocket, pad, locality
        ))
    else:
        print("No upcoming launches found")
        sys.exit(1)
