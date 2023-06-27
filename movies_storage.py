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

    - Returns: a movie which is a dictionary. All key-value pairs are str:

        {
            "Title": "...",
            "Year": "..."
            "Ratings": [
                {
                    "Source": "...",
                    "Value": "..."
                }
            ],
            "...": ".."
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
def movie_list(list_of_movie_dicts):
    """List all the movies in movies_data.json."""
    print(f"\n{len(list_of_movie_dicts)} movies in total:")  # get amount of movies
    # iterate over dict and display key, val (movie & rating)
    for movie in list_of_movie_dicts:
        print("---------------------------------")
        for key, val in movie.items():
            try:
                print(f"{key.capitalize()}: {val}")
            except AttributeError:
                print(f"{key}: {val}")
        time.sleep(0.8)


# ==============================================================================
# 2. Add movie | Create
# ==============================================================================
def movie_add(list_of_movie_dicts, url, api_key):
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
            return list_of_movie_dicts

        new_movie_title = new_movie_data["Title"]
        new_movie_rating = new_movie_data["imdbRating"]
        new_movie_year = new_movie_data["Year"]
        new_movie_poster = new_movie_data["Poster"]

        movie_in_database = False
        # check if movie is in database --> flag = True
        for movie in list_of_movie_dicts:
            if new_movie_title == movie["title"]:
                movie_in_database = True
                break

        # add movie to database if it doesn't exist and response is true
        if movie_in_database:
            print(f"{new_movie_title} is already on the list")
        else:
            new_movie = {
                "title": new_movie_title,
                "rating": new_movie_rating,
                "year": new_movie_year,
                "poster": new_movie_poster
            }
            list_of_movie_dicts.append(new_movie)
            print(f"{new_movie_title} was successfully added to the list")
        return list_of_movie_dicts

    except requests.exceptions.ConnectionError as e:
        print(
            f"There was a connection Error. Please check your internet connection\n"
            f"You can still use the other menu commands while having no internet\n"
            f"Further error details: {e}\n"
        )


# ==============================================================================
# 3. Delete movie | Delete
# ==============================================================================
def movie_delete(list_of_movie_dicts):
    """
    - Get user input for movie name and delete the movie if it exists in the database
    - Return the modified database.
    """
    movie_name = input("Enter movie name to delete: ")

    movie_in_database = False  # flag
    movie_index = ""
    # check if movie is in database and get its index
    for movie in list_of_movie_dicts:
        if movie_name == movie["title"]:
            movie_in_database = True
            movie_index = list_of_movie_dicts.index(movie)
            break

    # del movie if input is in database
    if movie_in_database:
        del list_of_movie_dicts[movie_index]
        print(f"{movie_name} was successfully deleted!")
    else:
        print(f"{movie_name}is not on the list\n")
    return list_of_movie_dicts


# ==============================================================================
# 4. Update movie | Update
# ==============================================================================
def movie_update(list_of_movie_dicts):
    """
    - get user input:
        - movie name:         # string
        - new movie rating:   # float

    - find movie and update the rating in database
    """
    movie_name = input("Enter a movie name to update: ")
    movie_in_database = False  # flag
    movie_index = ""
    # Check if movie is in database and get its index
    for movie in list_of_movie_dicts:
        if movie_name == movie["title"]:
            movie_in_database = True
            movie_index = list_of_movie_dicts.index(movie)
            break

    if movie_in_database:
        new_movie_rating = float(input(f"Enter a new rating for {movie_name}: "))
        list_of_movie_dicts[movie_index]["rating"] = new_movie_rating
        print(f"The rating of {movie_name} was successfully updated to {new_movie_rating}")
    else:
        print("This movie doesn't exist in the data base, please try again")
    return list_of_movie_dicts
