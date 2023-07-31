#!/usr/bin/python3
"""
Print values in states table based on matching given argument
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
                    WHERE name LIKE BINARY %(name) \
                    ORDER BY states.id ASC", {'name': sys.argv[4]})
    rows = cursor.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
    cursor.close()
    db.close()
