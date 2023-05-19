# Video 34
# https://www.youtube.com/watch?v=te5JrSCW-LY&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=34
# Date: 2023-05-18
# Title:
#       5 new changes in pandas you need to know about
# Note:


# Tanium@Mar@2023

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

print("1. ix has been deprecated")

print("\nExample 1:")
# read the drinks dataset into a DataFrame
drinks = pd.read_csv('http://bit.ly/drinksbycountry', index_col='country')
print(drinks.head())
print()
print(drinks.shape)

print()
print("drinks.ix['Angola', 1]")
print("AttributeError: 'DataFrame' object has no attribute 'ix'")

print()
# loc accesses by label
print(drinks.loc['Angola', 'spirit_servings'])
# alternative: use loc
print(drinks.loc['Angola', drinks.columns[1]])
# alternative: use loc
print(drinks.loc[drinks.index[4], 'spirit_servings'])

print()
# iloc accesses by position
print(drinks.iloc[4, 1])
# alternative: use iloc
print(drinks.iloc[drinks.index.get_loc('Angola'), 1])
# alternative: use iloc
print(drinks.iloc[4, drinks.columns.get_loc('spirit_servings')])

print("\n2. Aliases have been added for isnull and notnull")
print("\nExample 2:")
# read the UFO dataset into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head(20))

print()
# check which values are missing
print(ufo.isnull().head())

print()
# check which values are not missing
print(ufo.notnull().head())

print()
# drop rows with missing values
print(ufo.dropna().head())

print()
# fill in missing values
print(ufo.fillna(value='UNKNOWN').head())

print()
# new alias for isnull
print(ufo.isna().head())

print()
# new alias for notnull
print(ufo.notna().head())

print("\n3. drop now accepts 'index' and 'columns' keywords")
print("\nExample 3:")
# read the UFO dataset into a DataFrame
ufo = pd.read_csv('http://bit.ly/uforeports')
print(ufo.head())

print()
# old way to drop rows: specify labels and axis
print(ufo.drop([0, 1], axis=0).head())
print()
print(ufo.drop([0, 1], axis='index').head())

print()
# new way to drop rows: specify index
print(ufo.drop(index=[0, 1]).head())

print()
# old way to drop columns: specify labels and axis
print(ufo.drop(['City', 'State'], axis=1).head())
print()
print(ufo.drop(['City', 'State'], axis='columns').head())

print()
# new way to drop columns: specify columns
print(ufo.drop(columns=['City', 'State']).head())

print("\n4. rename and reindex now accept 'axis' keyword")
print("\nExample 4:")
# old way to rename columns: specify columns
print(ufo.rename(columns={'City':'CITY', 'State':'STATE'}).head())

print()
# new way to rename columns: specify mapper and axis
print(ufo.rename({'City':'CITY', 'State':'STATE'}, axis='columns').head())

print()
# note: mapper can be a function
print(ufo.rename(str.upper, axis='columns').head())

print("\n5. Ordered categories must be specified independent of the data")
print("\nExample 5:")
# create a small DataFrame
df = pd.DataFrame({'ID':[100, 101, 102, 103], 'quality':['good', 'very good', 'good', 'excellent']})
print(df)

print()
# old way to create an ordered category (deprecated)
print("df.quality.astype('category', categories=['good', 'very good', 'excellent'], ordered=True)")
print("TypeError: NDFrame.astype() got an unexpected keyword argument 'categories'")

print()
# new way to create an ordered category
from pandas.api.types import CategoricalDtype
quality_cat = CategoricalDtype(['good', 'very good', 'excellent'], ordered=True)
df['quality'] = df.quality.astype(quality_cat)
print(df.quality)
