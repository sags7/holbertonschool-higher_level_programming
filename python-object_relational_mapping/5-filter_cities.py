#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an
argument and lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password, database
name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = db.cursor()
    cur.execute("SELECT `name` FROM `cities`\
                JOIN `states` ON `cities`.`state_id` = `states`.`id`\
                WHERE `states`.`name` = %s\
                ORDER BY `cities`.`id` ASC", (sys.argv[4],)
                )
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
