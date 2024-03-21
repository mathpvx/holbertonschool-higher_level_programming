#!/usr/bin/python3
"""Takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument and
that is safe from MySQL injections"""


import MySQLdb
import sys


if __name__ == "__main__":
    """execute only if from python interpreter itself"""

    """ co to DB"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        )

    cursor = db.cursor()

    state_name = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name = %s\
        ORDER BY states.id ASC", (sys.argv[4], ))

    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
