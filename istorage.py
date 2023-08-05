from abc import ABC, abstractmethod
import json
import requests


class IStorage(ABC):
    @staticmethod
    def fetching_successful(response):
        """
        Check if fetching was successful based on response value and return Boolean
        """
        if response == "True":
            return True
        return False

    @staticmethod
    def modify_json(file_path, data):
        """
        Save modified data to file.
        """
        with open(file_path, "w") as f:
            json.dump(data, f)

    @staticmethod
    def parse_json(file):
        """
        Parse JSON file in to python object and return it.
        """
        with open(file, "r") as f:
            return json.load(f)

    # abstract methods
    @abstractmethod
    def list_movies(self):
        """
        Prints every movie in the database
        """

    @abstractmethod
    def add_movie(self, movie_title, movie_data, fetch_successful):
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
