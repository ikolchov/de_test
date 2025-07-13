import pandas as pd
"""
All ratings are contained in the file "ratings.dat" and are in the
following format:

UserID::MovieID::Rating::Timestamp

- UserIDs range between 1 and 6040 
- MovieIDs range between 1 and 3952
- Ratings are made on a 5-star scale (whole-star ratings only)
- Timestamp is represented in seconds since the epoch as returned by time(2)
- Each user has at least 20 ratings
"""


def read_rating_file(file, sep='::'):
    # could be more
    chunk_size = 10_000
    chunks = []
    column_names = [
        'user_id',
        'movie_id',
        'rating',
        'timestamp'
    ]
    dtypes = {
        'user_id': 'str',
        'movie_id': 'str',
        'rating': 'int',
        'timestamp': 'str',
    }
    for chunk in pd.read_csv(file, sep=sep, chunksize=chunk_size,
                             engine='python',
                             dtype=dtypes, names=column_names,
                             header=None):
        # drop timestamp
        chunk = chunk[['user_id', 'movie_id', 'rating']]

        chunks.append(chunk)

    df = pd.concat(chunks)
    return df