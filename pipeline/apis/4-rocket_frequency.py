#!/usr/bin/env python3
"""
Count and display SpaceX launches per rocket
"""

import requests


def get_all_launches():
    """
    Retrieves all SpaceX launches from the latest API
    
    Returns:
        list: All launch records
    """
    try:
        response = requests.get(
            "https://api.spacexdata.com/latest/launches",
            timeout=15
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return []


def count_launches_by_rocket():
    """
    Counts launches per rocket and returns sorted results
    
    Returns:
        list: Tuples of (rocket_name, count) sorted per requirements
    """
    launches = get_all_launches()
    rocket_counts = {}

    # Count launches per rocket
    for launch in launches:
        rocket_name = launch.get('rocket', {}).get('name', 'Unknown Rocket')
        rocket_counts[rocket_name] = rocket_counts.get(rocket_name, 0) + 1

    # Sort by count (descending) then name (ascending)
    sorted_counts = sorted(
        rocket_counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    return sorted_counts


if __name__ == '__main__':
    rocket_counts = count_launches_by_rocket()
    for name, count in rocket_counts:
        print("{}: {}".format(name, count))
