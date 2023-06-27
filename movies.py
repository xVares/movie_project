import movies_menu_functions as menu
import movies_storage

API_KEY = movies_storage.parse_json("data/api_key.json")["api_key"]
MOVIE_DATA_URL = f"http://www.omdbapi.com/?apikey={API_KEY}&"


# ==============================================================================
# Main
# ==============================================================================
def main():
    """
    Entry point of application

    - Using a list of movies as database, each movie is a dictionary:
        [
          {
            "title": "...", # string
            "rating": ...,  # float
            "year": ...     # int
          },
          {
            "title": "...", # string
            "rating": ...,  # float
            "year": ...     # int
          }
        ]

    - The menu has 9 entries and will be displayed as follows:
        0. Exit
        1. List movies
        2. Add movie
        3. Delete movie
        4. Update movie
        5. Stats
        6. Random movie
        7. Search movie
        8. Movies sorted by rating
        9. Generate Website
    """

    print("********** My Movies Database **********")

    # Menu will be displayed as infinite loop. Only entry 0 breaks this loop
    while True:
        movies = movies_storage.parse_json("data/movies_data.json")
        # Print menu and store user input in user_choice
        user_choice = menu.menu_and_user_choice()

        if user_choice == 0:
            print("Bye!")
            break

        elif user_choice == 1:
            movies_storage.movie_list(movies)
            input("\nPress enter to continue")

        elif user_choice == 2:
            modified_data = movies_storage.movie_add(movies, MOVIE_DATA_URL, API_KEY)
            movies_storage.modify_json("data/movies_data.json", modified_data)
            input("\nPress enter to continue")

        elif user_choice == 3:
            modified_data = movies_storage.movie_delete(movies)
            movies_storage.modify_json("data/movies_data.json", modified_data)
            input("\nPress enter to continue")

        elif user_choice == 4:
            modified_data = movies_storage.movie_update(movies)
            movies_storage.modify_json("data/movies_data.json", modified_data)
            input("\nPress enter to continue")

        elif user_choice == 5:
            menu.movie_stats(movies)
            input("\nPress enter to continue")

        elif user_choice == 6:
            menu.movie_random(movies)
            input("\nPress enter to continue")

        elif user_choice == 7:
            menu.movie_search(movies)
            input("\nPress enter to continue")

        elif user_choice == 8:
            menu.movie_sort(movies)
            input("\nPress enter to continue")

        elif user_choice == 9:
            menu.generate_website(movies, "_static/index_template.html")
            input("\nPress enter to continue")


if __name__ == "__main__":
    main()
