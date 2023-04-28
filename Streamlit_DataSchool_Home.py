import os
import sys
import streamlit as st
import pandas as pd

pd.set_option('expand_frame_repr',False)
pd.set_option('display.max_colwidth', None)
# st.set_page_config(layout="wide")
st.markdown("""
## Data analysis in Python with pandas - Data School 
\n https://www.youtube.com/watch?v=yzIMircGU5I&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y

Video 2: 
- How do I read a :red[tabular data file] into pandas?
\nhttps://hotstocks2021-dataschool-streamlit-video2-lbi26f.streamlit.app/
\n
Video 3: 
- How do I select a :red[Pandas Series] from a DataFrame?
\nhttps://hotstocks2021-dataschool-streamlit-video3-8efh30.streamlit.app/
\n
Video 4: 
- Pandas :red[Attribute and Method]
\nhttps://hotstocks2021-dataschool-streamlit-video4-gcszbr.streamlit.app/
\n
Video 5: 
- How do I :red[rename columns] in a pandas DataFrame?
\nhttps://hotstocks2021-dataschool-streamlit-video5-ozwrhd.streamlit.app/
\n
Video 6: 
- How do I :red[remove columns] from a pandas DataFrame?
\nhttps://hotstocks2021-dataschool-streamlit-video6-jzo273.streamlit.app/
\n
Video 7: 
- How do I :red[sort] a pandas DataFrame or a Series?
\nhttps://hotstocks2021-dataschool-streamlit-video7-1djh6g.streamlit.app/
\n
Video 8: 
- How do I :red[filter rows] of a pandas DataFrame by column value?
\nhttps://hotstocks2021-dataschool-streamlit-video8-z6nkbu.streamlit.app/
\n
Video 9:
- How do I :red[apply multiple filter criteria] to a pandas DataFrame?
\nhttps://hotstocks2021-dataschool-streamlit-video9-a6hnvz.streamlit.app/
\n
Video 10: 
- Read only :red[specific columns] from a DataFrame
- Read only :red[specific rows] from a DataFrame
- :red[Iterate] DataFrame
- Select only :red[numeric columns] from a DataFrame
\nhttps://hotstocks2021-dataschool-streamlit-video10-hjpo76.streamlit.app/
\nVideo 11: 
- How do I use the :red["axis"] parameter in pandas?
\nhttps://hotstocks2021-dataschool-streamlit-video11-soifzw.streamlit.app/
\nVideo 12: 
- How do I use :red[string methods] in pandas?
\nhttps://hotstocks2021-dataschool-streamlit-video12-z8xivl.streamlit.app/
\nVideo 13: 
- How do I change the :red[data type] of a pandas Series?
\nhttps://hotstocks2021-dataschool-streamlit-video13-5yvvo4.streamlit.app/
\nVideo 14: 
- How should I use :red[groupby] in pandas?
\nhttps://hotstocks2021-dataschool-streamlit-video14-lilw1u.streamlit.app/
\nVideo 15: 
- How do I :red[explore] a pandas Series?
\nhttps://hotstocks2021-dataschool-streamlit-video15-l1d8x1.streamlit.app/
\nVideo 16: 
- How do I handle :red[missing values (NaN or N/A)] a pandas?
\nhttps://hotstocks2021-dataschool-streamlit-video16-tszfyb.streamlit.app/
"""
)
