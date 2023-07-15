import time
import requests

from istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path="data/movies_data.json"):
        """
        Constructor of class StorageJson. Constructs following instance variables:
            name (str): The name of the product.
            price (int): The price of the product.
            quantity (int): The quantity of the product.
            active (bool): The activation status of the product.
            promotion (obj): The Promotion obj of the product.
            maximum ()
        """
        self.file_path = file_path
        self.movies_dict = self.parse_json(self.file_path)

    def list_movies(self):
        """List all the movies in the dictionary of movie dictionaries."""
        # Iterate over the dictionary and display movie details
        print(f"\n{len(self.movies_dict)} movies in total:")
        for movie_title, movie_data in self.movies_dict.items():
            print(f"---------------------------------\n"
                  f"Title: {movie_title}")
            for key, val in movie_data.items():
                try:
                    print(f"{key.capitalize()}: {val}")
                except AttributeError:
                    print(f"{key}: {val}")
            time.sleep(0.8)

    def add_movie(self, url, api_key):
        """
           - Add a new movie with its name and rating to the database
           - Return the modified database
           """
        # fetch data and parse it from database
        try:
            user_movie_title_input = input("Enter new movie name: ")
            new_movie_data = self.fetch_data(url, api_key, {"t": user_movie_title_input})
            successful_fetch = self.fetching_successful(new_movie_data["Response"])

            if not successful_fetch:
                print("We couldn't find the movie you were searching for")
                return self.movies_dict

            new_movie_title = new_movie_data["Title"]
            new_movie_rating = new_movie_data["imdbRating"]
            new_movie_year = new_movie_data["Year"]
            new_movie_poster = new_movie_data["Poster"]

            movie_in_database = False
            # check if movie is in database --> flag = True
            if new_movie_title in self.movies_dict:
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
                self.movies_dict[new_movie_title] = new_movie
                print(f"{new_movie_title} was successfully added to the list")
            return self.movies_dict

        except requests.exceptions.ConnectionError as e:
            print(f"There was a connection Error. Please check your internet connection \n"
                  f"You can still use other menu commands while having no internet connection \n"
                  f"Further error details: {e} \n")

    def delete_movie(self, title):
        """
        - Get user input for movie name and delete the movie if it exists in the database
        - Return the modified database.
        """
        movie_name = input("Enter movie name to delete: ").title()

        # check if movie is in database and delete it
        if movie_name in self.movies_dict:
            del self.movies_dict[movie_name]
            print(f"{movie_name} was successfully deleted!")
        else:
            print(f"{movie_name} is not on the list\n")

        return self.movies_dict

    def update_movie(self, title, notes):
        """
        - get user input:
            - movie name:         # string
            - new movie rating:   # float

        - find movie and update the rating in database
        """
        movie_name = input("Enter a movie name to update: ").title()
        movie_in_database = False  # flag

        # Check if movie is in database
        if movie_name in self.movies_dict:
            movie_in_database = True

        if movie_in_database:
            new_movie_rating = float(input(f"Enter a new rating for {movie_name}: "))
            self.movies_dict[movie_name]["rating"] = new_movie_rating
            print(f"The rating of {movie_name} was successfully updated to {new_movie_rating}")
        else:
            print("This movie doesn't exist in the data base, please try again")
        return self.movies_dict
