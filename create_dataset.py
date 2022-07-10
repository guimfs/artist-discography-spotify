import spotipy
from spotipy import SpotifyClientCredentials
from decouple import config

# This section is where the Spotify API is called
client_id = config("id")
client_secret = config("secret")
auth = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
client = spotipy.Spotify(client_credentials_manager=auth)

# This section is where the dataset's root is created
dataset_ = list()

# Here you can put any artist's link to create a dataset
artist = "https://open.spotify.com/artist/5Wabl1lPdNOeIn0SQ5A1mp?si=JwT-cUB1QgaK4zVn8dSnqA"
artist_uri = artist.split("/")[-1].split("?")[0]
albums = client.artist_albums(artist_uri)['items']
artist_name = albums[0]['artists'][0]['name']

# Here I selected the most important attributes of tracks and albums. You can change according to your preference
for album in albums:
    album_id = album['id']
    album_uri = album['uri']
    album_name = album['name']
    album_img = album['images'][0]['url']
    album_year = album['release_date']
    album_popularity = 0    
    tracks = client.album_tracks(album_uri)['items']
    for index, _ in enumerate(tracks):
        track_id = tracks[index]['id']
        track_name = tracks[index]['name']
        track_features = client.audio_features(track_id)[0]
        dictionary = dict()
        dictionary["artist_name"] = artist_name
        dictionary["album_name"] = album_name
        dictionary["album_img"] = album_img
        dictionary["album_year"] = album_year
        dictionary["track_name"] = track_name
        dictionary["track_id"] = index
        for feature, value in track_features.items():
            if feature in [
                "danceability",
                "energy",
                "key",
                "loudness",
                "mode",
                "speechiness",
                "acousticness",
                "instrumentalness",
                "liveness",
                "valence",
                "tempo",
                "duration_ms",
                "time_signature"]:
                dictionary[feature] = value
        dataset_.append(dictionary)

# This section is where csv and json files are named
json_archive = f'{artist_name.split()[0].lower()}_{artist_name.split()[1].lower()}_discography.json'
csv_archive = f'{artist_name.split()[0].lower()}_{artist_name.split()[1].lower()}_discography.csv'

# This section is where the album release year is converted to an integer
for data in dataset_:
    data["album_year"] = int(data["album_year"][0:4])

# This is the final dataset
dataset = dataset_



    



