import pandas as pd

"""
MovieID::Title::Genres

- Titles are identical to titles provided by the IMDB (including year of release)
- Genres are pipe-separated and are selected from the following genres:

	* Action
	* Adventure
	* Animation
	* Children's
	* Comedy
	* Crime
	* Documentary
	* Drama
	* Fantasy
	* Film-Noir
	* Horror
	* Musical
	* Mystery
	* Romance
	* Sci-Fi
	* Thriller
	* War
	* Western

- Some MovieIDs do not correspond to a movie due to accidental duplicate
entries and/or test entries
- Movies are mostly entered by hand, so errors and inconsistencies may exist


     movie_id                               title                        genres
0           1                    Toy Story (1995)   Animation|Children's|Comedy
1           2                      Jumanji (1995)  Adventure|Children's|Fantasy

"""


def read_movies_file(file, start_year=0, end_year=9999, sep='::'):
    # could be more
    chunk_size = 10_000
    chunks = []
    column_names = [
        'movie_id',
        'title',
        'genres',
    ]
    dtypes = {
        'movie_id': 'str',
        'title': 'str',
        'genres': 'str',
    }

    for chunk in pd.read_csv(file, sep=sep, chunksize=chunk_size,
                             engine='python', encoding='latin1',
                             dtype=dtypes, names=column_names,
                             header=None):
        # year should be at the end of the column, could be also with regex but should be way slower
        chunk['year'] = chunk['title'].str[-5:-1].astype(int)
        chunk['movie_title'] = chunk['title'].str[:-7].str.strip()

        # dump genres to a list
        chunk['movie_genres'] = chunk['genres'].str.split('|')
        chunk = chunk[['movie_id', 'year', 'movie_genres']]
        chunk = chunk.loc[(chunk['year'] >= start_year)
                          & (chunk['year'] < end_year)]
        chunks.append(chunk)

    df = pd.concat(chunks)
    return df
