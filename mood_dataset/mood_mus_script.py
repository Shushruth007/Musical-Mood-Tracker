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
    offset = 0
    trackList = []
    length = sp.playlist_items(playlist)['total']
    while (offset < length):
        tracks = sp.playlist_items(playlist, limit=50, offset=offset)
        offset += 50
        for i, item in enumerate(tracks['items']):
            try:
                track = item['track']
                trackList.append(dict(name=track['name'], id=track['id'], artist=track['artists'][0]['name']))
            except:
                pass

    # print(trackList[0])
    return trackList

def write_to_csv(track_features, filename):
    df = pd.DataFrame(track_features)
    df.drop_duplicates(subset=['name','artist'])

    # normalizing loudness
    df['loudness'] = pd.DataFrame(normalize_loudness(df[['loudness']].values))

    print ('Total tracks in data set', len(df))
    df.to_csv(filename, index=False)

def append_to_csv(track_features, filename):
    df = pd.DataFrame(track_features)
    df.drop_duplicates(subset=['name','artist'])

    # normalizing loudness
    df['loudness'] = pd.DataFrame(normalize_loudness(df[['loudness']].values))

    print ('Total tracks in data set', len(df))
    with open(filename, 'a', encoding="utf-8") as f:
        df.to_csv(f, header=f.tell()==0, index=False)


# Get music from single playlist
def single(playlist, mood, filename):
    spot = sp.Spotify(client_credentials_manager=SpotifyClientCredentials())
    print ("Getting user tracks from playlists")
    tracks = get_tracks_from_playlist(playlist, spot)
    print ("Getting track audio features")
    tracks_with_features = get_features(tracks,spot, mood)
    print ("Storing into csv")
    write_to_csv(tracks_with_features, filename)


#get music from multiple playlists, in text file
def multiple(playlist, mood, filename):
    spot = sp.Spotify(client_credentials_manager=SpotifyClientCredentials())
    with open(playlist) as topo_file:
        for line in topo_file:
            print ("Getting user tracks from playlists")
            print(line)
            tracks = get_tracks_from_playlist(line, spot)
            print ("Getting track audio features")
            tracks_with_features = get_features(tracks,spot, mood)
            print ("Storing into csv")
            append_to_csv(tracks_with_features, filename)


def main(multi, playlist, mood, filename):
    print("Start")
    if (multi):
        multiple(playlist, mood, filename)
    else:
        single(playlist, mood, filename)


if __name__ == '__main__':
    print ('Starting...')
    parser = argparse.ArgumentParser(description='this script will grab tracks from playlists')
    # parser.add_argument('-m', action='store_true')
    # parser.add_argument('--pl', help='playlist')
    # parser.add_argument('--md', help='mood')
    parser.add_argument("--fn", help="filename")

    args = parser.parse_args()
    # main(args.m, args.pl, args.md, args.fn)
    main(True, "Great.txt", 1, args.fn)
    main(True, "Good.txt", 2, args.fn)
    main(True, "Okay.txt", 3, args.fn)
    main(True, "Sad.txt", 4, args.fn)
    main(True, "Very Sad.txt", 5, args.fn)
