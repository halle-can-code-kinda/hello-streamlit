import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.header("Taylor Swift Playlist")
st.write(" ")
col1, col2 = st.columns(2)
url = "https://docs.google.com/spreadsheets/d/1poo8680VUsK15L5N_vh4N1xW4ygzHY3hlh3R2CoNv3g/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
data = conn.read(spreadsheet=url, usecols=[0, 1])
songs = pd.DataFrame(data)
st.dataframe(data)

with col1:
    values = range(0,9)
    year_labels = ['old',' ',' ',' ','indifferent',' ',' ',' ','new']
    year = st.select_slider("recent", values,label_visibility="collapsed",value = 4, format_func=(lambda x:year_labels[x]))
    speed_labels = ['slow',' ',' ',' ','indifferent',' ',' ',' ','fast']
    speed = st.select_slider(" ", values,label_visibility="collapsed",value = 4, format_func=(lambda x:speed_labels[x]))
    mode_labels = ['happy',' ',' ',' ','indifferent',' ',' ',' ','sad']
    mode = st.select_slider(" ", values,label_visibility="collapsed",value = 4, format_func=(lambda x:mode_labels[x]))
    popularity_labels = ['less known',' ',' ',' ','indifferent',' ',' ',' ','hit']
    mode = st.select_slider(" ", values,label_visibility="collapsed",value = 4, format_func=(lambda x:popularity_labels[x]))
    t1,t2 = st.columns(2)
    with t1: 
        remix = st.toggle("Include Remixes", True)
    with t2:
        live = st.toggle("Include Live Performances", True)
    b1,b2 = st.columns(2)
    with b1:
        button = st.button("Create Playlist")
    with b2:
        lucky = st.button("I'm feeling lucky")

with col2:
    if button:
        st.dataframe(data)


