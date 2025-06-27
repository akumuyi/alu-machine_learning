#!/usr/bin/env python3
"""
Retrieve starships from SWAPI that can hold a given number of passengers.
"""

import requests


def availableShips(passengerCount):
    """
    Returns a list of ships that can hold at least the given number
    of passengers.

    Args:
        passengerCount (int): Minimum number of passengers the ship must support
    
    Returns:
        list: Names of ships meeting the passenger requirement
    """
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships_list = []
    
    while url:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()
            
            for ship in data['results']:
                # Handle different passenger value formats
                passengers = ship.get('passengers', '0').replace(',', '')
                
                try:
                    # Convert to int if possible, skip if non-digit values
                    if passengers.isdigit():
                        if int(passengers) >= passengerCount:
                            ships_list.append(ship['name'])
                except AttributeError:
                    # Handle cases where passengers might be None
                    continue
                    
            url = data['next']  # Get next page URL
            
        except requests.exceptions.RequestException:
            break  # Exit loop on any request error
    
    return ships_list

