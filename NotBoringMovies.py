import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')]
    return cinema.sort_values(by='rating', ascending=False)
