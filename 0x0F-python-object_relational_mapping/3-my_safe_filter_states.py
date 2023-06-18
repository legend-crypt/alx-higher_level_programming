#!/usr/bin/python3
"""
    import for working querying data and getting command line args
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
    except Exception:
        print("Failed to connect to Databse")
        exit(0)
    cur = db.cursor()
    searched = argv[4]
    statement = "SELECT * FROM states WHERE name = BINARY %s \
        ORDER BY states.id ASC"
    cur.execute(statement, (searched,))
    row = cur.fetchall()
    print(row)
    cur.close()
    db.close()
