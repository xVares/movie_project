from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    """
    The main function of the movie database application.

    - It creates an instance of either StorageJson or StorageCsv based on the user choice.
    - It then initializes a MovieApp instance with the chosen storage.
    - Finally, it runs the movie application using the `run()` method of the MovieApp instance.

    The function dynamically selects the appropriate storage class based on the chosen option.

    Note: The file path determines which storage class will be used to handle the movie database.

    Supported File Formats:
    - JSON: If the user selects option 1, StorageJson will be used.
    - CSV: If the user selects option 2, StorageCsv will be used.
    """
    storage_types = {
        1: "data/movies_data.json",
        2: "data/movies_data.csv"
    }

    # Storage choice will be displayed as infinite loop, until 1 or 2 is chosen
    while True:
        try:
            user_storage_choice = int(input("Which Storage would you like to use?\n"
                                            "1. JSON\n"
                                            "2. CSV\n"
                                            "\n"
                                            "Enter your choice (1-2): "))

            file_path = storage_types.get(user_storage_choice)

            if file_path is None:
                raise ValueError
            else:
                if user_storage_choice == 1:
                    storage = StorageJson(file_path)
                    movie_app = MovieApp(storage)
                    movie_app.run()
                    break
                elif user_storage_choice == 2:
                    storage = StorageCsv(file_path)
                    movie_app = MovieApp(storage)
                    movie_app.run()
                    break
        except ValueError:
            print("Please select one of the storage options 1-2")
            input("Press Enter to try again\n")


if __name__ == "__main__":
    main()
