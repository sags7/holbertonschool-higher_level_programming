#!/usr/bin/python3
"""
Sets up a simple Flask application
with basic authentication and authorization
using Flask-HTTPAuth.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "MYSUPERSECRETKEY"  # change key later
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user


@app.route("/")
def home():
    return "Welcome to the Flask API!", 200


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )
    return jsonify({"access_token": f"{access_token}"}), 200


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted"), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted"), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    if get_jwt_identity()["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 401
    return jsonify(message="Admin Access: Granted"), 200


""" Custom error handlers for JWT"""


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"error": "Missing Authorization Header"}), 401


@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"error": "Invalid Token"}), 401


@jwt.expired_token_loader
def expired_token_response(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(debug=True)
