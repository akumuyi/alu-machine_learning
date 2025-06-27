#!/usr/bin/env python3
"""
Count and display SpaceX launches per rocket
"""

import requests


def get_all_launches():
    """
    Retrieves all SpaceX launches with pagination handling
    
    Returns:
        list: All launch records
    """
    base_url = "https://api.spacexdata.com/v4/launches"
    all_launches = []
    page = 1

    while True:
        try:
            # Get paginated results
            response = requests.get(
                base_url,
                params={'page': page, 'limit': 200},
                timeout=10
            )
            response.raise_for_status()
            page_data = response.json()

            if not page_data:
                break

            all_launches.extend(page_data)
            page += 1

        except requests.exceptions.RequestException:
            break

    return all_launches


def get_rocket_name(rocket_id):
    """
    Fetches rocket name by ID
    
    Args:
        rocket_id (str): Rocket identifier
        
    Returns:
        str: Rocket name or placeholder if unavailable
    """
    try:
        url = "https://api.spacexdata.com/v4/rockets/{}".format(rocket_id)
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        rocket_data = response.json()
        return rocket_data.get('name', "Unknown Rocket ({})".format(rocket_id))
    except requests.exceptions.RequestException:
        return "Unknown Rocket ({})".format(rocket_id)


def count_launches_by_rocket():
    """
    Counts launches per rocket and returns sorted results
    
    Returns:
        list: Tuples of (rocket_name, count) sorted per requirements
    """
    launches = get_all_launches()
    rocket_counts = {}

    # Count launches per rocket ID
    for launch in launches:
        rocket_id = launch.get('rocket')
        if rocket_id:
            rocket_counts[rocket_id] = rocket_counts.get(rocket_id, 0) + 1

    # Convert to name-based counts
    name_counts = {}
    for rocket_id, count in rocket_counts.items():
        name = get_rocket_name(rocket_id)
        name_counts[name] = name_counts.get(name, 0) + count

    # Convert to sorted list
    sorted_counts = sorted(
        name_counts.items(),
        key=lambda x: (-x[1], x[0])  # Descending count, ascending name
    )

    return sorted_counts


if __name__ == '__main__':
    rocket_counts = count_launches_by_rocket()
    for name, count in rocket_counts:
        print("{}: {}".format(name, count))
