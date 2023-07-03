import random
import statistics


# ==============================================================================
# Menu
# ==============================================================================
def show_menu_return_user_choice():
    """Print menu, return user choice for menu."""
    user_choice = int(input(
        "\n"
        "Menu:\n"
        "0. Exit\n"
        "1. List movies\n"
        "2. Add movie\n"
        "3. Delete movie\n"
        "4. Update movie\n"
        "5. Stats\n"
        "6. Random movie\n"
        "7. Search movie\n"
        "8. Movies sorted by rating\n"
        "9. Generate website\n"
        "\n"
        "Enter choice (0-9): "))

    return user_choice


# ==============================================================================
# 5. Stats | (Movie rating) - Average, Median, Best, Worst
# ==============================================================================
def movie_average_rating(dict_of_movie_dicts):
    """Loop over movie ratings, divide it by total movie amount and print average score."""
    number_of_movies = len(dict_of_movie_dicts)
    rating_total = 0

    for movie_name in dict_of_movie_dicts:
        movie_rating = dict_of_movie_dicts[movie_name]["rating"]
        if movie_rating != 'N/A':
            rating_total += float(movie_rating)
    print(f"The average score of all movies is: {round(rating_total / number_of_movies, 1)}")


def movie_median_rating(dict_of_movie_dicts):
    """Calculate the median rating of all movies."""
    sorted_ratings = []

    for movie_data in dict_of_movie_dicts.values():
        rating = movie_data.get("rating")
        if rating is not None and rating != "N/A":
            sorted_ratings.append(float(rating))

    rating_median = statistics.median(sorted_ratings)
    print(f"The median of all movies is: {rating_median}")


def movie_best_rating(dict_of_movie_dicts):
    """Find the movie with the highest rating."""
    best_movie_name = None
    best_movie_rating = float("-inf")

    for movie_name, movie_data in dict_of_movie_dicts.items():
        rating = movie_data.get("rating")
        if rating is not None and rating != "N/A":
            rating_float = float(rating)
            if rating_float > best_movie_rating:
                best_movie_name = movie_name
                best_movie_rating = rating_float

    if best_movie_name is not None:
        print(f"The movie with the current highest rating is: {best_movie_name} "
              f"with a rating of {best_movie_rating}")
    else:
        print("No movie ratings available.")


def movie_worst_rating(dict_of_movie_dicts):
    """Find the movie with the highest rating."""
    worst_movie_name = None
    worst_movie_rating = float("+inf")

    for movie_name, movie_data in dict_of_movie_dicts.items():
        rating = movie_data.get("rating")
        if rating is not None and rating != "N/A":
            rating_float = float(rating)
            if rating_float < worst_movie_rating:
                worst_movie_name = movie_name
                worst_movie_rating = rating_float

    if worst_movie_name is not None:
        print(f"The movie with the current lowest rating is: {worst_movie_name} "
              f"with a rating of {worst_movie_rating}")
    else:
        print("No movie ratings available.")


def movie_stats(dict_of_movie_dicts):
    """Wrapper function of (5. Stats) menu command. Calls four stat functions"""
    movie_average_rating(dict_of_movie_dicts)
    movie_median_rating(dict_of_movie_dicts)
    movie_best_rating(dict_of_movie_dicts)
    movie_worst_rating(dict_of_movie_dicts)


# ==============================================================================
# 6. Random movie
# ==============================================================================
def movie_random(dict_of_movie_dicts):
    """Gets random movie dict from list of movie dicts and use key access to get title & rating."""
    random_movie_title = random.choice(list(dict_of_movie_dicts))
    random_movie_rating = dict_of_movie_dicts[random_movie_title].get("rating")
    print(f"\n"
          f"Your random movie: \n"
          f"Title: {random_movie_title} \n"
          f"Rating: {random_movie_rating} \n")


# ==============================================================================
# 7. Search movie
# ==============================================================================
def movie_search(dict_of_movie_dicts):
    """
    Get search query from user and look for movies with matching titles.
    Function is NOT case-sensitive.
    """
    search_query = input("Search for a movie: ")
    found_movies = []

    for movie_title in dict_of_movie_dicts.keys():
        if search_query.lower() in movie_title.lower():
            found_movies.append(movie_title)

    if found_movies:
        print(f"\n"
              f"We found these movies according to your query '{search_query}':")
        for movie_title in found_movies:
            print(f"{movie_title}: {dict_of_movie_dicts[movie_title].get('rating')}")
    else:
        print(f"I'm sorry! We couldn't find any movies according to your search query "
              f"'{search_query}'.")


# ==============================================================================
# 8. Movies sorted by best rating
# ==============================================================================
def movie_sort(dict_of_movie_dicts):
    """Sort movies by best rating and print them."""
    print("\n"
          "All movies sorted by their best rating in descending order:")
    sorted_movies = []

    for movie, details in dict_of_movie_dicts.items():
        rating = details.get("rating")
        if rating == 'N/A':
            rating = 0.0
        else:
            rating = float(rating)
        sorted_movies.append((movie, rating))

    sorted_movies.sort(key=lambda x: x[1], reverse=True)

    for movie, rating in sorted_movies:
        if rating == 0.0:
            print(f"{movie}: N/A")
        else:
            print(f"{movie}: {rating}")


# ==============================================================================
# 9. Generate Website
# ==============================================================================
def generate_website(dict_of_movie_dicts, static_html):
    """
    - Get _static/index_template.html,
    - Create HTML movie grid with movie properties
    - Create main index file and write new generated HTML to _static/index.html
    """

    # get template
    with open(static_html, "r") as f:
        index_template = f.read()

        complete_movie_grid = ""
        for movie_name, movie_data in dict_of_movie_dicts.items():
            movie_title = movie_name
            movie_year = movie_data.get("year")
            movie_poster = movie_data.get("poster")

            movie_grid = f'<li>' \
                         f'<div class="movie">' \
                         f'<img class="movie-poster" src="{movie_poster}" title=""/>' \
                         f'<div class="movie-title">{movie_title}</div>' \
                         f'<div class="movie-year">{movie_year}</div>' \
                         f'</div>' \
                         f'</li>'
            complete_movie_grid += movie_grid

        index_title = index_template.replace("__TEMPLATE_TITLE__", "My Movie App")
        complete_index = index_title.replace("__TEMPLATE_MOVIE_GRID__", complete_movie_grid)

    # generate index.html
    with open("_static/index.html", "w") as f:
        f.write(complete_index)
        print("Website was generated successfully.")
