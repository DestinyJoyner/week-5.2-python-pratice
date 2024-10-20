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

# reformat the category column to 
def category_formatting(column):
    joinedStr = column.str.lower().str.replace(" ","-")
    return joinedStr

df["category"] = category_formatting(df["category"])

# print(df['category'])
# ANALYSIS:

# total spending for month
def monthly_expenses():
    return f'Total expenses for Jan: ${df['amount'].sum()}'

# print(monthly_expenses())

# compare to $5000 budget
def budget_status():
    monthly_expenses = df['amount'].sum()
    budget_difference = 5000 - abs(monthly_expenses)
    
    return f'Your current monthly budget is: ${budget_difference.round(2)}'

# print(budget_status())

# group and sum spending by category
def group_sum_spending_by_category ():
    # group by category
    grouped_by_category = df.groupby('category')
    sum_by_category = grouped_by_category['amount'].sum()
    # print(sum_by_category)
    return sum_by_category
    
# print(group_sum_spending_by_category())

# top 5 individual expenses
def top_5_expenses() :
    df['amount'] = abs(df['amount'])
    sorted_expenses = df.sort_values('amount', ascending=False).head(5)
    return sorted_expenses[['amount', 'description','category']]

# print(top_5_expenses())