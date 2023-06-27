import random
import statistics


# ==============================================================================
# Menu
# ==============================================================================
def menu_and_user_choice():
    """Print menu, return user choice for menu."""
    user_choice = int(
        input(
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
            "Enter choice (0-9): "
        )
    )
    return user_choice


# ==============================================================================
# 5. Stats | (Movie rating) Average, Median, Best, Worst
# ==============================================================================
def movie_average_rating(list_of_movie_dicts):
    """Loop over movie ratings, divide it by total movie amount and print average score."""
    movie_amount = len(list_of_movie_dicts)
    rating_total = 0

    for movie in list_of_movie_dicts:
        rating_total += float(movie["rating"])

    print(f"The average score of all movies is: {round(rating_total / movie_amount, 1)}")


def movie_median_rating(list_of_movie_dicts):
    """
    Sort movies by rating, loop over ratings and append them in sorted order to empty list.
    Finally Print median.
    """
    sorted_movies = sorted(list_of_movie_dicts, key=lambda movies: movies["rating"])
    sorted_ratings = []
    for movie in sorted_movies:
        sorted_ratings.append(float(movie["rating"]))

    rating_median = statistics.median(sorted_ratings)
    print(f"The median of all movies is: {rating_median}")


def movie_best_rating(list_of_movie_dicts):
    """Sort list of movie dicts by best rating and print best movie rating & title."""
    sorted_movies = sorted(list_of_movie_dicts, reverse=True, key=lambda movies: movies["rating"])
    best_movie_name = sorted_movies[0]["title"]
    best_movie_rating = float(sorted_movies[0]["rating"])

    print(
        f"The movie with the current highest rating is: {best_movie_name} "
        f"with a rating of {best_movie_rating}"
    )


def movie_worst_rating(list_of_movie_dicts):
    """Sort list of movie dicts by worst rating and print worst movie rating & title."""
    sorted_movies = sorted(list_of_movie_dicts, reverse=False, key=lambda movies: movies["rating"])
    worst_movie_name = sorted_movies[0]["title"]
    worst_movie_rating = float(sorted_movies[0]["rating"])

    print(
        f"The movie with the current worst rating is: {worst_movie_name} with a rating of"
        f" {worst_movie_rating}"
    )


def movie_stats(list_of_movie_dicts):
    """Wrapper function of (5. Stats) menu command. Calls four stat functions"""
    movie_average_rating(list_of_movie_dicts)
    movie_median_rating(list_of_movie_dicts)
    movie_best_rating(list_of_movie_dicts)
    movie_worst_rating(list_of_movie_dicts)


# ==============================================================================
# 6. Random movie
# ==============================================================================
def movie_random(list_of_movie_dicts):
    """Gets random movie dict from list of movie dicts and use key access to get title & rating."""
    random_movie = random.choice(list_of_movie_dicts)
    print(f"{random_movie['title']}: {random_movie['rating']}")


# ==============================================================================
# 7. Search movie
# ==============================================================================
def movie_search(list_of_movie_dicts):
    """Get search query from user and look for suiting movie titles. Fn is NOT case-sensitive."""
    search_query = input("Search for a movie: ")

    movie_in_database = False
    for movie in list_of_movie_dicts:
        if search_query in movie["title"]:
            print(
                f"\nWe found these movies according to your query '{search_query}':\n")
            movie_in_database = True
            print(f"{movie['title']}: {movie['rating']}")

    if not movie_in_database:
        print("I'm sorry! We couldn't find any movies according to your search query")


# ==============================================================================
# 8. Movies sorted by best rating
# ==============================================================================
def movie_sort(list_of_movie_dicts):
    """Sort movies by best rating and print them."""
    sorted_movies = sorted(list_of_movie_dicts, reverse=True, key=lambda movies: movies["rating"])

    for movie in sorted_movies:
        print(f"{movie['title']} {movie['rating']}")


# ==============================================================================
# 9. Generate Website
# ==============================================================================
def generate_website(list_of_movie_dicts, static_html):
    """
    - Get _static/index_template.html,
    - Create HTML movie grid with movie properties
    - Create main index file and write new generated HTML to _static/index.html
    """

    # get template
    with open(static_html, "r") as f:
        index_template = f.read()

        complete_movie_grid = ""
        for movie in list_of_movie_dicts:
            movie_title = movie["title"]
            movie_year = movie["year"]
            movie_poster = movie["poster"]

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
