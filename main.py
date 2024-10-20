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
    sum_by_category= grouped_by_category['amount'].sum()
    
    # Convert the Series to a DataFrame and rename the column
    table_result = sum_by_category.reset_index() 
    table_result.columns=['category', 'total_amount']
    return table_result
    
# print(group_sum_spending_by_category())

# top 5 individual expenses
def top_5_expenses() :
    df['amount'] = abs(df['amount'])
    sorted_expenses = df.sort_values('amount', ascending=False).head(5)
    return sorted_expenses[['amount', 'description','category']]

# print(top_5_expenses())

# VISUALIZATION - pie chart
import matplotlib.pyplot as plt

def pie_chart_spending_by_category():
    group_by_category = group_sum_spending_by_category()
    result_table = group_by_category.reset_index()
    result_table["percentage"] = abs(result_table['total_amount']) / abs(df['amount'].sum() ) * 100
    # print(result_table)
    # create pie chart
    plt.figure(figsize=(10,6))
    plt.pie(result_table['percentage'], labels=result_table['category'],autopct='%1.1f%%', startangle=90)
    
    #Equal aspect ratio ensures that pie chart is circular
    plt.axis('equal') 
    plt.show()
    return
    
    
print(pie_chart_spending_by_category())