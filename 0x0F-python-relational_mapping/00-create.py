#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="lehjend419619", db="hbtn_0e_0_usa")

statement = "CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa"
cur = db.cursor()
create_table = """
	CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id))
"""

# datas = ("California", "Arizona", "Texas", "New York", "Nevada")
# for data in datas:
# 	cur.execute(f"INSERT INTO states (name) VALUES ('{data}')")
# db.commit()
cur.execute("SELECT * FROM states ORDER BY id DESC")
for state in cur:
    print(state)
