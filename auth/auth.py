from flask import Blueprint
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask import request

auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/')
def test():
    return "auth route"

@auth_blueprint.route("/customer-login", methods=["POST"])
def customer_login():
    
    id_ = 0
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    ##############################

    id_ = f'{id}_m'
    access_token = create_access_token(identity=id_)
    return jsonify(access_token=access_token, role="member"), 200

@auth_blueprint.route("/doctor-login", methods=["POST"])
def doctor_login():
    
    id_ = 0
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    ##############################
    
    id_ = f'{id}_l'
    access_token = create_access_token(identity=id_)
    return jsonify(access_token=access_token, role="lead"), 200


@auth_blueprint.route("/protected", methods=["GET"])
@jwt_required()
def protected_test():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200