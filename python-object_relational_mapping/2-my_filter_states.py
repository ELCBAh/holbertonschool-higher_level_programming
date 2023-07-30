#!/usr/bin/python3
"""
Given argument print values in states table where name matches argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connecting to database and getting states
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY '{}' \
                    ORDER BY id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
