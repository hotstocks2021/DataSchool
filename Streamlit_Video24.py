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
- 


Video 24 of Data analysis in Python with Pandas by Data School
\n https://www.youtube.com/watch?v=0s_1IsROgDc&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=24
## Pandas Doc String handling: 
https://pandas.pydata.org/pandas-docs/version/0.22/api.html
## Set the display options
:red[pd.set_option('expand_frame_repr', False)]
\n:red[pd.set_option('display.max_colwidth', None)]

## Example 1: 
\n:green[**train = pd.read_csv("http://bit.ly/kaggletrain"")**]
\nprint(train.:red[head()])
"""
)
train = pd.read_csv("http://bit.ly/kaggletrain")
st.table(train.head())
st.write("print(ufo.:red[shape])")
st.write(str(train.shape))

st.markdown("""
## Example 2:
- add a column to a Dataset using the existing data 
\n:green[train:red[["Sex_male"]] = train.:red[Sex.map({"female":0, "male":1}])]
""")
train["Sex_male"] = train.Sex.map({"female":0, "male":1})
st.table(train.head())

st.markdown("""
## Example 3:
- using the get_dummies method to add column using existing data
\n:green[**train = pd.read_csv("http://bit.ly/kaggletrain"")**]
\n:green[train:red[["Sex_male"]] = :red[pd.get_dummies(train.Sex, prefix="Sex").iloc[:,1:]]]
""")
train = pd.read_csv("http://bit.ly/kaggletrain")
train["Sex_male"] = pd.get_dummies(train.Sex, prefix="Sex").iloc[:,1:]
st.write("print(train.:red[head()])")
st.table(train.head())

st.markdown("""
## Example 4:
- using the get_dummies method to add columns using existing data
\n:green[**train = pd.read_csv("http://bit.ly/kaggletrain"")**]
\n:green[train:red[["Embarked_C"]] = :red[pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,:1]]]
\n:green[train:red[["Embarked_Q"]] = :red[pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,1:2]]]
\n:green[train:red[["Embarked_S"]] = :red[pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,2:]]]
""")
train = pd.read_csv("http://bit.ly/kaggletrain")
train["Embarked_C"] = pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,:1]
train["Embarked_Q"] = pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,1:2]
train["Embarked_S"] = pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,2:]
st.write("print(train.:red[head()])")
st.table(train.head())

st.markdown("""
## Example 5:
- an easier way of doing example 4
\n:green[**train = pd.read_csv("http://bit.ly/kaggletrain"")**]
\n:green[:red[embarked_dummies] = :red[pd.get_dummies(train.Embarked, prefix="Embarked").iloc[ : , : ]]]
\n:green[:red[train] = :red[pd.concat([train, embarked_dummies], axis=1)]]
""")
train = pd.read_csv("http://bit.ly/kaggletrain")
embarked_dummies = pd.get_dummies(train.Embarked, prefix="Embarked").iloc[:,:]
train = pd.concat([train, embarked_dummies], axis=1)
st.write("print(train.:red[head()])")
st.table(train.head())

st.markdown("""
## Example 6:
- the easiest way of doing example 4
\n:green[**train = pd.read_csv("http://bit.ly/kaggletrain"")**]
\n:green[:red[train] = :red[pd.get_dummies(train, columns=["Sex", "Embarked"]]]
""")
train = pd.read_csv("http://bit.ly/kaggletrain")
train = pd.get_dummies(train, columns=["Sex", "Embarked"])
st.write("print(train.:red[head()])")
st.table(train.head())
