# Video 35
# https://www.youtube.com/watch?v=RlIiVeig3hc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=35
# Date: 2023-05-19
# Title:
#       My top 25 pandas tricks
# Note:


import os
import sys

try:
    import pandas as pd
except ImportError as e:
    os.system("pip install pandas")
    import pandas as pd

# Set the display options
pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_colwidth', None)

print(pd.__version__)
print()

print("11. Create a DataFrame from the clipboard")
print("\nExample 11:")
# control C (copy) something and run the below two line. The result will display the data that you copied.
# df = pd.read_clipboard()
# print(df)


print("13. Filter a DataFrame by multiple categories")
print("\nExample 13:")
movies = pd.read_csv("http://bit.ly/imdbratings")
print(movies.head())
print()
print(movies[(movies.genre == 'Action') | (movies.genre == 'Drama') | (movies.genre == 'Western')].head())
print()
print(movies.loc[(movies.genre == 'Action') | (movies.genre == 'Drama') | (movies.genre == 'Western'), : ].head())
print()
print(movies[movies.genre.isin(['Action', 'Drama', 'Western'])].head())
print()
print(movies.loc[movies.genre.isin(['Action', 'Drama', 'Western']), : ].head())

print()
print(movies[~movies.genre.isin(['Action', 'Drama', 'Western'])].head())
print()
print(movies.loc[~movies.genre.isin(['Action', 'Drama', 'Western']), : ].head())

print("18. Aggregate by multiple functions")
print("\nExample 18:")
orders = pd.read_csv('http://bit.ly/chiporders', sep='\t')
print(orders.head(10))
print()
print(orders.dtypes)

# convert object to float data type
orders['item_price'] = orders.item_price.str.replace("$", "").astype(float)
print()
print(orders.head(10))

print()
# get the sum of item_price for order_id = 1
print(orders[orders.order_id == 1].item_price.sum())

print()
# groupby 'order_id' and get the sum and count of 'item_price'
print(orders.groupby('order_id').item_price.agg(['sum', 'count']))

print("19. Combine the output of an aggregation with a DataFrame")
print("\nExample 19:")
print(orders.head(10))

print()
# order total
print(orders.groupby('order_id').item_price.sum().head())

print()
# order total and append it to the DataFrame
orders['total_price'] = orders.groupby('order_id').item_price.transform('sum')
print(orders.head(10))

print()
# get the % total of the order per item and append it to the DataFrame
orders['percent_of_total'] = orders.item_price / orders.total_price
print(orders.head(10))

print("22. Create a pivot table")
print("\nExample 22:")
titanic = pd.read_csv('http://bit.ly/kaggletrain')
print(titanic.head(10))
print(titanic.pivot_table(index='Sex', columns=['Pclass'], values=['Survived'], aggfunc='mean'))
print()
print(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean', margins=True))
print()
print(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='count', margins=True))

print("23. Convert continuous data into categorical data")
print("\nExample 23:")
print(titanic.Age.head(10))
print()
print(pd.cut(titanic.Age, bins=[0, 10, 25, 60, 99], labels=['child', 'young adult', 'adult', 'senior']).head(10))

print("25. Style a DataFrame")
print("\nExample 25:")
stocks = pd.read_csv('http://bit.ly/smallstocks', parse_dates=['Date'])
print(stocks)

print()
format_dict = {'Date':'{:%m/%d/%y}', 'Close':'${:.2f}', 'Volume':'{:,}'}
print(stocks.style.format(format_dict))

print(stocks.style.format(format_dict).hide_index().highlight_min('Close', color='red').highlight_max('Close', color='lightgreen'))
