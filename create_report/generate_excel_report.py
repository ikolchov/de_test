import pandas as pd


def generate_excel_report(movies_df, users_df, ratings_df, destination_folder, report_name):
    # combine movies with rating

    movie_rating_df = pd.merge(
        movies_df,
        ratings_df,
        left_on='movie_id',
        right_on='movie_id',
        how='inner'
    )
    movie_rating_users_df = pd.merge(
        movie_rating_df,
        users_df,
        left_on='user_id',
        right_on='user_id',
        how='inner'
    )

    cleared_df = movie_rating_users_df.explode('movie_genres')

    cleared_df = cleared_df.groupby(['movie_genres', 'year'])['rating'].mean().round(4).reset_index()
    cleared_df = cleared_df.rename(columns={'movie_genres': 'genre',
                                            'rating': 'average_rating'})

    cleared_df = cleared_df.sort_values(by=['genre', 'year'])

    cleared_df.to_excel(f'{destination_folder}/{report_name}', index=False)

    print('Report generated')
