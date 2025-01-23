from flask import Blueprint, request, jsonify
from models.User import User
from utils.extensions import db
from flask_jwt_extended import create_access_token

auth_route = Blueprint("auth", __name__)

@auth_route.route("/register", methods=["POST"])
def register():
    user_data = request.json
    if not all([user_data.get("username"), user_data.get("password")]):
        return jsonify({
            "message": "username and password are required"
        }), 400

    if User.query.filter_by(username=user_data["username"]).first():
        return jsonify({
            "message": "User already exists"
        }), 400

    new_user = User(username=user_data["username"], password=user_data["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201


@auth_route.route("/login", methods=["POST"])
def login():
    user_data = request.json
    if not all([user_data.get("username"), user_data.get("password")]):
        return jsonify({
            "message": "username and password are required"
        }), 400

    user = User.query.filter_by(username=user_data["username"]).first()

    if not user:
        return jsonify({
            "message": "Invalid username or password"
        }), 401
    if user.password != user_data["password"]:
        return jsonify({
            "message": "Invalid username or password"
        }), 401

    access_token = create_access_token(identity=str(user.user_id))

    return jsonify({
        "username": user.username,
        "access_token": access_token,
    }), 200
