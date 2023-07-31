#!/usr/bin/python3
"""
Lists cities of given database
"""
import sys
import MySQLdb

__init__ == "__main__":
    """
    Connecting to database and getting states
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                   INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
