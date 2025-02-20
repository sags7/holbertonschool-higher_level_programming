#!/usr/bin/python3
"""
Sets up a simple Flask application that defines and
handles routes and responds to different endpoints,
including POST requests to add data to the API.
"""

from flask import Flask
from flask import jsonify
from flask import request

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}}

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": f"{username} not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return {"error": "Username is required"}, 400
    if username in users:
        return {"error": "Username already exists"}, 400
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


@app.route("/data")
def serve_data():
    return jsonify(list(users.keys()))
