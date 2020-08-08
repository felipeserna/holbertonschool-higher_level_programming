#!/usr/bin/python3
"""
Module - Filter states by user input
"""


import MySQLdb
import sys


if __name__ == "__main__":
    user_arg = sys.argv[1]
    passwd_arg = sys.argv[2]
    db_arg = sys.argv[3]
    user_filter = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user_arg,
                           passwd=passwd_arg, db=db_arg, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
                 ORDER BY id ASC"
                .format(user_filter))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
