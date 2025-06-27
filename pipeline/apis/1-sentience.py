#!/usr/bin/env python3
"""
Retrieve home planets of all sentient species from SWAPI.
"""

import requests
import time


def fetch_url(url):
    """
    Fetch data from a URL with exponential backoff for rate limits.

    Args:
        url (str): URL to fetch

    Returns:
        dict: JSON response data
    """
    retries = 0
    max_retries = 5

    while retries < max_retries:
        response = requests.get(url)
        if response.status_code == 429:
            wait_time = 2 ** retries
            time.sleep(wait_time)
            retries += 1
            continue
        response.raise_for_status()
        return response.json()

    raise Exception(f"Max retries exceeded for URL: {url}")

def sentientPlanets():
    """
    Returns a list of home planets of all sentient species.

    Returns:
        list: Names of home planets (with duplicates removed)
    """
    # Step 1: Fetch all sentient species
    species_url = "https://swapi-api.alx-tools.com/api/species/"
    sentient_species = []

    while species_url:
        data = fetch_url(species_url)
        for species in data["results"]:
            if species["designation"].lower() == "sentient":
                sentient_species.append(species)
        species_url = data["next"]

    # Step 2: Process homeworlds
    planet_id_to_name = {}
    null_homeworld = False

    for species in sentient_species:
        homeworld_url = species.get("homeworld")

        if homeworld_url is None:
            null_homeworld = True
            continue

        # Skip if we've already processed this planet URL
        if homeworld_url in planet_id_to_name:
            continue

        planet_data = fetch_url(homeworld_url)
        planet_id = planet_data["url"].split("/")[-2]
        planet_id_to_name[homeworld_url] = (int(planet_id), planet_data["name"])

    # Step 3: Create sorted planet list
    sorted_planets = sorted(
        planet_id_to_name.values(),
        key=lambda x: x[0]
    )
    planet_names = [name for (_, name) in sorted_planets]

    # Add 'unknown' if any species had null homeworld
    if null_homeworld:
        planet_names.append("unknown")

    return planet_names
