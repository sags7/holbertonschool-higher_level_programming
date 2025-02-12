#!/usr/bin/python3
"""
Consumes and processes data from an API using Python
"""

import requests
import csv

fetchedRequests = requests.get("https://jsonplaceholder.typicode.com/posts")


def fetch_and_print_posts():
    """fetches and prints posts"""

    if fetchedRequests.status_code == 200:
        fetched_data = fetchedRequests.json()
        for data in fetched_data:
            print(f"{data['title']}")


def fetch_and_save_posts():
    """fetches and saves posts"""
    
    if fetchedRequests.status_code == 200:
        with open("posts.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
            
            writer.writerow(["id", "title", "body"])
            for data in fetchedRequests.json():
                writer.writerow([data["id"], data["title"], data["body"]])
