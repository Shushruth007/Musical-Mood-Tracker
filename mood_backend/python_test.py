from itertools import count
import spotipy as sp
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn import preprocessing
import os
import pandas as pd
import argparse
import json
import requests
import math
import sys

os.environ["SPOTIPY_CLIENT_ID"] = "988f2b18b9da4913a53774eae0b618fa"
os.environ["SPOTIPY_CLIENT_SECRET"] = "d1abb213da9040db907cf8a0573c7dfa"
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:8080/'



def get_last_songs(spot):
    fetch = spot.current_user_recently_played(limit=20)
    songs = fetch["items"]
    song_list = []
    for i, item in enumerate(songs):
        try:
            track = item['track']
            print(track['name'])
            song_list.append(track['id'])
        except:
            pass

    return song_list

def create_feature_list(song_list, spot):
    feature_list = []
    for song in song_list:
        f = get_track_features(song, spot)
        if not f:
            pass
        else:
            f = f[0]
            req_features = {"acousticness" : f["acousticness"],
                            "danceability": f["danceability"],
                            "liveness": f["liveness"],
                            #"loudness": f["loudness"],
                            "speechiness": f["speechiness"],
                            "tempo": f["tempo"],
                            "valence": f["valence"]}
            feature_list.append(req_features)
    return feature_list

def get_track_features(track_id, sp):
    if track_id is None:
        return None
    else:
        features = sp.audio_features([track_id])
    return features

def get_mood(feature_list):
    count = 0
    score = 0
    for item in feature_list:
        count += 1
        mood = get_prediction(item)
        score += mood

    return math.ceil(score/count)

def get_prediction(features):
    response = requests.post(
    url='https://base-api.mage.ai/v1/predict',
    headers={
        'Content-Type': 'application/json',
    },
    data=json.dumps({
  "api_key": "fj76C91aptJrT15HO56TDC14Yo0YhpPZz6RH22S7",
  "features": [
    features
  ],
  "model": "custom_prediction_classification_1649533288907",
  "version": "1"
}),
)

    predictions = response.json()
    return (predictions[0]["prediction"])


def call_api():
    scope = "user-read-recently-played"

    token = util.prompt_for_user_token("Shushruth007", scope)
    if token:
        spt = sp.Spotify(auth=token)
        songs = get_last_songs(spt)
        features = create_feature_list(songs, spt)
        return get_mood(features)


# print(get_prediction({
#       "acousticness": 0.0332,
#       "danceability": 0.789,
#       "liveness": 0.0876,
#       "loudness": 0.6429850746268657,
#       "speechiness": 0.041,
#       "tempo": 112.985,
#       "valence": 0.753
#     }))

