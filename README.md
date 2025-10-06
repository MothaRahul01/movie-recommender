# Movie Recommender

A simple content-based movie recommendation system using Python.  
It recommends movies based on genres similarity using the [MovieLens dataset](https://grouplens.org/datasets/movielens/).

## Features
- Input a movie title and get top 5 similar movies.
- Uses **cosine similarity** on movie genres.
- Built with **Python**, **pandas**, and **scikit-learn**.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MothaRahul01/movie-recommender.git
   cd movie-recommender
Create a virtual environment (optional but recommended):

python -m venv venv
venv\Scripts\Activate.ps1   # For Windows PowerShell


Install dependencies:

pip install pandas scikit-learn

Usage

Place the MovieLens CSV files (movies.csv and u.data) in the project folder.

Run the recommender script:

python recommender.py


Enter a movie title when prompted to get top 5 recommended movies.

Example
Enter a movie you like: Toy Story (1995)

Top 5 movie recommendations:
1. A Bug's Life (1998)
2. Chicken Run (2000)
3. Monsters, Inc. (2001)
4. Shrek (2001)
5. Finding Nemo (2003)



