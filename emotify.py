class Emotify:
    EMOTIONS_DICT = {
        "joy": {
            "mode": 1,
            "min_acousticness": 0.0,
            "max_acousticness": 0.3,
            "min_danceability": 0.5,
            "max_danceability": 1.0,
            "min_energy": 0.5,
            "max_energy": 1.0,
            "min_loudness": -20,
            "max_loudness": 0,
            "min_tempo": 100,
            "max_tempo": 300,
            "min_valence": 0.7,
            "max_valence": 1.0,
        },
        "surprise": {
            "min_danceability": 0.5,
            "max_danceability": 1.0,
            "min_energy": 0.5,
            "max_energy": 1.0,
            "min_loudness": -20,
            "max_loudness": 0,
            "min_tempo": 100,
            "max_tempo": 300,
        },
        "neutral": {
            "target_acousticness": 0.5,
            "target_danceability": 0.5,
            "target_energy": 0.5,
            "target_loudness": -30,
            "min_tempo": 50,
            "min_tempo": 200,
            "min_valence": 0.5,
            "max_valence": 0.7,
        },
        "sadness": {
            "mode": 0,
            "min_acousticness": 0.5,
            "max_acousticness": 1.0,
            "min_danceability": 0.0,
            "max_danceability": 0.4,
            "min_energy": 0.0,
            "max_energy": 0.4,
            "min_loudness": -60,
            "max_loudness": -20,
            "min_tempo": 0,
            "max_tempo": 70,
            "min_valence": 0.0,
            "max_valence": 0.3,
        },
        "anger": {
            "mode": 0,
            "min_acousticness": 0.0,
            "max_acousticness": 0.2,
            "min_energy": 0.7,
            "max_energy": 1.0,
            "min_loudness": -10,
            "max_loudness": -0.0,
            "min_tempo": 100,
            "max_tempo": 300,
            "min_valence": 0.0,
            "max_valence": 0.3,
        },
        "fear": {
            "mode": 0,
            "min_acousticness": 0.2,
            "max_acousticness": 0.8,
            "min_danceability": 0.0,
            "max_danceability": 0.4,
            "min_energy": 0.0,
            "max_energy": 0.4,
            "min_loudness": -60,
            "max_loudness": -20,
            "min_tempo": 20,
            "max_tempo": 100,
            "min_valence": 0.0,
            "max_valence": 0.5,
        },
        "disgust": {
            "mode": 0,
            "min_acousticness": 0.0,
            "max_acousticness": 0.4,
            "min_danceability": 0.0,
            "max_danceability": 0.7,
            "min_energy": 0.0,
            "max_energy": 0.8,
            "min_loudness": -50,
            "max_loudness": -10,
            "min_tempo": 20,
            "max_tempo": 200,
            "min_valence": 0.0,
            "max_valence": 0.3,
        },
    }

    def __init__(self, classifier, emotions):
        self.classifier = classifier
        self.emotions = emotions

    def get_emotions(self):
        return {
            "joy": next((x for x in self.emotions if x["label"] == "joy"), 0)["score"],
            "surprise": next((x for x in self.emotions if x["label"] == "surprise"), 0)[
                "score"
            ],
            "neutral": next((x for x in self.emotions if x["label"] == "neutral"), 0)[
                "score"
            ],
            "sadness": next((x for x in self.emotions if x["label"] == "sadness"), 0)[
                "score"
            ],
            "anger": next((x for x in self.emotions if x["label"] == "anger"), 0)[
                "score"
            ],
            "fear": next((x for x in self.emotions if x["label"] == "fear"), 0)[
                "score"
            ],
            "disgust": next((x for x in self.emotions if x["label"] == "disgust"), 0)[
                "score"
            ],
        }

    def positive_genres(self):
        return {"dance", "happy", "party", "pop", "road-trip"}

    def negative_genres(self):
        return {"acoustic", "hardcore", "emo", "rainy-day", "sad"}

    def get_parameters(self):
        if self.classifier["label"] == "POSITIVE":
            genres = self.positive_genres()
        else:
            genres = self.negative_genres()

        all_emotions = self.get_emotions()
        main_emotion = max(all_emotions, key=all_emotions.get)

        return {"genres": genres, "emotions_params": self.EMOTIONS_DICT[main_emotion]}
