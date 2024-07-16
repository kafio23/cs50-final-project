# CS50-final-project
This Python Project recommends a song according to user's input (text). In order to interpretate user's emotions from the text, this program uses the sentiment analysis library *Transformers by Hugging* [https://huggingface.co/docs/transformers/index]. The metrics obtained go through a Custom Class which calculate the parameters to get the correct song from Spotify API.

User's input -> Transformers Library -> Custom Class -> Spotify API -> Song

## Spotify Setup
1. Create an Spotify App
2. Select options: Web API and Web Playback SDK
3. In file `.env` add `client_id` and `client_secret`

## How to install
```
npm run build
flask run
```