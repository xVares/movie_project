import random
import statistics


class MovieApp:
    def __init__(self, movie_storage):
        """
        Constructor of class MovieApp. has member from type IStorage
            storage (class): inherits all methods from StorageJson class
        """
        self._storage = movie_storage

    def show_menu_return_user_choice(self):
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

    def _command_list_movies(self):
        self._storage.list_movies()

    def _command_movie_stats(self):
        def average_movie_rating():
            """Loop over movie ratings, divide it by total movie amount and print average score."""
            number_of_movies = len(self._storage.movies_dict)
            rating_total = 0

            for movie_name in self._storage.movies_dict:
                movie_rating = self._storage.movies_dict[movie_name]["rating"]
                if movie_rating != 'N/A':
                    rating_total += float(movie_rating)
            print(
                f"The average score of all movies is: {round(rating_total / number_of_movies, 1)}")

        def median_movie_rating():
            """Calculate the median rating of all movies."""
            sorted_ratings = []

            for movie_data in self._storage.movies_dict.values():
                rating = movie_data.get("rating")
                if rating is not None and rating != "N/A":
                    sorted_ratings.append(float(rating))

            rating_median = statistics.median(sorted_ratings)
            print(f"The median of all movies is: {rating_median}")

        def best_movie_rating():
            """Find the movie with the highest rating."""
            best_movie_name = None
            best_rating = float("-inf")

            for movie_name, movie_data in self._storage.movies_dict.items():
                rating = movie_data.get("rating")
                if rating is not None and rating != "N/A":
                    rating_float = float(rating)
                    if rating_float > best_rating:
                        best_movie_name = movie_name
                        best_rating = rating_float

            if best_movie_name is not None:
                print(f"The movie with the current highest rating is: {best_movie_name} "
                      f"with a rating of {best_rating}")
            else:
                print("No movie ratings available.")

        def worst_movie_rating():
            """Find the movie with the highest rating."""
            worst_movie_name = None
            worst_rating = float("+inf")

            for movie_name, movie_data in self._storage.movies_dict.items():
                rating = movie_data.get("rating")
                if rating is not None and rating != "N/A":
                    rating_float = float(rating)
                    if rating_float < worst_rating:
                        worst_movie_name = movie_name
                        worst_rating = rating_float

            if worst_movie_name is not None:
                print(f"The movie with the current lowest rating is: {worst_movie_name} "
                      f"with a rating of {worst_rating}")
            else:
                print("No movie ratings available.")

        def movie_stats():
            """Wrapper function of (5. Stats) menu command. Calls four stat functions"""
            average_movie_rating()
            median_movie_rating()
            best_movie_rating()
            worst_movie_rating()

        movie_stats()

    def _command_movie_random(self):
        """
        Gets random movie dict from list of movie dicts and
        Uses key access to get title & rating.
        """
        random_movie_title = random.choice(list(self._storage.movies_dict))
        random_movie_rating = self._storage.movies_dict[random_movie_title].get("rating")
        print(f"\n"
              f"Your random movie: \n"
              f"Title: {random_movie_title} \n"
              f"Rating: {random_movie_rating} \n")

    def _command_search_movie(self):
        """
        Get search query from user and look for movies with matching titles.
        Function is NOT case-sensitive.
        """
        search_query = input("Search for a movie: ")
        found_movies = []

        for movie_title in self._storage.movies_dict.keys():
            if search_query.lower() in movie_title.lower():
                found_movies.append(movie_title)

        if found_movies:
            print(f"\n"
                  f"We found these movies according to your query '{search_query}':")
            for movie_title in found_movies:
                print(f"{movie_title}: {self._storage.movies_dict[movie_title].get('rating')}")
        else:
            print(f"I'm sorry! We couldn't find any movies according to your search query "
                  f"'{search_query}'.")

    def _command_sort_movie(self):
        """Sort movies by best rating and print them."""
        print("\n"
              "All movies sorted by their best rating in descending order:")
        sorted_movies = []

        for movie, details in self._storage.movies_dict.items():
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

    def _generate_website(self, static_html):
        """
        - Get _static/index_template.html,
        - Create HTML movie grid with movie properties
        - Create main index file and write new generated HTML to _static/index.html
        """

        # get template
        with open(static_html, "r") as f:
            index_template = f.read()

            complete_movie_grid = ""
            for movie_name, movie_data in self._storage.movies_dict.items():
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

    def run(self):
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

        # Create a dict mapping user choices to corresponding functions
        choice_actions = {
            0: lambda: print("Bye!"),
            1: lambda: self._storage.list_movies(),
            2: lambda: self._storage.storage.add_movie(),
            3: lambda: self._storage.delete_movie(),
            4: lambda: self._storage.update_movie(notes="add notes ?"),  # TODO: notes?
            5: lambda: self._command_movie_stats(),
            6: lambda: self._command_movie_random(),
            7: lambda: self._command_search_movie(),
            8: lambda: self._command_sort_movie(),
            9: lambda: self._generate_website("_static/index_template.html")
        }

        # Menu will be displayed as an infinite loop. Only entry 0 breaks this loop
        while True:
            try:
                user_choice = self.show_menu_return_user_choice()
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
