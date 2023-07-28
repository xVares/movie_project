from abc import ABC, abstractmethod
import json
import requests


class IStorage(ABC):
    @staticmethod
    def fetch_data(fetch_url, params):
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
        res = requests.get(fetch_url, params=params)
        return res.json()

    @staticmethod
    def fetching_successful(response):
        """
        Check if fetching was successful based on response value and return Boolean
        """
        if response == "True":
            return True
        return False

    @staticmethod
    def parse_json(file):
        """
        Parse JSON file in to python object and return it.
        """
        with open(file, "r") as f:
            return json.load(f)

    @staticmethod
    def modify_json(file, data):
        """
        Save modified data to file.
        """
        with open(file, "w") as f:
            json.dump(data, f)

    # abstract methods
    @abstractmethod
    def list_movies(self):
        """
        Prints every movie in the database
        """

    @abstractmethod
    def add_movie(self):
        """
        Add a movie to the storage system.
        """

    @abstractmethod
    def delete_movie(self):
        """
        Delete a movie from the storage system.
        """

    @abstractmethod
    def update_movie(self):
        """
        Update the movie manually.
        """
