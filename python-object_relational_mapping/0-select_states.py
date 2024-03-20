#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


if __name__ == "__main__":
    """including the guard clause so that the code is only
    executed when the script is run directly
    """

    """establish a connection to the MySQLdb database"""
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    """calling the cursor method that will be used to execute SQL
    queries and fetch results from the database
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()