import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import random
import generate_playlist as gp


st.title("Taylor Swift Playlist")
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

if "button1" not in st.session_state:
    st.session_state["button1"] = False

if "button2" not in st.session_state:
    st.session_state["button2"] = False

with col1:
    values = range(0,9)
    year_labels = ['old',' ',' ',' ','indifferent',' ',' ',' ','new']
    slider.append(st.select_slider("recent", values,label_visibility="collapsed",value = 4, format_func=(lambda x:year_labels[x])))
    speed_labels = ['slow',' ',' ',' ','indifferent',' ',' ',' ','fast']
    slider.append(st.select_slider(" ", values,label_visibility="collapsed",value =4, format_func=(lambda x:speed_labels[x])))
    mode_labels = ['sad',' ',' ',' ','indifferent',' ',' ',' ','happy']
    slider.append(st.select_slider(" ", values,label_visibility="collapsed",value = 4, format_func=(lambda x:mode_labels[x])))
    popularity_labels = ['less known',' ',' ',' ','indifferent',' ',' ',' ','hit']
    slider.append(st.select_slider(" ", values,label_visibility="collapsed",value = 4, format_func=(lambda x:popularity_labels[x])))
    acoustic_labels = ['less acoustic',' ',' ',' ','indifferent',' ',' ',' ','more acoustic']
    slider.append(st.select_slider(" ", values,label_visibility="collapsed",value = 4, format_func=(lambda x:acoustic_labels[x])))
    t1,t2 = st.columns(2)
    with t1:
        t_remixes = st.toggle("Include Remixes",True)
    with t2: 
        t_live = st.toggle("Include Live Performances",True)
    b1,b2 = st.columns(2)
    with b1:
        button = st.button("Create Playlist")
    with b2:
        lucky = st.button("I'm feeling lucky")

# adding song to new playlist
with col2:    
    if button:
        st.session_state["button1"] = not st.session_state["button1"]
        total, slider = gp.get_totals()
        filtered_list = gp.filter_songs(data)
        if total == 0:
            random_songs = gp.luck(filtered_list)
            st.dataframe(random_songs, hide_index=True)
            gp.spotify_inputs()
        else:
            playlist = gp.score(total, slider,filtered_list)
            st.dataframe(playlist,hide_index=True)
            gp.spotify_inputs()

    if lucky:
        st.session_state["button1"] = not st.session_state["button1"]
        random_songs = gp.luck(data)
        st.dataframe(random_songs, hide_index=True)
        gp.spotify_inputs()
