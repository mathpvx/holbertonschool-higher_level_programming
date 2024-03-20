#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username>
<mysql password> <database name>"""


import MySQLdb
import sys


"""execute only if from python interpreter itself"""
if __name__ == "__main__":
    """ lists of arg taken when executing"""
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306
        )
    # instantiate a cursor
    cursor = db.cursor()
    # retrieves all columns from the specified table
    cursor.execute("SELECT * FROM `states` ORDER BY states.id")
    # .fetchall() returns a list of tuples of each row
    # iterates on each tuple and prints
    states = cursor.fetchall()
    for state in states:
        print(state)
    db.close()
