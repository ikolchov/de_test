from zipfile import ZipFile

from func_storage.read_movies_files import read_movies_file
from func_storage.read_rating_files import read_rating_file
from func_storage.read_users_files import read_users_file


def get_data_from_zip(location, movie_start_year=0, movie_end_year=9999, age_start=0, age_end=999):
    with ZipFile(location, 'r') as z:
        files_in_zip = [f for f in z.namelist() if f.endswith('.dat')]
        for file in files_in_zip:
            with z.open(file) as f:
                if file.endswith('movies.dat'):
                    movies_df = read_movies_file(f, start_year=movie_start_year, end_year=movie_end_year)
                elif file.endswith('users.dat'):
                    users_df = read_users_file(f, age_start=age_start, age_end=age_end)
                elif file.endswith('ratings.dat'):
                    ratings_df = read_rating_file(f)

    return movies_df, users_df, ratings_df
