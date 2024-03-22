#!/usr/bin/python3
""" Takes the name of a state as an arg and l
ists all cities from the database hbtn_0e_4_usa
Usage: ./0-select_states.py <mysql username>
<mysql password> <database name> """


import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],)

    cursor = db.cursor()
    cursor.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (sys.argv[4], ))
    print(", ".join(map(lambda x: x[0], cursor.fetchall())))
    cursor.close()
    db.close()
