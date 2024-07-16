from flask import Flask, render_template, jsonify, request
from transformers import pipeline

app = Flask(__name__,  template_folder='template')

emotion_pipeline = pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base', return_all_scores=True)
classifier = pipeline(task="sentiment-analysis")

@app.route('/index')
def hello():
    text = "This was a great day, I would like to talk to everyone!"
    emotions = emotion_pipeline(text)
    preds = classifier(text)
    print(emotions)
    print(preds)
    preds = [{"score": round(pred["score"], 4), "label": pred["label"]} for pred in preds]
    print(preds)
    
    return render_template("home.html")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_text = request.form.get('textareaResponse', '')
        print(user_text)

    emotions = emotion_pipeline(user_text)
    preds = classifier(user_text)
    print(emotions)
    print(preds)
    
    return render_template("base.html")

@app.route('/data', methods=['GET'])
def get_data():
    data = [
        {'name': 'John Doe', 'age': 32, 'city': 'New York'},
        {'name': 'Jane Doe', 'age': 27, 'city': 'London'},
        {'name': 'Jim Smith', 'age': 45, 'city': 'Paris'},
    ]
    return jsonify({'data': data})
