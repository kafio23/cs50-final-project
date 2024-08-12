# CS50-final-project
#### Video Demo:  https://www.youtube.com/watch?v=kCb4bIIqZrI
#### Description: This Python Project recommends and plays a song based on the user's input (text). To assess the user's emotions from the text, the program utilizes the sentiment analysis library [Transformers by Hugging](https://huggingface.co/docs/transformers/index). The metrics generated are processed through a Custom Class (Emotify) which selects the parameters in order to retrieve the correct song from [Spotify API](https://developer.spotify.com/documentation/web-api).

User's input -> Transformers Library -> Custom Class (Emotify) -> Spotify API -> Recommended Song

## Spotify Setup
1. Create an Spotify App
2. Select options: Web API and Web Playback SDK
3. In [Spotify Dashboard](https://developer.spotify.com/dashboard) get **Client ID** and **Client Secret**. Also add a **Redirect URI**.
4. In the file `.env` of this project, add `client_id`, `client_secret` and `redirect_uri`.

## Prerequisites
1. nodejs >= 21.0.0
2. python >= 3.10.0
3. Virtual env:
```
python -m venv venv
source venv/bin/activate 
```

## How to install
```
pip install -r requirements.txt
npm install
```

## Usage
```
npm run build
flask run
```

## Technologies
1. Backend: Flask
2. Frontend: React + Webpack
3. Images (background, favicon, etc) were generated with [Google Gemini](https://gemini.google.com/app)