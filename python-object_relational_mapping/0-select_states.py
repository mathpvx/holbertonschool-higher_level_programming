#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username>
<mysql password> <database name>"""


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
        database=sys.argv[3])

    """fetchall() returns a list of tuples of each row
    iterates on each tuple and prints
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
