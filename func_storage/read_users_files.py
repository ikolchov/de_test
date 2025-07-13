import pandas as pd

"""

USERS FILE DESCRIPTION
================================================================================

User information is in the file "users.dat" and is in the following
format:

UserID::Gender::Age::Occupation::Zip-code

All demographic information is provided voluntarily by the users and is
not checked for accuracy.  Only users who have provided some demographic
information are included in this data set.

- Gender is denoted by a "M" for male and "F" for female
- Age is chosen from the following ranges:

	*  1:  "Under 18"
	* 18:  "18-24"
	* 25:  "25-34"
	* 35:  "35-44"
	* 45:  "45-49"
	* 50:  "50-55"
	* 56:  "56+"

- Occupation is chosen from the following choices:

	*  0:  "other" or not specified
	*  1:  "academic/educator"
	*  2:  "artist"
	*  3:  "clerical/admin"
	*  4:  "college/grad student"
	*  5:  "customer service"
	*  6:  "doctor/health care"
	*  7:  "executive/managerial"
	*  8:  "farmer"
	*  9:  "homemaker"
	* 10:  "K-12 student"
	* 11:  "lawyer"
	* 12:  "programmer"
	* 13:  "retired"
	* 14:  "sales/marketing"
	* 15:  "scientist"
	* 16:  "self-employed"
	* 17:  "technician/engineer"
	* 18:  "tradesman/craftsman"
	* 19:  "unemployed"
	* 20:  "writer"
"""


def read_users_file(file, age_start=0, age_end=999, sep='::'):
    # could be more
    chunk_size = 10_000
    chunks = []
    column_names = [
        'user_id',
        'gender',
        'age',
        'occupation',
        'zip_code',
    ]
    dtypes = {
        'user_id': 'str',
        'gender': 'str',
        'age': 'int',
        'occupation': 'str',
        'zip_code': 'str'
    }

    for chunk in pd.read_csv(file, sep=sep, chunksize=chunk_size,
                             engine='python',
                             dtype=dtypes, names=column_names,
                             header=None):
        # we only need the user_id and age
        chunk = chunk[['user_id', 'age']]
        chunk = chunk.loc[(chunk['age'] >= age_start)
                          & (chunk['age'] < age_end)]
        chunks.append(chunk)

    df = pd.concat(chunks)
    return df
