import sqlite3 as lite
import sys

con = lite.connect("q1.db")
    
try:
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM customers WHERE grade > 200 ORDER BY Id")
        rows = cur.fetchall()
    
    print(f"Connected to SQLite \nTotal rows are:   {len(rows)} \nPrinting each row")
    for row in rows:
        print(f"Id:  {row[0]} \nName:  {row[1]} \nCity:  {row[2]} \nGrade:  {row[3]} \nSeller:  {row[4]}")
       # print(f" {row[0]} \n  {row[1]} \n  {row[2]} \n  {row[3]} \n  {row[4]} \n ")
        print("", "", sep="\n")
except sqlite3.Error as e:
    print('ERROR', e) # \n
        # print(traceback.print_exc())
    
    
    # print("Connected to SQLite", "Total rows are:   2", "Printing each row", sep="\n")
    # for row in rows:
    #     if row[0] == 3004 and row[1] == "Fabian Johns" and row[2] == "Paris" and row[3] == 300 and row[4] == 5006:
    #         print(f"Id:  {row[0]} \nName:  {row[1]} \nCity:  {row[2]} \nGrade:  {row[3]} \nSeller:  {row[4]}")
    # print("", "", sep="\n")
    # for row in rows:
    #     if row[0] == 3008 and row[1] == "Julian Green" and row[2] == "London" and row[3] == 300 and row[4] == 5002:
    #         print(f"Id:  {row[0]} \nName:  {row[1]} \nCity:  {row[2]} \nGrade:  {row[3]} \nSeller:  {row[4]}")

cur.close()
con.close()

# print("", "", sep="\n")
print("The SQLite connection is closed")
