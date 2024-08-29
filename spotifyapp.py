import spotipy

def authenticate_spotify(self):
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=os.getenv("7e311aa466b947909b3a708d4868e76d"),
            client_secret=os.getenv("4a7d7442354d499c821defa59cc1886c"),
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    self.user_id = sp.current_user()["id"]
    self.sp = sp