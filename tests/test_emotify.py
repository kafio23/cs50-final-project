import pytest
from emotify import Emotify

emotions = [
    [
        {"label": "neutral", "score": 0.549},
        {"label": "sadness", "score": 0.111},
        {"label": "disgust", "score": 0.104},
        {"label": "surprise", "score": 0.078},
        {"label": "anger", "score": 0.064},
        {"label": "fear", "score": 0.051},
        {"label": "joy", "score": 0.040},
    ]
]

preds = [{"label": "POSITIVE", "score": 0.748}]


@pytest.fixture
def empty_emotify():
    return Emotify(classifier=preds[0], emotions=emotions[0])


def test_positive_genres(empty_emotify):
    assert empty_emotify.positive_genres() == {
        "dance",
        "happy",
        "party",
        "pop",
        "road-trip",
    }


def test_negative_genres(empty_emotify):
    assert empty_emotify.negative_genres() == {
        "acoustic",
        "hardcore",
        "emo",
        "rainy-day",
        "sad",
    }


def test_get_emotions(empty_emotify):
    assert empty_emotify.get_emotions() == {
        "joy": 0.040,
        "surprise": 0.078,
        "neutral": 0.549,
        "sadness": 0.111,
        "anger": 0.064,
        "fear": 0.051,
        "disgust": 0.104,
    }


def test_get_parameters(empty_emotify):
    assert empty_emotify.get_parameters() == {
        "genres": {"dance", "happy", "party", "pop", "road-trip"},
        "emotions_params": {
            "target_acousticness": 0.5,
            "target_danceability": 0.5,
            "target_energy": 0.5,
            "target_loudness": -30,
            "min_tempo": 50,
            "min_tempo": 200,
            "min_valence": 0.5,
            "max_valence": 0.7,
        },
    }
