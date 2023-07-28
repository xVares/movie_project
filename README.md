# Movie Project

## Overview

The Movie Project is an ongoing Python project that I started with a basic understanding of programming. The purpose of
this project is to continuously improve my programming skills by implementing new concepts and features along the way.
This README provides an overview of the project and its functionalities.

Furthermore, this is a Python project that provides a simple database for managing a list of movies. It allows you to
perform various operations on the movie data, such as listing movies, adding new movies, deleting movies, updating movie
details, generating statistics, searching movies, sorting movies by rating, and generating a website.

## Functionality

The application utilizes the OMDb API to fetch movie data based on user search queries. By leveraging the data from
the [OMDb API](http://www.omdbapi.com/), the application creates a movie library. The movie library is then displayed in
a visually appealing grid format on a static website.

## Prerequisites

To run this project, ensure that you have the following:

- Python 3.x installed on your system.
- Your own API key from [OMDb API](http://www.omdbapi.com/) (details in [Configuration section](#configuration))

## Installation

1. Clone the project repository to your local machine:

```bash
git clone <repository_url>
```

2. Install the dependencies by running the following command:

```bash
pip install -r requirements.txt
```

<a name="configuration"></a>

## Configuration

Before running the project, make sure to set up the API key. Follow these steps:

1. Create a file named `api_key.json` inside the `data` directory.

2. In the `api_key.json` file, add the following JSON object:

```json
{
    "api_key": "YOUR_API_KEY"
}
```

3. Replace `YOUR_API_KEY` with your actual API key inside the quotation marks to fetch movie data.

## Usage

To start the application, run the following command:

```bash
python main.py
```

The application will display a menu with various options. Choose the desired option by entering the corresponding
number. The available menu options are:

1. **List movies**: Display the list of movies in the database.
2. **Add movie**: Add a new movie to the database by providing movie details.
3. **Delete movie**: Remove a movie from the database by specifying its title.
4. **Update movie**: Update the details of a movie in the database.
5. **Stats**: Generate and display statistics about the movies in the database.
6. **Random movie**: Get a random movie suggestion from the database.
7. **Search movie**: Search for a movie by title.
8. **Movies sorted by rating**: Sort and display the movies in the database by rating.
9. **Generate Website**: Generate a website using the movie data and a provided template.

To exit the application, choose the "Exit" option from the menu by entering `0`.

## Data Storage

The movie data is stored in the `data` directory either as a JSON file named `movies_data.json` or as a CSV file
named `movies_data.csv`. You can modify this file directly or use the application's menu options to add, delete, and
update movies.