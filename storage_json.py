import requests
import json

from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        """
        Constructor of class StorageJson. Initializes the instance variables.

        Parameters:
            file_path (str): The file path of the movie database JSON.
        """
        self.API_KEY = self.parse_json("data/api_key.json")["api_key"]
        self.MOVIE_DATA_URL = f"http://www.omdbapi.com/?apikey={self.API_KEY}&"
        self.file_path = file_path
        self.movie_dict = self.parse_json(self.file_path)

    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.

        The function loads the information from the JSON
        file and returns the data.

        For example, the function may return:
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
        return self.parse_json(self.file_path)

    def add_movie(self, movie_title, movie_data, fetch_successful):
        """
        Add a new movie with its name, rating, and other details to the database.
        Modify the JSON by adding the new movie to the database.
        """
        # fetch data and parse it from database
        try:
            if not fetch_successful:
                raise RuntimeError

            new_movie_title = movie_data["Title"]
            new_movie_rating = movie_data["imdbRating"]
            new_movie_year = movie_data["Year"]
            new_movie_poster = movie_data["Poster"]

            # check if movie is in database --> flag = True
            movie_in_database = False
            if new_movie_title in self.movie_dict:
                movie_in_database = True

            # add movie to database if it doesn't exist and response is true
            if movie_in_database:
                print(f"{new_movie_title} is already on the list")
            else:
                new_movie = {
                    "rating": new_movie_rating,
                    "year": new_movie_year,
                    "poster": new_movie_poster
                }
                self.movie_dict[new_movie_title] = new_movie
                self.modify_json(self.file_path, self.movie_dict)
                print(f"{new_movie_title} was successfully added to the list")

        except RuntimeError:
            print("We couldn't find the movie you were searching for")

        except requests.exceptions.ConnectionError as e:
            print(f"There was a connection Error. Please check your internet connection \n"
                  f"You can still use other menu commands while having no internet connection \n"
                  f"Further error details: {e} \n")

    def delete_movie(self):
        """
        Get user input for the movie name and delete the movie if it exists in the database.
        """
        movie_name = input("Enter movie name to delete: ").title()

        # check if movie is in database and delete it
        if movie_name in self.movie_dict:
            del self.movie_dict[movie_name]
            self.modify_json(self.file_path, self.movie_dict)
            print(f"{movie_name} was successfully deleted!")

        else:
            print(f"{movie_name} is not on the list\n")

    def update_movie(self):
        """
        Get user input for the movie name and the new movie rating.
        Find the movie in the database and update its rating.
        """
        movie_name = input("Enter a movie name to update: ").title()
        movie_in_database = False  # flag

        # Check if movie is in database
        if movie_name in self.movie_dict:
            movie_in_database = True

        if movie_in_database:
            new_movie_rating = float(input(f"Enter a new rating for {movie_name}: "))

            self.movie_dict[movie_name]["rating"] = new_movie_rating
            self.modify_json("data/movies_data.json", self.movie_dict)
            print(f"The rating of {movie_name} was successfully updated to {new_movie_rating}")
        else:
            print("This movie doesn't exist in the data base, please try again")
