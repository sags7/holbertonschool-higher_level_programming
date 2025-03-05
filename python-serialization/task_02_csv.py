#!/usr/bin/python3
"""
module provides example functionality
to convert from CSV to JSON
"""

import csv
import json
import os


def convert_csv_to_json(filename_csv):
    """converts a csv file to json"""
    if not os.path.exists(filename_csv):
        print("file to convert, not found")
        return False
    try:
        data = []
        with open(filename_csv, "r", encoding="utf-8") as csv_file:
            csvReader = csv.DictReader(csv_file)
            for row in csvReader:
                data.append(row)
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)
            return True
    except (EOFError, OSError, csv.Error) as err:
        print(f"error converting csv to json: {err}")
        return False
