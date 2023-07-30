#!/usr/bin/python3
"""
Listing all states from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
