#!/usr/bin/python3
"""

"""

import MySQLdb # type: ignore
import sys


def filter_states():
    """
    Connects to MySQL database and retrieves all states from a table
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = db.cursor()

    cur.execute("SELECT `states.id`, `states.name` FROM `states` WHERE `states`.`name` LIKE `N%` ORDER BY `states`.`id` ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    filter_states()
