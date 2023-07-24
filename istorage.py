import json
import time

import requests

from abc import ABC, abstractmethod


class IStorage(ABC):
    @staticmethod
    def fetch_data(request_url, api_key, params):
        """
        - Fetches data from the specified URL using the provided API key and parameters.

        - Parameters:
            - request_url (str): The URL to fetch data from.
            - api_key (str): The API key to authenticate the request.
            - params (dict): A dictionary of parameters to include in the request.

        - Returns: a dictionary of movie dictionaries. All key-value pairs are str:

    {
        "Title": {
            "rating": "...",
            "year": "...",
            "poster": "..."
        },
        "Title": {
            "rating": "...",
            "year": "...",
            "poster": "..."
        },
        "Title": {
            "rating": "...",
            "year": "...",
            "poster": "..."
        }
    }
        """
        correct_url = f"{request_url}{api_key}"
        res = requests.get(correct_url, params=params)
        return res.json()

    @staticmethod
    def fetching_successful(response):
        """check if fetching was successful based on response value"""
        if response == "True":
            return True
        return False

    @staticmethod
    def parse_json(file):
        """Parse json file in to python object and load it."""
        with open(file, "r") as f:
            return json.load(f)

    @staticmethod
    def modify_json(file, data):
        """Save modified data to file."""
        with open(file, "w") as f:
            json.dump(data, f)

    # abstract methods
    @abstractmethod
    def list_movies(self):
        """Retrieve a list of movies stored in the storage system.

        Returns:
            list: A list of movie objects.
        """

    @abstractmethod
    def add_movie(self):
        """Add a movie to the storage system.

        Args:
            url (str): URL to make a fetch request (OMDb).
        """

    @abstractmethod
    def delete_movie(self):
        """Delete a movie from the storage system.

        Args:
            title (str): The title of the movie to be deleted.
        """

    @abstractmethod
    def update_movie(self, notes):
        """Update the notes for a movie in the storage system.

        Args:
            notes (str): The updated notes for the movie.
        """
