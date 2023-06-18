#!/usr/bin/python3
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="lehjend419619", db="hbtn_0e_0_usa")

statement = "CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa"
cur = db.cursor()
# create_table = """
#     CREATE TABLE IF NOT EXISTS cities (
#         id INT NOT NULL AUTO_INCREMENT,
#         state_id INT NOT NULL,
#         name VARCHAR(256) NOT NULL,
#         PRIMARY KEY (id),
#         FOREIGN KEY(state_id) REFERENCES states(id)
#     )
# """
# cur.execute(create_table)

datas = ((6, "San Francisco"), (6, "San Jose"), (6, "Los Angeles"), (6, "Fremont"), (6, "Livermore"),(7, "Page"), (7, "Phoenix"),(8, "Dallas"), (8, "Houston"), (8, "Austin"),(9, "New York"), (10, "Las Vegas"), (10, "Reno"), (10, "Henderson"), (10, "Carson City"))
try:
	for data in datas:
		cur.execute(f"INSERT INTO cities (state_id, name) VALUES (%s, %s)", data)
except Exception as e:
    print(e)
db.commit()
cur.execute("SELECT * FROM states ORDER BY id DESC")
for state in cur:
    print(state)
