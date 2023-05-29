# Movie Recommendation System

![App Screenshot](template\images\app_screenshot.png)


This is a movie recommendation system built using Python. The system utilizes a movie dataset to provide recommendations based on user input.

## Dataset

The dataset used in this project consists of two CSV files:

1. `tmdb_5000_movies.csv`: This file contains information about movies, including title, genres, overview, cast, crew, and keywords.
2. `tmdb_5000_credits.csv`: This file provides credits information for the movies.

## Usage

To use the movie recommendation system, follow these steps:

1. Make sure you have the necessary Python libraries installed, including pandas, numpy, and ast.
2. Download the dataset files (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`).
3. Update the file paths in the script to point to the correct locations of the dataset files.
4. Run the Python script to preprocess the data and build the recommendation system.
5. Once the system is ready, you can provide a movie title as input to get recommendations based on that movie.

## Data Preprocessing

The data preprocessing steps performed in the script include:

1. Merging the two datasets based on movie title.
2. Cleaning the data by removing unwanted columns and dropping rows with missing values.
3. Extracting and converting relevant information from certain columns, such as genres, keywords, cast, and crew.
4. Preparing the data for recommendation by concatenating the relevant columns to form a new column called "tags".
5. Performing text vectorization to represent the movie tags as numerical vectors.
6. Calculating cosine similarity between the vectors to measure similarity between movies.

## Movie Recommendation

![App Screenshot](template\images\app_screenshot.png)


The movie recommendation system recommends movies based on user input. You can provide a movie title, and the system will find similar movies based on cosine similarity scores. The top five recommended movies will be displayed.

## Files

- `script.py`: The Python script that performs data preprocessing and builds the movie recommendation system.
- `tmdb_5000_movies.csv`: The movie dataset file containing movie information.
- `tmdb_5000_credits.csv`: The credits dataset file containing credits information.

Feel free to explore and modify the script according to your needs to enhance the movie recommendation system.

