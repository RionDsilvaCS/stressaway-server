from flask import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask import request
import json
from flask_cors import cross_origin

journal_blueprint = Blueprint('journal_blueprint', __name__)

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

    new_journal = {"id":"8766989", "title":title, "body":body, "time":time}
    with open('./db/user_1.json', 'r') as file:
        data = json.load(file)
    
    data.append(new_journal)
        
    with open('./db/user_1.json', 'w') as file:
        json.dump(data, file)

    return jsonify(msg=new_journal), 200