#!/usr/bin/python3

import MySQLdb


def list_states():
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
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
