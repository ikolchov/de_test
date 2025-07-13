# de_test

This project is for creating a report from a `.zip` file.

---

## How to run

1. Run:

   ```bash
   pip install -r requirements.txt
   ```
   
## Project Structure:
```
├── create_report
│   └── generate_excel_report.py
├── data
│   └── ml-1m.zip
├── func_storage
│   ├── get_data_from_zip.py
│   ├── read_movies_files.py
│   ├── read_rating_files.py
│   └── read_users_files.py
├── main.py
├── README.md
├── requirements.txt
├── res
│   └── average_rating_report.xlsx
└── src
    └── config.py
```

## How to configure

Adjust the settings in `src/config.py` if you need to change file locations or filter criteria:

- By default, the script expects the `.zip` file here: `./data/ml-1m.zip`
- The report will be created here: `./res/`
- Default prefilter conditions:

  - `MOVIE_START_YEAR = 1990`  
    *(inclusive; all movies released from 1990 onward)*
  - `MOVIE_END_YEAR = 9999`  
    *(upper bound)*
  - `USER_MIN_AGE = 18`  
    *(users aged 18 and older)*
  - `USER_MAX_AGE = 50`  
    *(upper age limit, exclusive)*