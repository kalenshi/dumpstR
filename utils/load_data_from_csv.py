import csv
import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
netflix_movies = os.path.join(BASE_DIR, "netflix_titles.csv")


def load_data(filepath):
    """
    Loads data from csv file and returns as a pandas dataframe
    Args:
        filepath:

    Returns:

    """
    df = pd.read_csv(filepath)

    print(df.columns)
    # with open(filepath, encoding="utf8", newline="") as csvfile:
    #     count = 0
    #     spread_sheet = csv.DictReader(csvfile)
    #     df = pd.DataFrame()
    #     for row in spread_sheet:
    #         df._append(df.Series(row, index=df.index))
    #
    #     print(df.head())


if __name__ == '__main__':
    load_data(netflix_movies)
