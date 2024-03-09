from flask import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask import request
import json

learn_blueprint = Blueprint('learn_blueprint', __name__)

@learn_blueprint.route('/')
def test():
    return jsonify(msg="learn route"), 200

@learn_blueprint.route('/get-learn')
def get_learn():

    with open('./db/learn.json', 'r') as file:
        data = json.load(file)
    
    return jsonify(learn=data), 200