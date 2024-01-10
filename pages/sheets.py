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
    exclude = st.multiselect("Exclude: ", options=["Remixes","Live Performances", "Collaborations"])
    b1,b2 = st.columns(2)
    with b1:
        button = st.button("Create Playlist")
    with b2:
        lucky = st.button("I'm feeling lucky")

def get_totals():    
    total = 0
    for i in range(len(slider)):
        slider[i]=slider[i]-4
        total = total +abs(slider[i])
    return total, slider

def score(total_scores, individual_scores,data):
    weight = []
    for i in range(len(individual_scores)):
        weight.append(abs(individual_scores[i])/total_scores)
    st.write(len(data))
    weighted_songs = []
    for i in range(len(data)):
        #score old vs new slider
        if slider[0] < 0:
            st.write(data['tempo'].max())


    st.write(total_scores)
    st.write(individual_scores)
    st.write(weight)

def filter_songs(songs):
    if "Live Performances" in exclude:
        songs = songs.query('live==0')
    return songs

def luck(songs):
    random_songs = []
    for i in range(len(songs)):
        random_songs.append(songs.iloc[i,3])
    random_songs = pd.DataFrame(random.sample(random_songs,20))
    random_songs = random_songs.rename(columns = {0:"Song Title"})
    return random_songs

with col2:    
    if button:
        total, slider = get_totals()
        filtered_list = filter_songs(data)
        if total == 0:
            random_songs = luck(filtered_list)
            st.dataframe(random_songs, hide_index=True)
        else:
            score(total, slider,filtered_list) 


    if lucky:
        random_songs = luck(data)
        st.dataframe(random_songs, hide_index=True)    

