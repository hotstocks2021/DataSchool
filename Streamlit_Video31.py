import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      How do I use the MultiIndex in pandas?
Note: 

Video 31 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=tcRGa2soc-c&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=31
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

## Example 1: 
\n:green[**stocks = pd.read_table('http://bit.ly/smallstocks')**]
"""
)
stocks = pd.read_csv('http://bit.ly/smallstocks')
st.table(stocks)
st.write("print(train.:red[shape])")
st.write(str(stocks.shape))
st.write("print(train.:red[dtypes])")
st.table(stocks.dtypes)
st.write("print(train.:red[index])")
st.write(str(stocks.index))

st.markdown("""
## Example 2:
- group the DataFrame by stock symbols then find the mean
""")
st.write(":green[print(stocks.:red[groupby(\"Symbol\").Close.mean()])]")
st.table(stocks.groupby("Symbol").Close.mean())

st.markdown("""
## Example 3:
- group the DataFrame by stock symbols and date then find the mean
""")
st.write(":green[print(stocks.:red[groupby([\"Symbol\", \"Date\"]).Close.mean()])]")
st.table(stocks.groupby(["Symbol", "Date"]).Close.mean())
ser = stocks.groupby(["Symbol", "Date"]).Close.mean()
st.write(":green[:red[ser] = stocks.:red[groupby([\"Symbol\", \"Date\"]).Close.mean()]]")
st.write("print(:red[type](ser))")
st.write(str(type(ser)))
st.write(":red[Note:] ser is a :red[Series]")
st.write("print(ser.:red[index]))")
st.write(ser.index)
st.write(":red[Note:] ser.index is a :red[MultiIndex] means it is two dimensions")

st.markdown("""
## Example 4:
- multi index Series can be unstacked to a DataFrame
""")
ser = ser.unstack()
st.write(":green[:red[ser] = ser.:red[unstack()]]")
st.write("print(:red[ser])")
st.write(ser)

st.markdown("""
## Example 5:
- example 4 can be done by using the pivot_table() method
""")
st.write(":green[df = stocks.:red[pivot_table(values=\"Close\", columns=\"Date\", index=\"Symbol\")]]")
df = stocks.pivot_table(values="Close", columns="Date", index="Symbol")
st.write("print(:red[df])")
st.write(df)

st.markdown("""
## Example 6:
- create a :red[multi index] DataFrame
""")
st.write("print(:red[stocks])")
st.table(stocks)

st.write(":green[stocks.:red[set_index( [\"Symbol\", \"Date\"] , inplace=True)]]")
stocks.set_index(["Symbol", "Date"], inplace=True)
st.write(":green[stocks.:red[sort_index(inplace=True)]]")
stocks.sort_index(inplace=True)
st.write("print(:red[stocks])")
st.table(stocks)

st.write("print(:red[stocks.index])")
st.write(stocks.index)

st.markdown("""
## Example 7:
- use a tuple on multi index DataFrame
""")
st.write(":green[print(stocks.loc[:red[ (\"AAPL\", \"2016-10-03\")] , :])]")
st.table(stocks.loc[("AAPL", "2016-10-03"), :])

st.markdown("""
## Example 8:
- use a tuple and a list to select multiple indexes on multi index DataFrame
""")
st.write(":green[print(stocks.loc[:red[( [\"AAPL\", \"MSFT\"] , \"2016-10-03\")] , :])]")
st.table(stocks.loc[(["AAPL", "MSFT"], "2016-10-03"), :])
st.write(":red[Note:] multiple stocks for the same date")

st.markdown("""
## Example 9:
- use a tuple and a list to select multiple indexes on multi index DataFrame
""")
st.write(":green[print(stocks.loc[:red[\"AAPL\", (\"2016-10-03\", \"2016-10-05\")], : ])]")
st.table(stocks.loc["AAPL", ("2016-10-03", "2016-10-05"), : ])
st.write(":red[Note:] multiple dates for the same stock")

st.markdown("""
## Example 10:
- use a tuple and a list to select multiple indexes on multi index DataFrame
""")
st.write(":green[print(stocks.loc[:red[slice(None)], (\"2016-10-03\", \"2016-10-05\")], : )]")
st.table(stocks.loc[slice(None), ("2016-10-03", "2016-10-05"), : ])
st.write(":red[Note:] multiple dates for all stocks")

st.markdown("""
## Example 11:
- merge two DataFrames together
""")
st.write(":green[**stocks = pd.read_table('http://bit.ly/smallstocks')**]")
st.write("print(:red[stocks])")
st.table(stocks)

st.write("Creating a new :red[Close] DataFrame:")
st.write(":red[Close] = pd.read_csv('http://bit.ly/smallstocks', :red[usecols=[0, 1, 3], index_col=[\"Symbol\", \"Date\"]])")
Close = pd.read_csv('http://bit.ly/smallstocks', usecols=[0, 1, 3], index_col=["Symbol", "Date"])
st.write("print(:red[Close])")
st.table(Close)

st.write("Creating a new :red[Volume] DataFrame:")
st.write(":red[Volume] = pd.read_csv('http://bit.ly/smallstocks', :red[usecols=[0, 2, 3], index_col=[\"Symbol\", \"Date\"]])")
Volume = pd.read_csv('http://bit.ly/smallstocks', usecols=[0, 2, 3], index_col=["Symbol", "Date"])
st.write("print(:red[Volume])")
st.table(Volume)

st.write(":red[Merging] the two new DataFrames together")
st.write(":red[both] = pd.:red[merge(Close, Volume, left_index=True, right_index=True)]")
both = pd.merge(Close, Volume, left_index=True, right_index=True)
st.write("print(:red[both])")
st.table(both)

st.write(":red[Note:] left_index=True, right_index=True; those are the two indexes required to merge the two DataFrames")

st.markdown("""
## Example 12:
- reset multi indexes DataFrame
""")
st.write("both.:red[reset_index(inplace=True)]")
both.reset_index(inplace=True)
st.write("print(:red[both])")
st.table(both)