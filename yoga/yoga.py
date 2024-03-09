from flask import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask import request
import json

yoga_blueprint = Blueprint('yoga_blueprint', __name__)

@yoga_blueprint.route('/')
def test():
    return jsonify(msg="yoga route"), 200

@yoga_blueprint.route('/get-yoga')
def get_yoga():

    with open('./db/yoga.json', 'r') as file:
        data = json.load(file)

    return jsonify(yoga=data), 200