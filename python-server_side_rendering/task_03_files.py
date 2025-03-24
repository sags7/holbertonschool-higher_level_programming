#!/usr/bin/python3
"""
In this task, you will build a feature in your Flask application to read and display product data from two different data formats: JSON and CSV. You will create a single HTML template that can display data from either file type, depending on a query parameter provided in the URL. You will add functionality to your Flask application to filter product data based on an optional id query parameter. Additionally, you will handle edge cases such as invalid source parameter values or when the specified id is not found in the data.

Objective
Read and parse data from JSON and CSV files.
Use query parameters in Flask to determine data sources and filter criteria.
Implement error handling for invalid inputs and missing data.
Render dynamic data in HTML templates using Jinja.

"""


from flask import Flask, render_template, request
import json, csv

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
