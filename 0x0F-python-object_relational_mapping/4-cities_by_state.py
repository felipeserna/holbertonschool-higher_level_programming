#!/usr/bin/python3
"""
Module - lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    user_arg = sys.argv[1]
    passwd_arg = sys.argv[2]
    db_arg = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user_arg,
                           passwd=passwd_arg, db=db_arg, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities \
                 INNER JOIN states \
                 ON cities.state_id = states.id \
                 ORDER BY cities.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
