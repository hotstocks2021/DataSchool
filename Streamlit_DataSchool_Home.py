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
\nVideo 17: 
- What do I need to know about the pandas :red[index? (Part 1)]
\nhttps://hotstocks2021-dataschool-streamlit-video17-s3s6cw.streamlit.app/
\nVideo 18: 
- What do I need to know about the pandas :red[index? (Part 2)]
\nhttps://hotstocks2021-dataschool-streamlit-video18-tlcbgq.streamlit.app/
\nVideo 20: 
- How do I use :red[loc] and :red[iloc] from a pandas DataFrame?
\nhttps://hotstocks2021-dataschool-streamlit-video19-uvpk3r.streamlit.app/
\nVideo 21: 
- When should I use the :red[inplace] parameter in pandas?
\nhttps://hotstocks2021-dataschool-streamlit-video20-6yp26d.streamlit.app/
\nVideo 22: 
- How do I use pandas with :red[scikit-learn] to create Kaggle submissions?
- Export dataset to :red[CSV]
- Convert dataset to :red[pickle file] and pickel file back to dataset
\nhttps://hotstocks2021-dataschool-streamlit-video22-i6nvw6.streamlit.app/
\nVideo 23: 
- How do I use :red[sample] method in pandas?
\nhttps://hotstocks2021-dataschool-streamlit-video23-7xxrc7.streamlit.app/
\nVideo 24: 
- How do I create :red[dummy variables] in pandas?
\nhttps://hotstocks2021-dataschool-streamlit-video24-09o1p6.streamlit.app/
"""
)
