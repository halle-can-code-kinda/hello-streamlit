import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import random


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
    weighted_songs = []
    for i in range(len(data)):
        score = 0
        #score old vs new slider
         #score tempo
        if slider[0] < 0:
            score = score + (1/(data['release_year'].min()-data['release_year'].max())*data.iloc[i,8]-1/(data['release_year'].min()-data['release_year'].max())*data['release_year'].max())*weight[0]
        elif slider[0] > 0:
            score = score + (1/(data['release_year'].max()-data['release_year'].min())*data.iloc[i,8]-1/(data['release_year'].max()-data['release_year'].min())*data['release_year'].min())*weight[0]
        #score tempo
        if slider[1] < 0:
            score = score + (1/(data['tempo'].min()-data['tempo'].max())*data.iloc[i,20]-1/(data['tempo'].min()-data['tempo'].max())*data['tempo'].max())*weight[1]
        elif slider[1] > 0:
            score = score + (1/(data['tempo'].max()-data['tempo'].min())*data.iloc[i,20]-1/(data['tempo'].max()-data['tempo'].min())*data['tempo'].min())*weight[1]
        #score valence
        if slider[2] < 0:
            score = score + (1/(data['valence'].min()-data['valence'].max())*data.iloc[i,22]-1/(data['valence'].min()-data['valence'].max())*data['valence'].max())*weight[2]
        elif slider[2] > 0:
            score = score + (1/(data['valence'].max()-data['valence'].min())*data.iloc[i,22]-1/(data['valence'].max()-data['valence'].min())*data['valence'].min())*weight[2]
         #score popularity
        if slider[3] < 0:
            score = score + (1/(data['popularity'].min()-data['popularity'].max())*data.iloc[i,23]-1/(data['popularity'].min()-data['popularity'].max())*data['popularity'].max())*weight[3]
        elif slider[3] > 0:
            score = score + (1/(data['popularity'].max()-data['popularity'].min())*data.iloc[i,23]-1/(data['popularity'].max()-data['popularity'].min())*data['popularity'].min())*weight[3]
        if slider[4] < 0:
            score = score + (1/(data['acousticness'].min()-data['acousticness'].max())*data.iloc[i,11]-1/(data['acousticness'].min()-data['acousticness'].max())*data['acousticness'].max())*weight[4]
        elif slider[4] > 0:
            score = score + (1/(data['acousticness'].max()-data['acousticness'].min())*data.iloc[i,11]-1/(data['acousticness'].max()-data['acousticness'].min())*data['acousticness'].min())*weight[4]
        weighted_songs.append([data.iloc[i,3],data.iloc[i,0],score,data.iloc[i,8],data.iloc[i,20],data.iloc[i,22],data.iloc[i,23]])
    weighted_songs = pd.DataFrame(weighted_songs)
    weighted_songs = weighted_songs.sort_values(2,ascending=False)
    #st.dataframe(weighted_songs)
    song_list = []
    for i in range(30):
        song_list.append(weighted_songs.iloc[i,0])
    song_list = pd.DataFrame(random.sample(song_list,20))
    song_list = song_list.rename(columns={0:"Song Title"})
    return song_list

def filter_songs(songs):
    if t_live == False:
        songs = songs.query('live==0')
    if t_remixes == False:
        songs = songs.query('remix==0')
    return songs

def luck(songs):
    random_songs = []
    for i in range(len(songs)):
        random_songs.append(songs.iloc[i,3])
    random_songs = pd.DataFrame(random.sample(random_songs,20))
    random_songs = random_songs.rename(columns = {0:"Song Title"})
    return random_songs


 
# adding song to new playlist
with col2:    
    if button:
        st.session_state["button1"] = not st.session_state["button1"]
        total, slider = get_totals()
        filtered_list = filter_songs(data)
        if total == 0:
            playlist = luck(filtered_list)
            st.dataframe(playlist, hide_index=True)

        else:
            playlist = score(total, slider,filtered_list)
            st.dataframe(playlist,hide_index=True)


    if lucky:
        st.session_state["button1"] = not st.session_state["button1"]
        playlist = luck(data)
        st.dataframe(playlist, hide_index=True)

