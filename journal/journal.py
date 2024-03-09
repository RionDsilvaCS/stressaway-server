from flask import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask import request
import json
from flask_cors import cross_origin
import requests
import os

journal_blueprint = Blueprint('journal_blueprint', __name__)

def get_sentiment(api_key, user_input):
    url = "https://api.fireworks.ai/inference/v1/completions"
    payload = {
    "model": "accounts/fireworks/models/mixtral-8x7b-instruct",
    "max_tokens": 4096,
    "top_p": 1,
    "top_k": 40,
    "presence_penalty": 0,
    "frequency_penalty": 0,
    "temperature": 0.1,
    "prompt": f"consider you are an expert in sentiment analysis from text given for a mental health assist based web application\n\ni want you to do the sentiment analysis for the {user_input} based on emotions etc, some example of tags include\n\nPositive, Negative, Neutral, Happy, Sad, Joyful, Cheerful, Excited, Content, Angry, Disappointed, Surprised, Frustrated, Calm, Anxious, Hopeful, Optimistic, Pessimistic, Confused, Satisfied, Inspirational, Motivated, Nostalgic, Amused, Appreciative.\n\nThe output should display only the sentiment of the given sentence, without any additional information or explanations. The format should be as follows:\n\ninput:\n{{input}}: where the user types the input and you have to get the sentiment.\n\noutput :\n{{sentiment}}: just display the sentiment of the given sentence without any additional information.\n\ninstructions:\n1) take only the sentence given by the user as input.\n2) Display only the sentiment of the sentence given by user as output, without any additional information.\n\nInput:\n{user_input}\n",
}
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        try:
            data = response.json()
            sentiment_output = data.get("choices", [{}])[0].get("text", "")
            if not sentiment_output:
                sentiment_output = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            return sentiment_output
        except Exception as e:
            print(f"Error: {e}")
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


@journal_blueprint.route('/')
def test():
    return jsonify(msg="journal route"), 200

@journal_blueprint.route('/get-journal')
@cross_origin()
def get_journal():
    
    with open('./db/user_1.json', 'r') as file:
        data = json.load(file)

    return jsonify(journals=data), 200

@journal_blueprint.route('/create-journal', methods=['POST'])
@cross_origin()
def create_journal():
    title = request.json.get("title", None)
    body = request.json.get("body", None)
    time = request.json.get("time", None)

    new_journal = {"id":"8766989", "title":title, "body":body, "date":time}
    with open('./db/user_1.json', 'r') as file:
        data = json.load(file)
    
    data.append(new_journal)
        
    with open('./db/user_1.json', 'w') as file:
        json.dump(data, file)

    return jsonify(msg="Success"), 200

@journal_blueprint.route('/create-journal-ai', methods=['POST'])
@cross_origin()
def create_journal_ai():
    title = request.json.get("title", None)
    body = request.json.get("body", None)
    time = request.json.get("time", None)

    new_journal = {"id":"8766989", "title":title, "body":body, "date":time}
    with open('./db/user_1.json', 'r') as file:
        data = json.load(file)
    
    data.append(new_journal)
        
    with open('./db/user_1.json', 'w') as file:
        json.dump(data, file)
    
    api_key = os.environ.get('API_KEY')
    sentiment = get_sentiment(api_key, body)

    return jsonify(msg=sentiment), 200