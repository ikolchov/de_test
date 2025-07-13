from create_report.generate_excel_report import generate_excel_report
from func_storage.get_data_from_zip import get_data_from_zip
from src.config import ProductionConfig

current_config = ProductionConfig

if __name__ == '__main__':
    movies_df, users_df, ratings_df = get_data_from_zip(location=current_config.RAW_DATA_LOCATION,
                                                        movie_start_year=current_config.MOVIE_START_YEAR,
                                                        movie_end_year=current_config.MOVIE_END_YEAR,
                                                        age_start=current_config.USER_MIN_YEAR,
                                                        age_end=current_config.USER_MAX_YEAR,
                                                        )
    generate_excel_report(movies_df=movies_df,
                          users_df=users_df,
                          ratings_df=ratings_df,
                          destination_folder=current_config.REPORT_LOCATION,
                          report_name=current_config.REPORT_FILE_NAME,
                          )
