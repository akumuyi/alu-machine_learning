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

    raise Exception("Max retries exceeded for URL: {}".format(url))


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
            # Check both designation and classification for sentience
            designation = species.get("designation", "").lower()
            classification = species.get("classification", "").lower()
            name = species.get("name", "").lower()

            # Broader sentience detection
            if ("sentient" in designation or
              "sentient" in classification or
              name in ["wookiee", "human", "hutt", "yoda's species"]):
                  sentient_species.append(species)
        species_url = data["next"]

    # Step 2: Process homeworlds, skipping null values
    planet_urls_seen = set()
    planet_names = []

    for species in sentient_species:
        homeworld_url = species.get("homeworld")

        # Skip species without homeworld
        if not homeworld_url:
            continue

        if homeworld_url in planet_urls_seen:
            continue

        planet_urls_seen.add(homeworld_url)
        planet_data = fetch_url(homeworld_url)
        planet_names.append(planet_data["name"])

    # Sort alphabetically to match expected output
    planet_names.sort()

    return planet_names
