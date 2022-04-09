import spotipy as sp
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn import preprocessing
import os
import pandas as pd
import argparse

os.environ["SPOTIPY_CLIENT_ID"] = "988f2b18b9da4913a53774eae0b618fa"
os.environ["SPOTIPY_CLIENT_SECRET"] = "d1abb213da9040db907cf8a0573c7dfa"

def get_track_features(track_id, sp):
    if track_id is None:
        return None
    else:
        features = sp.audio_features([track_id])
    return features

def normalize_loudness(loudness):
    min_max_scaler = preprocessing.MinMaxScaler()
    loudness_scaled = min_max_scaler.fit_transform(loudness)
    return loudness_scaled

def get_features(tracks, sp, mood):
    tracks_with_features=[]

    for track in tracks:
        features = get_track_features(track['id'], sp)
        print (track['name'])
        if not features:
            print("passing track %s" % track['name'])
            pass
        else:
            f = features[0]
            tracks_with_features.append(dict(
                                            name=track['name'],
                                            artist=track['artist'],
                                            id=track['id'],
                                            danceability=f['danceability'],
                                            energy=f['energy'],
                                            loudness=f['loudness'],
                                            speechiness=f['speechiness'],
                                            acousticness=f['acousticness'],
                                            tempo=f['tempo'],
                                            liveness=f['liveness'],
                                            valence=f['valence'],
                                            mood=mood
                                            ))

        # time.sleep(0.1)

    # print(tracks_with_features[0])
    return tracks_with_features

def get_tracks_from_playlist(playlist, sp):
    playlist = sp.playlist_items(playlist)
    trackList = []
    tracks = playlist
    for i, item in enumerate(tracks['items']):
        track = item['track']
        trackList.append(dict(name=track['name'], id=track['id'], artist=track['artists'][0]['name']))

    # print(trackList[0])
    return trackList

def write_to_csv(track_features, filename):
    df = pd.DataFrame(track_features)
    df.drop_duplicates(subset=['name','artist'])

    # normalizing loudness
    df['loudness'] = pd.DataFrame(normalize_loudness(df[['loudness']].values))

    print ('Total tracks in data set', len(df))
    df.to_csv(filename, index=False)




def main(playlist, mood, filename):
    spot = sp.Spotify(client_credentials_manager=SpotifyClientCredentials())
    print ("Getting user tracks from playlists")
    tracks = get_tracks_from_playlist(playlist, spot)
    print ("Getting track audio features")
    tracks_with_features = get_features(tracks, spot, mood)
    print ("Storing into csv")
    write_to_csv(tracks_with_features, filename)

if __name__ == '__main__':
    print ('Starting...')
    parser = argparse.ArgumentParser(description='this script will grab tracks from playlists')
    parser.add_argument('--pl', help='playlist')
    parser.add_argument('--md', help='mood')
    parser.add_argument("--fn", help="filename")

    args = parser.parse_args()
    main(args.pl, args.md, args.fn)