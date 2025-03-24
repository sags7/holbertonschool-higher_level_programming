#!/usr/bin/python3
"""
Building on the previous exercise, you will now add the functionality
to fetch and display data from a SQLite database in your Flask application.
The application should allow users to choose between JSON, CSV, and SQL (SQLite database)
as data sources using the source query parameter.

Objective
Set up and interact with a SQLite database in a Flask application.
Extend existing functionality to handle multiple data sources.
Implement error handling for database-related issues.
"""

from flask import Flask, render_template, request
import csv
import json
import sqlite3

app = Flask(__name__)


def read_json_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def read_csv_file(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        data = []
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def read_sqlite_data():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    connection.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]


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


@app.route('/products')
def display_products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sqlite_data()
    else:
        return render_template('product_display.html', error='Wrong source')

    if id:
        product = [p for p in products if str(p['id']) == id]

        if not product:
            return render_template('product_display.html', error='Product not found')
        products = product

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
