import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "my-client-id"
client_secret = "my-client-secret"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
# print(user_id)

billboard_urlDate = "https://www.billboard.com/charts/hot-100/"

response = requests.get(f"{billboard_urlDate}2023-07-29/")
billboard = response.text

# print(billboard)
soup = BeautifulSoup(billboard, "html.parser")

song_title = soup.select("li ul li h3")
# print(song_title)
# print(song_title.find(class_="c-title__link ").getText())
song_titles = []
for song in song_title:
    song_titles.append(song.getText().strip())

# print(song_titles)


# date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
# 2023-07-29
song_names = ["The list of song", "titles from your", "web scrape"]
# song_uris = []
# year = date.split("-")[0]
# for song in song_names:
#
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     print(result)
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} doesn't exist in Spotify. Skipped.")

user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

