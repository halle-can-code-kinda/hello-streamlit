
import requests
import json
spotify_token = 'fa7bf51d5c0242058e1737db56270f6f'
spotify_user_id = 'd84a30e86c93422699bb9be941893e25'
import streamlit as st


def create_playlist():
	"""Create A New Playlist"""
	request_body = json.dumps(
		{
			"name": "Taylor Swift is Awesome",
			"description": "Songs",
			"public": False,
		}
	)
	query = "https://api.spotify.com/v1/users/{}/playlists".format(
		spotify_user_id)
	response = requests.post(
		query,
		data=request_body,
		headers={
			"Content-Type": "application/json",
			"Authorization": "Bearer {}".format(spotify_token),
		},
	)
	response = response.json()
	return response["id"]


def add_song(playlist_id, urls):
	"""Add all liked songs into a new Spotify playlist"""

	request_data = json.dumps(urls)

	query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
		playlist_id)

	response = requests.post(
		query,
		data=request_data,
		headers={
			"Content-Type": "application/json",
			"Authorization": "Bearer {}".format(spotify_token)
		}
	)

	return "songs added successfully"



# creating spotify playlist
if st.button("Button"):
			 play_id = create_playlist()


# getting url for spotify songs

#urls = []
#for i in range(len(response['items'])):
	#urls.append(get_spotify_uri(song_info[i][0], song_info[i][1]))

# adding song to new playlist
#add_song(play_id, urls)
