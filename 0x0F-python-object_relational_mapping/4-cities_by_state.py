#!/usr/bin/python3

"""
    script to list all the columns in cities
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":

    if len(argv) != 4:
        print("username, password and database name must enterd")
        exit(0)
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
    except Exception as e:
        print(e)
        exit(0)
    cur = db.cursor()
    statement = """SELECT c.id, c.name, s.name
        FROM cities as c INNER JOIN states as s
        ON c.state_id = s.id ORDER BY c.id ASC
        """
    cur.execute(statement)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
