#!/usr/bin/python3
"""
Module - Filter states by user input. Safe from MySQL injections
"""


import MySQLdb
import sys


if __name__ == "__main__":
    user_arg = sys.argv[1]
    passwd_arg = sys.argv[2]
    db_arg = sys.argv[3]
    state_name = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user_arg,
                           passwd=passwd_arg, db=db_arg, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name \
                 FROM cities \
                 INNER JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name=%s \
                 ORDER BY cities.id", (state_name,))
    query_rows = cur.fetchall()
    print(", ".join(row[0] for row in query_rows))
    cur.close()
    conn.close()
