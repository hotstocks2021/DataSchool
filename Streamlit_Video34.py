import os
import sys
import streamlit as st
import pandas as pd

st.write("[Home](https://hotstocks2021-dataschool-streamlit-dataschool-home-i8njd0.streamlit.app/)")

# pd.set_option('expand_frame_repr', False)
# pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
##      5 new changes in pandas you need to know about
Video 34 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=te5JrSCW-LY&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=34

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
## :red[1. ix has been deprecated]
"""
)

st.markdown("""
## Example 1: 
- read the drinks dataset into a DataFrame
"""
)
st.write(":red[drinks] = pd.read_csv(\"http://bit.ly/drinksbycountry\", index_col=\"country\")")
drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col='country')
st.write("drinks.:red[head()]")
st.table(drinks.head())
st.write("drinks.:red[shape]")
st.write(drinks.shape)
st.write("- **The goal is to get the data for :red[Angola] and :red[spirit_servings] which is :red[57]**")
st.write("drinks.:red[ix]['Angola', 1]")
st.write("- :red[AttributeError: 'DataFrame' object has no attribute 'ix']")
st.write(":red[Notes:] use :red[loc] or :red[iloc] instead")

st.write("- use :red[loc] to achieve the goal")
st.write("drinks.:red[loc][:red[\"Angola\"], :red[\"spirit_servings\"]]")
st.write(drinks.loc["Angola", "spirit_servings"])
st.write(":green[alternative: use loc]")
st.write("drinks.:red[loc][:red[\"Angola\"], :red[drinks.columns[1]]]")
st.write(drinks.loc['Angola', drinks.columns[1]])
st.write(":green[alternative: use loc]")
st.write("drinks.:red[loc][:red[drinks.index[4]], :red[\"spirit_servings\"]]")
st.write(drinks.loc[drinks.index[4], 'spirit_servings'])

st.write("- use :red[iloc] to achieve the goal")
st.write("drinks.:red[iloc][:red[4], :red[1]]")
st.write(drinks.iloc[4, 1])
st.write(":green[alternative: use iloc]")
st.write("drinks.:red[iloc][:red[drinks.index.get_loc('Angola')], :red[1]]")
st.write(drinks.iloc[drinks.index.get_loc('Angola'), 1])
st.write(":green[alternative: use iloc]")
st.write("drinks.:red[iloc][:red[4], :red[drinks.columns.get_loc(\"spirit_servings\")]]")
st.write(drinks.iloc[4, drinks.columns.get_loc('spirit_servings')])

st.markdown("""
- [More information](http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)
- [Video: How do I select multiple rows and columns from a pandas DataFrame?](https://www.youtube.com/watch?v=xvpNA7bC8cs&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=20)
""")

st.markdown("""
## :red[2. Aliases have been added for isnull and notnull]
"""
)

st.markdown("""
## Example 2:
- read the UFO dataset into a DataFrame
"""
)
st.write(":red[ufo] = pd.read_csv('http://bit.ly/uforeports'")
ufo = pd.read_csv('http://bit.ly/uforeports')
st.write("ufo.:red[head(20)]")
st.table(ufo.head(20))
st.write("ufo.:red[shape]")
st.write(ufo.shape)

st.write("- **check which values are missing by using :red[isnull()]**")
st.write("ufo.:red[isnull()].head()")
st.table(ufo.isnull().head())

st.write("- **check which values are not missing by using :red[notnull()]**")
st.write("ufo.:red[notnull()].head()")
st.table(ufo.notnull().head())

st.write("- **drop rows with missing values**")
st.write("ufo.:red[dropna()].head()")
st.table(ufo.dropna().head())

st.write("- **fill in missing values**")
st.write("ufo.:red[fillna(value='UNKNOWN')].head()")
st.table(ufo.fillna(value='UNKNOWN').head())

st.write("- **new alias for isna which is the same thing as isnull**")
st.write("ufo.:red[isna()].head()")
st.table(ufo.isna().head())

st.write("- **new alias for notna which is the same thing as notnull**")
st.write("ufo.:red[notna()].head()")
st.table(ufo.notna().head())

st.markdown("""
- [More information](http://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html)
- [Video: How do I handle missing values in pandas?](https://www.youtube.com/watch?v=fCMrO_VzeL8&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=17)
""")

st.markdown("""
## :red[3. drop now accepts 'index' and 'columns' keywords]
"""
)

st.markdown("""
## Example 3:
- read the UFO dataset into a DataFrame
"""
)
st.write(":red[ufo] = pd.read_csv('http://bit.ly/uforeports'")
ufo = pd.read_csv('http://bit.ly/uforeports')
st.write("ufo.:red[head(20)]")
st.table(ufo.head(20))
st.write("ufo.:red[shape]")
st.write(ufo.shape)

st.write("- **:red[old way] to :red[drop rows]: specify :red[labels] and :red[axis]**")
st.write("ufo.:red[drop([0, 1], axis=0)].head()")
st.table(ufo.drop([0, 1], axis=0).head())

st.write("- **:red[old way] to :red[drop rows]: specify :red[labels] and :red[axis]**")
st.write("ufo.:red[drop([0, 1], axis=index)].head()")
st.table(ufo.drop([0, 1], axis='index').head())
st.write(":red[Note:] 2nd looks the same as the 1st due to :red['inplace=True'] wasn't used.")

st.write("- **:red[new way] to :red[drop rows]: :red[specify index]**")
st.write("ufo.:red[drop(index=[0, 1])].head()")
st.table(ufo.drop(index=[0, 1]).head())

st.write("- **:red[old way] to :red[drop columns]: specify :red[labels] and :red[axis]**")
st.write("ufo.:red[drop(['City', 'State'], axis=1)].head()")
st.table(ufo.drop(['City', 'State'], axis=1).head())

st.write("- **:red[old way] to :red[drop columns]: specify :red[labels] and :red[axis]**")
st.write("ufo.:red[drop(['City', 'State'] axis=columns)].head()")
st.table(ufo.drop(['City', 'State'], axis='columns').head())

st.write("- **:red[new way] to :red[drop columns]: :red[specify columns]**")
st.write("ufo.:red[columns=['City', 'State']].head()")
st.table(ufo.drop(columns=['City', 'State']).head())

st.markdown("""
- [More information](http://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html)
- [Video: How do I remove columns from a pandas DataFrame?](https://www.youtube.com/watch?v=gnUKkS964WQ&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=6)
""")

st.markdown("""
## :red[4. rename and reindex now accept "axis" keyword]
"""
)

st.markdown("""
## Example 4:
"""
)

st.write("- **:red[old way] to :red[rename columns]: specify :red[columns]**")
st.write("ufo.:red[rename](:red[columns={'City':'CITY', 'State':'STATE'}]).head()")
st.table(ufo.rename(columns={'City':'CITY', 'State':'STATE'}).head())

st.write("- **:red[new way] to :red[rename columns]: specify :red[mapper and axis]**")
st.write("ufo.:red[rename](:red[{'City':'CITY', 'State':'STATE'}], :red[axis='columns']).head()")
st.table(ufo.rename({'City':'CITY', 'State':'STATE'}, axis='columns').head())

st.write("- **:red[note]: :red[mapper] can be a function**")
st.write("ufo.:red[rename(str.upper, axis='columns')].head()")
st.table(ufo.rename(str.upper, axis='columns').head())

st.write(":red[Note]: :red[mapper] is the syntax to rename something")
st.markdown("""
- [More information](http://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html)
- [Video: How do I rename columns in a pandas DataFrame?](https://www.youtube.com/watch?v=0uBirYFhizE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=5)
""")

st.markdown("""
## :red[5. Ordered categories must be specified independent of the data]
"""
)

st.markdown("""
## Example 5:
"""
)

st.write("- **create a small DataFrame**")
df = pd.DataFrame({'ID':[100, 101, 102, 103], 'quality':['good', 'very good', 'good', 'excellent']})
st.write(":red[df] = pd.DataFrame({'ID':[100, 101, 102, 103], 'quality':['good', 'very good', 'good', 'excellent']})")
st.table(df)

st.write("- **:red[old way] to create an :red[ordered category (deprecated)]**")
st.write("df.quality.astype('category', categories=['good', 'very good', 'excellent'], ordered=True)")
st.write("- :red[TypeError: NDFrame.astype() got an unexpected keyword argument 'categories']")

st.write("- **:red[new way] to create an ordered category**")
st.write(":green[from pandas.api.types import CategoricalDtype]")
from pandas.api.types import CategoricalDtype
st.write(":green[:red[quality_cat] = :red[CategoricalDtype(['good', 'very good', 'excellent']], :red[ordered=True)]]")
quality_cat = CategoricalDtype(['good', 'very good', 'excellent'], ordered=True)
st.write(":green[:red[df['quality']] = :red[df.quality.astype(quality_cat)]]")
df['quality'] = df.quality.astype(quality_cat)
st.write(":green[df.:red[quality]]")
st.table(df.quality)

st.write(":red[Note]: :red[category] is a string data type in Columns. It can make the :red[DataFrame smaller] and can make :red[operation faster]")
st.markdown("""
- [More information](http://pandas.pydata.org/pandas-docs/stable/whatsnew/index.html)
- [Video: How do I make my pandas DataFrame smaller and faster?](https://www.youtube.com/watch?v=wDYDYGyN_cw&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=22)
""")