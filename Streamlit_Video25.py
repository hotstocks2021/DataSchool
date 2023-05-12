import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      How do I work with dates and times in pandas?
Note: 


Video 25 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=yCgJGsg0Xa4&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=25
## Pandas Doc :red[String] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html

## Pandas Doc :red[Datetime Properties] handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html#datetimelike-properties

## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**ufo = pd.read_csv("http://bit.ly/uforeports")**]
\nprint(ufo.:red[head()])
"""
)
ufo = pd.read_csv("http://bit.ly/uforeports")
st.table(ufo.head())
st.write("print(ufo.:red[shape])")
st.write(str(ufo.shape))
st.write("print(ufo.:red[dtypes])")
st.table(ufo.dtypes)

st.markdown("""
## Example 2:
- convert the time column to pandas time
\n:green[:red[ufo["Time"]] = :red[pd.to_datetime(ufo.Time)]]
\nprint(ufo.head())
""")
ufo["Time"] = pd.to_datetime(ufo.Time)
st.table(ufo.head())
st.write("print(ufo.:red[dtypes])")
st.table(ufo.dtypes)

st.markdown("""
## Example 3:
- get the hour out of the pandas time series
\nprint(:red[ufo.Time.dt.hour.head()])
""")
st.table(ufo.Time.dt.hour.head())

st.markdown("""
## Example 4:
- get the dayofweek out of the pandas time series
\nprint(:red[ufo.Time.dt.dayofweek.head()])
""")
st.table(ufo.Time.dt.dayofweek.head())

st.markdown("""
## Example 5:
- get the dayofyear out of the pandas time series
\nprint(:red[ufo.Time.dt.dayofyear.head()])
""")
st.table(ufo.Time.dt.dayofyear.head())

st.markdown("""
## Example 6:
- convert a manually entered date to a :red[timestamp]
\nprint(:red[ts])
""")
ts = pd.to_datetime("1/1/1999")
st.write(ts)

st.markdown("""
## Example 7:
- use a :red[timestamp] to compare with a dataset
\nprint(:red[ufo.loc[ufo.Time >= ts, :].head()])
""")
st.table(ufo.loc[ufo.Time >= ts, :].head())

st.markdown("""
## Example 8:
- find the :red[latest] in a time series
\nprint(ufo.Time.:red[max()])
""")
st.write(ufo.Time.max())

st.markdown("""
## Example 9:
- find the max and min methods to do math in a time series
\nprint(ufo.:red[Time.max() - ]ufo.Time.:red[min()])
""")
st.write(ufo.Time.max() - ufo.Time.min())

st.markdown("""
## Example 10:
- find out how many report sightings in a year
\n:green[:red[ufo["Year"]] = ufo.Time.dt.year]
\nprint(ufo.:red[head()])
""")
ufo["Year"] = ufo.Time.dt.year
st.table(ufo.head())

st.write(":green[:red[year_data] = :red[ufo.Year.value_counts().sort_index()]]")
year_data = ufo.Year.value_counts().sort_index()
st.write("print(:red[year_data])")
st.table(year_data)

import matplotlib.pyplot as plt
import numpy as np
st.markdown("""
## Example 11:
- plot the report sightings in a year
\n:green[:red[xpoints] = :red[np.array(year_data.index.values)]]
\n:green[:red[ypoints] = :red[np.array(year_data.values)]]
""")
xpoints = np.array(year_data.index.values)
ypoints = np.array(year_data.values)
# plt.plot(xpoints, ypoints)
# plt.show()

st.line_chart(xpoints)
st.line_chart(ypoints)

