from istorage import IStorage
import time
import requests
import csv
import pandas as pd


class StorageCsv(IStorage):
    def __init__(self, file_path="data/movies_data.csv"):
        """
        Constructor of class StorageCsv. Initializes the instance variables.

        Parameters:
            file_path (str, optional): The file path of the CSV containing movie data.
        """
        self.API_KEY = self.parse_json("data/api_key.json")["api_key"]
        self.MOVIE_FETCH_URL = f"http://www.omdbapi.com/?apikey={self.API_KEY}&"
        self.file_path = file_path
        self.movie_data_csv = self.return_csv_lines()
        self.movie_dict = self.list_to_dict_conversion()

    def modify_csv(self, data):
        """
        Modifies the CSV file with new data.

        Parameters:
            data (list): List of data to be appended to the CSV file.
        """
        with open(self.file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    def return_csv_lines(self):
        """
        Returns an ordered list of every cell in the CSV.

        Returns:
            list: List of strings representing each cell in the CSV.
        """
        with open(self.file_path, "r") as f:
            data = f.read()
            data_cells = data.split("\n")
            return data_cells

    def list_to_dict_conversion(self):
        """
        Serializes CSV data to a dictionary and assigns it to the instance variable.

        Returns:
            dict: A dictionary containing movie data with movie titles as keys and rating/year as values.
        """
        movie_dict = {}
        for movie_data in self.movie_data_csv[1:]:
            try:
                title, rating, year = movie_data.split(",")

                # Add the movie data to the movie_dict using the movie_title as key
                movie_dict[title] = {
                    "rating": rating,
                    "year": year
                }
            except ValueError:
                pass
        return movie_dict

    def list_movies(self):
        """
        Prints every movie in the database along with its details.
        """
        # ['title, rating, year', 'Titanic, 9.2, 1995', 'The Dark Knight, 8.8, 2002']

        print(f"\n{len(self.movie_data_csv) - 2} movies in total:")
        for movie in self.movie_data_csv[1:]:
            if movie == "":
                break
            title, rating, year = movie.split(",")
            print(f"---------------------------------\n"
                  f"Title: {title}\n"
                  f"Rating: {rating}\n"
                  f"Year: {year}")
            time.sleep(0.8)

    def add_movie(self):
        """
        Add a movie to the storage system by fetching its data from an external API
        and saving it to the CSV file.
        """
        try:
            user_movie_title = input("Enter new movie name: ")
            new_movie_data = self.fetch_data(self.MOVIE_FETCH_URL, {"t": user_movie_title})
            fetch_successful = self.fetching_successful(new_movie_data["Response"])

            if not fetch_successful:
                raise RuntimeError

            new_movie_title = str(new_movie_data["Title"])
            new_movie_rating = str(new_movie_data["imdbRating"])
            new_movie_year = str(new_movie_data["Year"])

            # check if movie is in database --> flag = True
            movie_in_database = False
            if new_movie_title in self.movie_dict:
                movie_in_database = True

            # add movie to database if it doesn't exist and response is true
            if movie_in_database:
                print(f"{new_movie_title} is already on the list")
            else:
                new_movie = [new_movie_title, new_movie_rating, new_movie_year]

                self.modify_csv([new_movie])

                # Update in-memory storage
                self.movie_data_csv = self.return_csv_lines()
                self.movie_dict = self.list_to_dict_conversion()
                print(f"{new_movie_title} was successfully added to the list")

        except RuntimeError:
            print("We couldn't find the movie you were searching for")

        except requests.exceptions.ConnectionError as e:
            print(f"There was a connection Error. Please check your internet connection \n"
                  f"You can still use other menu commands while having no internet connection \n"
                  f"Further error details: {e} \n")

    def delete_movie(self):
        """
        Delete a movie from the storage system based on user input (movie_name).
        """
        movie_name = input("Enter movie name to delete: ").title()

        # Check if movie is in database
        if movie_name in self.movie_dict:
            print("Movie is already on the database")

            # Use pandas to delete the movie from the CSV file
            df = pd.read_csv(self.file_path)
            df = df[df['title'] != movie_name]
            df.to_csv(self.file_path, index=False)

            # Update the in-memory storage
            self.movie_data_csv = self.return_csv_lines()
            self.movie_dict = self.list_to_dict_conversion()

            print(f"Movie '{movie_name}' deleted successfully.")
        else:
            print(f"Movie '{movie_name}' not found in the CSV file.")

    def update_movie(self):
        """
        Update the rating of a movie in the storage system
        based on user input (movie name and new rating).
        """
        movie_name = input("Enter a movie name to update: ").title()
        movie_in_database = False  # flag

        # Check if movie is in database
        if movie_name in self.movie_dict:
            movie_in_database = True

        if movie_in_database:
            new_movie_rating = float(input(f"Enter a new rating for {movie_name}: "))

            self.movie_dict[movie_name]["rating"] = new_movie_rating
            self.modify_json("data/movie_dict.json", self.movie_dict)
            print(f"The rating of {movie_name} was successfully updated to {new_movie_rating}")
        else:
            print("This movie doesn't exist in the data base, please try again")
