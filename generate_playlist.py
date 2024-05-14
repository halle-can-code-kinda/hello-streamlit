import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import random

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
        elif slider[3] > 0:
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

def spotify_inputs():
    send_to_spotify = st.button("Create Spotify Playlist")
