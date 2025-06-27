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
    base_url = "https://api.spacexdata.com/v5/launches"
    all_launches = []
    page = 1

    while True:
        try:
            # Get paginated results
            response = requests.get(
                base_url,
                params={'page': page, 'limit': 200, 'populate': 'rocket'},
                timeout=20
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


def count_launches_by_rocket():
    """
    Counts launches per rocket type and returns sorted results
    
    Returns:
        list: Tuples of (rocket_name, count) sorted per requirements
    """
    launches = get_all_launches()
    rocket_counts = {}

    # Count launches per rocket type
    for launch in launches:
        try:
            # Get rocket name directly from populated data
            rocket_name = launch['rocket']['name']
        except (KeyError, TypeError):
            continue
            
        rocket_counts[rocket_name] = rocket_counts.get(rocket_name, 0) + 1

    # Convert to sorted list
    sorted_counts = sorted(
        rocket_counts.items(),
        key=lambda x: (-x[1], x[0])  # Descending count, ascending name
    )

    return sorted_counts


if __name__ == '__main__':
    rocket_counts = count_launches_by_rocket()
    for name, count in rocket_counts:
        print("{}: {}".format(name, count))
