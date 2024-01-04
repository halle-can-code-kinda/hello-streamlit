import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1poo8680VUsK15L5N_vh4N1xW4ygzHY3hlh3R2CoNv3g/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, usecols=[0, 1])
songs = pd.DataFrame(data)
st.dataframe(data)
values = range(0,9)
year_labels = ['old',' ',' ',' ','indifferent',' ',' ',' ','new']
year = st.select_slider("recent", values,label_visibility="collapsed",value =4, format_func=(lambda x:year_labels[x]))
speed_labels = ['slow',' ',' ',' ','indifferent',' ',' ',' ','fast']
speed = st.select_slider(" ", values,label_visibility="collapsed",value =4, format_func=(lambda x:speed_labels[x]))