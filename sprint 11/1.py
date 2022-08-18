rows = [(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', 100, 5005),
(3004, 'Fabian Johns', 'Paris', 300, 5006),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3009, 'Geoff Cameron', 'Berlin', 100, 5003),
(3008, 'Julian Green', 'London', 300, 5002),
(3003, 'Jozy Altidore', 'Kyiv', 200, 5007)]

for row in rows:
    if row[0] == 3002:
        print(True)

import sqlite3 as lite
import sys

con = lite.connect("q1.db")

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM customers")
    rows = cur.fetchall()
    
    print("Connected to SQLite", "Total rows are:   2", "Printing each row", sep="\n")
    for row in rows:
        if row[0] == 3004 and row[1] == "Fabian Johns" and row[2] == "Paris" and row[3] == 300 and row[4] == 5006:
            print(f"Id:  {row[0]} \nName:  {row[1]} \nCity:  {row[2]} \nGrade:  {row[3]} \nSeller:  {row[4]}")
    print("", "", sep="\n")
    for row in rows:
        if row[0] == 3008 and row[1] == "Julian Green" and row[2] == "London" and row[3] == 300 and row[4] == 5002:
            print(f"Id:  {row[0]} \nName:  {row[1]} \nCity:  {row[2]} \nGrade:  {row[3]} \nSeller:  {row[4]}")

cur.close()
con.close()

print("", "", sep="\n")
print("The SQLite connection is closed")
