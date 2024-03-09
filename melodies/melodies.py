from flask import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask import request
from flask_cors import cross_origin
import random
import json

melodies_blueprint = Blueprint('melodies_blueprint', __name__)

@melodies_blueprint.route('/')
def test():
    return jsonify(msg="melodies route"), 200

@melodies_blueprint.route('/get-melodies')
@cross_origin()
def get_melodies():
    tag = request.json.get("tag", 'Stress_Relief') #'Stress_Relief'

    with open('./db/song.json', 'r') as file:
        all_songs = json.load(file)

    selected_songs = random.sample(all_songs[tag], 6)

    
    return jsonify(tracks=selected_songs), 200