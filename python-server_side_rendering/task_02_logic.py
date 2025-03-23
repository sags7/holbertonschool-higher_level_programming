#!/usr/bin/python3

"""
In this task, you will enhance your Flask application by integrating dynamic content into your HTML templates using Jinja’s loop and conditional constructs. You will read a list of items from a JSON file and display them dynamically on a web page.

Objective
Use Jinja’s loop and conditional constructs to dynamically render content in HTML templates.
Read and parse JSON data in Python.
Integrate dynamic content into your Flask application.
"""

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        items = json.load(f)
    list_of_items = items.get('items', [])
    return render_template('items.html', items=list_of_items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
