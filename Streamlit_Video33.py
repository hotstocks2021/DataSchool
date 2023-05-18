import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      4 new time-saving tricks in pandas
Video 33 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=-NbY7E9hKxk&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=33

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
## :red[1. Create a datetime column from a DataFrame]
"""
)


st.markdown("""
## Example 1: 
- create an example DataFrame
"""
)
st.write(":red[df] = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],  columns=[\"month\", \"day\", \"year\", \"hour\"])")
df = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],  columns=['month', 'day', 'year', 'hour'])
st.write("df.:red[head()]")
st.table(df.head())
st.write("df.:red[shape]")
st.write(df.shape)

st.markdown("""
## Example 2: 
- create a datetime column from the entire DataFrame
"""
)
st.write(":red[df] = pd.:red[to_datetime(df)]")
df = pd.to_datetime(df)
st.write("df.:red[head()]")
st.table(df.head())
st.write("df.:red[shape]")
st.write(df.shape)
st.write(":red[Note:] since the column names are month, day, year, and hour, Pandas knows they are date and time.")

st.markdown("""
## Example 3:
- create a datetime column from the entire DataFrame
"""
)
st.write(":red[df] = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],  columns=[\"month\", \"day\", \"year\", \"hour\"])")
df = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],  columns=['month', 'day', 'year', 'hour'])
st.write(":red[df] = pd.:red[to_datetime](df[\"month\", \"day\", \"year\"])")
df = pd.to_datetime(df[['month', 'day', 'year']])
st.write("df.:red[head()]")
st.table(df.head())

st.markdown("""
## Example 4:
- overwrite the index
"""
)
st.write(":red[df] = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],  columns=[\"month\", \"day\", \"year\", \"hour\"])")
df = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],  columns=['month', 'day', 'year', 'hour'])
st.write("df.:red[index] = pd.:red[to_datetime](df:red[ [ [ \"month\", \"day\", \"year\" ] ] ]")
df.index = pd.to_datetime(df[['month', 'day', 'year']])
st.write("df.:red[head()]")
st.table(df.head())

st.markdown("""
- [More information](http://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html)
- [Video: How do I work with dates and times in pandas?](https://www.youtube.com/watch?v=yCgJGsg0Xa4&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=26)
""")

st.markdown("""
## :red[2. Create a category column during file reading]
"""
)

st.markdown("""
## Example 5:
- read the drinks dataset into a DataFrame and convert the 'continent' datatype to category
"""
)
drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'continent':'category'})
st.write(":red[drinks] = pd.read_csv(\"http://bit.ly/drinksbycountry\", :red[dtype={\"continent\":\"category\"}])")
st.write("print(drinks.:red[head()])")
st.table(drinks.head())
st.write("drinks.:red[dtypes]")
st.write(drinks.dtypes)

st.markdown("""
- [More information](http://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html)
- [Video: How do I make my pandas DataFrame smaller and faster?](https://www.youtube.com/watch?v=wDYDYGyN_cw&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=22)
""")

st.markdown("""
## :red[3. Convert the data type of multiple columns at once]
"""
)

st.markdown("""
## Example 6:
- read the drinks dataset into a DataFrame
"""
)
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
st.write(":red[drinks] = pd.read_csv(\"http://bit.ly/drinksbycountry")
st.write("drinks.:red[dtypes]")
st.write(drinks.dtypes)

drinks = drinks.astype({'beer_servings':'float', 'spirit_servings':'float'})
st.write(":red[drinks] = drinks.astype({\"beer_servings\":\"float\", \"spirit_servings\":\"float\"}")
st.write("drinks.:red[dtypes]")
st.write(drinks.dtypes)

st.markdown("""
- [More information](http://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html)
- [Video: How do I change the data type of a pandas Series?](https://www.youtube.com/watch?v=V0AWyzVMf54&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=14)
""")

st.markdown("""
## :red[4. Apply multiple aggregations on a Series or DataFrame]
"""
)

st.markdown("""
## Example 7:
- example of a single aggregation function after a groupby
"""
)
st.write("drinks.:red[groupby(\"continent\")].beer_servings.:red[mean()]")
st.write(drinks.groupby('continent').beer_servings.mean())

st.markdown("""
## Example 8:
- multiple aggregation functions can be applied simultaneously
"""
)
st.write("drinks.:red[groupby(\"continent\")].beer_servings.:red[agg([\"mean\", \"min\", \"max\"])]")
st.write(drinks.groupby('continent').beer_servings.agg(['mean', 'min', 'max']))

st.markdown("""
## Example 9:
- apply the same aggregations to a Series
"""
)
st.write("drinks.beer_servings.:red[agg([\"mean\", \"min\", \"max\"])]")
st.write(drinks.beer_servings.agg(['mean', 'min', 'max']))

st.markdown("""
## Example 10:
- DataFrame describe method provides similar functionality but is less flexible
"""
)
st.write("drinks.:red[describe()]")
st.write(drinks.describe())

st.markdown("""
- [More information](http://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html)
- [Video: When should I use a "groupby" in pandas?](https://www.youtube.com/watch?v=qy0fDqoMJx8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=15)
""")

import base64
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

show_pdf(".\data\Pandas_Cheat_Sheet.pdf")
