import pandas as pd

#  load data
def load_data():
    return pd.read_csv('data/october-2024.csv')

# store into dataframe
df = load_data()

# lowercase all column names
df.columns = df.columns.str.lower()

# function for date formatting
def date_formatting(column):
    abbrevDate = pd.to_datetime(column)
    formattedDate = abbrevDate.dt.strftime('%b %d, %Y')
    return formattedDate

# check date function
df['formatted_date'] = date_formatting(df['date'])

# print(df)