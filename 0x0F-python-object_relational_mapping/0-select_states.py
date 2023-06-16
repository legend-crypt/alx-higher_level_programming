#!/usr/bin/python3

"""
    Import for mysql connection
"""
import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

def display(username, password, database):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    cur = db.cursor()
    statement = "SELECT * FROM states ORDER BY states.id ASC"
    cur.execute(statement)
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    display(username, password, database)