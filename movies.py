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

    - Using a dictionary of movies as database, each movie is a dictionary:
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

    # Define a dictionary mapping user choices to corresponding functions
    choice_actions = {
        0: lambda: print("Bye!"),
        1: lambda: movies_storage.movie_list(movies),
        2: lambda: movies_storage.modify_json("data/movies_data.json",
                                              movies_storage.movie_add(movies, MOVIE_DATA_URL,
                                                                       API_KEY)),
        3: lambda: movies_storage.modify_json("data/movies_data.json",
                                              movies_storage.movie_delete(movies)),
        4: lambda: movies_storage.modify_json("data/movies_data.json",
                                              movies_storage.movie_update(movies)),
        5: lambda: menu.movie_stats(movies),
        6: lambda: menu.movie_random(movies),
        7: lambda: menu.movie_search(movies),
        8: lambda: menu.movie_sort(movies),
        9: lambda: menu.generate_website(movies, "_static/index_template.html")
    }

    # Menu will be displayed as an infinite loop. Only entry 0 breaks this loop
    while True:
        movies = movies_storage.parse_json("data/movies_data.json")
        user_choice = menu.show_menu_return_user_choice()

        try:
            correct_input = isinstance(user_choice, int) or user_choice < 0 or user_choice > 9

            if not correct_input:
                raise ValueError

            action = choice_actions.get(user_choice)
            if action:
                action()
                if user_choice == 0:
                    break
            else:
                raise ValueError

            input("\nPress enter to continue")

        except ValueError:
            print("Error! Please select one of the menu points 0-9")
            input("Press Enter to try again")


if __name__ == "__main__":
    main()
