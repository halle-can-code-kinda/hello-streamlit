import spotipy

def authenticate_spotify(self):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    self.user_id = sp.current_user()["id"]
    self.sp = sp