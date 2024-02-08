import requests
import json

user_id = "ynossnhxdkty7r7f48dfmeknr"

endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
request_body = json.dumps({
          "name": "Indie bands like Franz Ferdinand but using Python",
          "description": "My first programmatic playlist, yooo!",
          "public": False # let's keep it between us - for now
        })
response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":"fa7bf51d5c0242058e1737db56270f6f"})
playlist_id = response.json()['id']