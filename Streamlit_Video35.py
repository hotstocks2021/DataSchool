import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      My top 25 pandas tricks
Video 35 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=RlIiVeig3hc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=35

\n:red[Note:] 

## Pandas Doc :red[String] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html

## Pandas Doc :red[Datetime Properties] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html#datetimelike-properties

## Pandas Doc :red[Options and Setting] :
- :red[get_option] 
\n   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_option.html
- :red[set_option]
\n   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.set_option.html
- :red[reset_option]
\n   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.reset_option.html
- :red[describe_option]
\n   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.describe_option.html

## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]
"""
)

st.markdown("""
## :red[11. Create a DataFrame from the clipboard]
"""
)

st.markdown("""
- control C (copy) something and run the below two line. The result will display the data that you copied.
"""
)
st.write(":red[df] = pd.:red[read_clipboard()]")
df = pd.read_clipboard()
st.write("print(:red[df])")
st.table(df)

st.markdown("""
## :red[13. Filter a DataFrame by multiple categories]
"""
)

st.write(":green[**movies = pd.read_csv('http://bit.ly/imdbratings')**]")
movies = pd.read_csv("http://bit.ly/imdbratings")
st.write("print(movies.:red[head()])")
st.table(movies.head())

st.write("- get :red['genre'] = :red[Action] :red[|] :red[Drama] :red[|] :red[Western]")
st.write(":red[movies][ :red[(movies.genre == 'Action') **|** (movies.genre == 'Drama') **|** (movies.genre == 'Western') ]].head()")
st.table(movies[(movies.genre == 'Action') | (movies.genre == 'Drama') | (movies.genre == 'Western')].head())

st.write("- get :red['genre'] = :red[Action] :red[|] :red[Drama] :red[|] :red[Western] by using :red[loc]")
st.write("movies.:red[loc][:red[(movies.genre == 'Action') | (movies.genre == 'Drama') | (movies.genre == 'Western'), : ]].head())")
st.table(movies.loc[(movies.genre == 'Action') | (movies.genre == 'Drama') | (movies.genre == 'Western'), : ].head())

st.write("- get :red['genre'] = :red[Action] :red[|] :red[Drama] :red[|] :red[Western] by using :red[isin()]")
st.write("movies[movies.genre.:red[isin(['Action', 'Drama', 'Western'])].head()")
st.table(movies[movies.genre.isin(['Action', 'Drama', 'Western'])].head())

st.write("- get :red['genre'] = :red[Action] :red[|] :red[Drama] :red[|] :red[Western] by using :red[loc] and :red[isin()]")
st.write("movies.:red[loc][movies.genre.:red[isin(['Action', 'Drama', 'Western'])]].head()")
st.table(movies.loc[movies.genre.isin(['Action', 'Drama', 'Western']), : ].head())

st.write("- get :red['genre'] not = :red[Action] :red[|] :red[Drama] :red[|] :red[Western] by using :red[isin()]")
st.write("movies[:red[**~**]movies.genre.:red[isin(['Action', 'Drama', 'Western'])].head()")
st.table(movies[~movies.genre.isin(['Action', 'Drama', 'Western'])].head())

st.write("- get :red['genre'] not = :red[Action] :red[|] :red[Drama] :red[|] :red[Western] by using :red[loc] and :red[isin()]")
st.write("movies.:red[loc][:red[**~**]movies.genre.:red[isin(['Action', 'Drama', 'Western'])]].head()")
st.table(movies.loc[~movies.genre.isin(['Action', 'Drama', 'Western']), : ].head())

st.markdown("""
## :red[18. Aggregate by multiple functions]
"""
)

st.write(":green[**orders = pd.read_csv('http://bit.ly/chiporders', sep='\t')**]")
orders = pd.read_csv('http://bit.ly/chiporders', sep='\t')

st.write("print(orders.:red[head()])")
st.table(orders.head(10))
st.write("print(orders.dtypes)")
st.write(orders.dtypes)

st.write("- :red[convert] the :red['item_price'] from object to :red[float]")
orders['item_price'] = orders.item_price.str.replace("$", "").astype(float)
st.write("print(orders.:red[head()])")
st.table(orders.head(10))
st.write("print(orders.dtypes)")
st.write(orders.dtypes)

st.write("- get the :red[sum] of :red[item_price] for :red[order_id = 1]")
st.write(orders[orders.order_id == 1].item_price.sum())

st.write("- groupby 'order_id' and get the sum and count of 'item_price'")
st.write("orders.:red[groupby]('order_id').item_price.:red[agg(['sum', 'count'])].head()")
st.table(orders.groupby('order_id').item_price.agg(['sum', 'count']).head())

st.markdown("""
## :red[19. Combine the output of an aggregation with a DataFrame]
"""
)
st.write("print(orders.:red[head()])")
st.table(orders.head(10))

st.write("- get the total price of each order")
st.write("orders.:red[groupby](:red['order_id']).:red[item_price].:red[sum()].head()")
st.table(orders.groupby('order_id').item_price.sum().head())

st.write("- get the order total and append it to the DataFrame")
st.write(":red[**Note**:] :red[transform()] which performs the same calculation as the previous example but returns output data that is the same shape as the input data")
st.write(":red[orders['total_price']] = orders.groupby('order_id').item_price.:red[transform]('sum')")
orders['total_price'] = orders.groupby('order_id').item_price.transform('sum')
st.write("print(orders.:red[head()])")
st.table(orders.head(10))

st.write("- get the % total of the order per item and append it to the DataFrame")
st.write("orders[:red['percent_of_total']] = :red[orders.item_price] / :red[orders.total_price]")
orders['percent_of_total'] = orders.item_price / orders.total_price
st.write("print(orders.:red[head()])")
st.table(orders.head(10))

st.markdown("""
## :red[22. Create a pivot table]
"""
)
st.write(":green[**:red[titanic] = pd.read_csv('http://bit.ly/kaggletrain)**]")
titanic = pd.read_csv('http://bit.ly/kaggletrain')
st.write("print(titanic.:red[head()])")
st.table(titanic.head())

st.write("titanic.:red[pivot_table](:red[index='Sex'], :red[columns='Pclass'], :red[values='Survived'], :red[aggfunc='mean'])")
st.table(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean'))

st.write("titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean', :red[margins=True])")
st.table(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean', margins=True))

st.write("titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', :red[aggfunc='count'], margins=True)")
st.table(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='count', margins=True))

st.markdown("""
## :red[23. Convert continuous data into categorical data]
"""
)
st.write("print(titanic.:red[Age.head(10)])")
st.table(titanic.Age.head(10))
st.write(":red[pd.cut](:red[titanic.Age], :red[bins=[0, 10, 25, 60, 99]], :red[labels=['child', 'young adult', 'adult', 'senior']]).head(10)")
st.table(pd.cut(titanic.Age, bins=[0, 10, 25, 60, 99], labels=['child', 'young adult', 'adult', 'senior']).head(10))

st.markdown("""
## :red[25. Style a DataFrame]
"""
)
st.write(":green[**pd.read_csv('http://bit.ly/smallstocks', parse_dates=['Date']**]")
stocks = pd.read_csv('http://bit.ly/smallstocks', parse_dates=['Date'])
st.table(stocks.head())

format_dict = {'Date':'{:%m/%d/%y}', 'Close':'${:.2f}', 'Volume':'{:,}'}
st.table(stocks.style.format(format_dict))

st.table(stocks.style.format(format_dict).hide_index().highlight_min('Close', color='red').highlight_max('Close', color='lightgreen'))

st.table(stocks.style.format(format_dict).hide_index().background_gradient(subset='Volume', cmap='Blues'))

st.table(stocks.style.format(format_dict).hide_index().bar('Volume', color='lightblue', align='zero').set_caption('Stock Prices from October 2016'))
