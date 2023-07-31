#!/usr/bin/python3
"""
A script that displays given state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connecting to database and getting cities
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cursor.fetchall()
    out = []
    for row in rows:
        out.append(row[0])
    print(", ".join(out))
    cursor.close()
    db.close()
