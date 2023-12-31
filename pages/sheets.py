import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import random

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
slider = []

with col1:
    values = range(0,9)
    year_labels = ['old',' ',' ',' ','indifferent',' ',' ',' ','new']
    slider.append(st.select_slider("recent", values,label_visibility="collapsed",value = 4, format_func=(lambda x:year_labels[x])))
    speed_labels = ['slow',' ',' ',' ','indifferent',' ',' ',' ','fast']
    slider.append(st.select_slider(" ", values,label_visibility="collapsed",value =4, format_func=(lambda x:speed_labels[x])))
    mode_labels = ['happy',' ',' ',' ','indifferent',' ',' ',' ','sad']
    slider.append(st.select_slider(" ", values,label_visibility="collapsed",value = 4, format_func=(lambda x:mode_labels[x])))
    popularity_labels = ['less known',' ',' ',' ','indifferent',' ',' ',' ','hit']
    slider.append(st.select_slider(" ", values,label_visibility="collapsed",value = 4, format_func=(lambda x:popularity_labels[x])))
    exclude = st.multiselect("Exclude: ", options=["Remixes","Live Peroformances", "Collaborations"])
    b1,b2 = st.columns(2)
    with b1:
        button = st.button("Create Playlist")
    with b2:
        lucky = st.button("I'm feeling lucky")

def get_playlist():
    
    for i in range(len(slider)):
        total = total + slider[i]
with col2:
    if button:
        if "Live Performances" in exclude:
            songs = songs.query('live==0')
        st.dataframe(songs)
        
    
    if lucky:
        random_songs = []
        for i in range(len(data)):
            random_songs.append(data.iloc[i,3])
        playlist = pd.DataFrame(random.sample(random_songs,20))
        playlist = playlist.rename(columns = {0:"Song Title"})
        st.dataframe(playlist, hide_index=True)



