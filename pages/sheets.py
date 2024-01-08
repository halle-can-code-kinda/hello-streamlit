import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.header("Taylor Swift Playlist")
st.write(" ")
col1, col2 = st.columns(2)
url = "https://docs.google.com/spreadsheets/d/1poo8680VUsK15L5N_vh4N1xW4ygzHY3hlh3R2CoNv3g/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)
cols = []
for i in range(26):
    cols.append(i)
data = conn.read(spreadsheet=url, usecols=cols)
songs = pd.DataFrame(data)

with col1:
    values = range(-4,4)
    year_labels = ['old',' ',' ',' ','indifferent',' ',' ',' ','new']
    year = st.select_slider("recent", values,label_visibility="collapsed",value = 0, format_func=(lambda x:year_labels[x]))
    speed_labels = ['slow',' ',' ',' ','indifferent',' ',' ',' ','fast']
    speed = st.select_slider(" ", values,label_visibility="collapsed",value = 0, format_func=(lambda x:speed_labels[x]))
    mode_labels = ['happy',' ',' ',' ','indifferent',' ',' ',' ','sad']
    mode = st.select_slider(" ", values,label_visibility="collapsed",value = 0, format_func=(lambda x:mode_labels[x]))
    popularity_labels = ['less known',' ',' ',' ','indifferent',' ',' ',' ','hit']
    mode = st.select_slider(" ", values,label_visibility="collapsed",value = 0, format_func=(lambda x:popularity_labels[x]))
    exclude = st.multiselect("Exclude: ", options=["Remixes","Live Peroformances", "Collaborations"])
    b1,b2 = st.columns(2)
    st.write(values)
    with b1:
        button = st.button("Create Playlist")
    with b2:
        lucky = st.button("I'm feeling lucky")

with col2:
    if button:
        if "Live Performances" in exclude:
            songs = songs.query('live==0')
        st.dataframe(songs)


