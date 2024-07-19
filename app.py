import os
import spotipy
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
from transformers import pipeline
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__,  template_folder='template')

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

emotion_pipeline = pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base', top_k=None)
classifier = pipeline(task="sentiment-analysis")


@app.route('/', methods=['GET'])
def home():    
    return render_template("base.html")


@app.route('/emotify', methods=['POST'])
def emotify():
    if request.method == 'POST':
        user_text = request.form.get('textareaResponse', '')
        print(user_text)

        emotions = emotion_pipeline(user_text)
        preds = classifier(user_text)
        print(emotions)
        print(preds)
    
    print('Inside!!')
    print(f'My id is: {client_id}.')
    print(f'My secret key is: {client_secret}.')
    genres = ['classical', 'jazz']
    # TODO: CustomModel
    recommendations = get_spotify_recommendations(genres)
    print(f"Recommended genres: {recommendations['tracks'][0]}")
    return jsonify({'data': recommendations['tracks'][0]})

def get_spotify_recommendations(genres):
    recommendations = sp.recommendations(seed_genres=genres, limit=10)
    return recommendations
