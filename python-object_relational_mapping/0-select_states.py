#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to the database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3])

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    # Fetch all the rows
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals():
        db.close()
