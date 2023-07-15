import json
import time

import requests


# ==============================================================================
# Fetch data and parse json
# ==============================================================================
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


def fetching_successful(response):
    """check if fetching was successful based on response value"""
    if response == "True":
        return True
    return False


def parse_json(file):
    """Parse json file to python object and load it."""
    with open(file, "r") as f:
        return json.load(f)


def modify_json(file, data):
    """Safe modified data to file."""
    with open(file, "w") as f:
        json.dump(data, f)


# CRUD functions

# ==============================================================================
# 1. List movies | Read
# ==============================================================================
def movie_list(dict_of_movie_dicts):
    """List all the movies in the dictionary of movie dictionaries."""
    # Iterate over the dictionary and display movie details
    print(f"\n{len(dict_of_movie_dicts)} movies in total:")
    for movie_title, movie_data in dict_of_movie_dicts.items():
        print(f"---------------------------------\n"
              f"Title: {movie_title}")
        for key, val in movie_data.items():
            try:
                print(f"{key.capitalize()}: {val}")
            except AttributeError:
                print(f"{key}: {val}")
        time.sleep(0.8)


# ==============================================================================
# 2. Add movie | Create
# ==============================================================================
def movie_add(dict_of_movie_dicts, url, api_key):
    """
    - Add a new movie with its name and rating to the database
    - Return the modified database
    """
    # fetch data and parse it from database
    try:
        user_movie_title_input = input("Enter new movie name: ")
        new_movie_data = fetch_data(url, api_key, {"t": user_movie_title_input})
        successful_fetch = fetching_successful(new_movie_data["Response"])

        if not successful_fetch:
            print("We couldn't find the movie you were searching for")
            return dict_of_movie_dicts

        new_movie_title = new_movie_data["Title"]
        new_movie_rating = new_movie_data["imdbRating"]
        new_movie_year = new_movie_data["Year"]
        new_movie_poster = new_movie_data["Poster"]

        movie_in_database = False
        # check if movie is in database --> flag = True
        if new_movie_title in dict_of_movie_dicts:
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
            dict_of_movie_dicts[new_movie_title] = new_movie
            print(f"{new_movie_title} was successfully added to the list")
        return dict_of_movie_dicts

    except requests.exceptions.ConnectionError as e:
        print(f"There was a connection Error. Please check your internet connection \n"
              f"You can still use other menu commands while having no internet connection \n"
              f"Further error details: {e} \n")


# ==============================================================================
# 3. Delete movie | Delete
# ==============================================================================
def movie_delete(dict_of_movie_dicts):
    """
    - Get user input for movie name and delete the movie if it exists in the database
    - Return the modified database.
    """
    movie_name = input("Enter movie name to delete: ").title()

    # check if movie is in database and delete it
    if movie_name in dict_of_movie_dicts:
        del dict_of_movie_dicts[movie_name]
        print(f"{movie_name} was successfully deleted!")
    else:
        print(f"{movie_name} is not on the list\n")

    return dict_of_movie_dicts


# ==============================================================================
# 4. Update movie | Update
# ==============================================================================
def movie_update(dict_of_movie_dicts):
    """
    - get user input:
        - movie name:         # string
        - new movie rating:   # float

    - find movie and update the rating in database
    """
    movie_name = input("Enter a movie name to update: ").title()
    movie_in_database = False  # flag

    # Check if movie is in database
    if movie_name in dict_of_movie_dicts:
        movie_in_database = True

    if movie_in_database:
        new_movie_rating = float(input(f"Enter a new rating for {movie_name}: "))
        dict_of_movie_dicts[movie_name]["rating"] = new_movie_rating
        print(f"The rating of {movie_name} was successfully updated to {new_movie_rating}")
    else:
        print("This movie doesn't exist in the data base, please try again")
    return dict_of_movie_dicts
