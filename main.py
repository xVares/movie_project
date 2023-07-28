from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv


def main():
    """
    The main function of the movie database application.

    - It creates an instance of either StorageJson or StorageCsv based on the file path provided.
    - It then initializes a MovieApp instance with the chosen storage.
    - Finally, it runs the movie application using the `run()` method of the MovieApp instance.

    The function dynamically selects the appropriate storage class based on the file path.

    Note: The file path determines which storage class will be used to handle the movie database.

    Supported File Formats:
    - JSON: If the file path contains "movies_data.json", StorageJson will be used.
    - CSV: If the file path contains "movies_data.csv", StorageCsv will be used.
    """
    file_path = "data/movies_data.json"

    if "movies_data.json" in file_path:
        storage = StorageJson(file_path)
        movie_app = MovieApp(storage)
        movie_app.run()

    elif "movies_data.csv" in file_path:
        storage = StorageCsv(file_path)
        movie_app = MovieApp(storage)
        movie_app.run()


if __name__ == "__main__":
    main()
