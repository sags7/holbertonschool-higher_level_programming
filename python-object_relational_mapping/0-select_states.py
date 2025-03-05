#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all states
from a table, ordered by id in ascending order

Requirements:
- MySQL server is running
- hbtn_0e_usa database must exist and have a states table
- User must have the necessary permissions

Author: Juan Sebastian Aramburo
"""

import MySQLdb
import sys


def list_states():
    """
    Connects to MySQL database and retrieves all states from a table
    Raises: Exception - if unable to query database
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db="hbtn_0e_0_usa",
        charset="utf8"
    )

    cur = db.cursor()

    cur.execute("SELECT id, name FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
