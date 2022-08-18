
# Create a Python program to use the sqlite database named "q1.db". The query to the database should display information, as shown in the example below, including phrases: about the successful connection, the total number of records, the actual records, the record of closing the database. From the table of "customers" to deduce all records for which in a "grade" field of value more than 200 with sort ordering on id



# For example output:

# Connected to SQLite
# Total rows are:   2
# Printing each row
# Id:  3022
# Name:  Nik Rimando
# City:  Madrid
# Grade:  1000
# Seller:  6001


# Id:  3025
# Name:  Grem Zusisa
# City:  USA
# Grade:  2000
# Seller:  6002


# The SQLite connection is closed


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
        print("", "", sep="\n")
except sqlite3.Error as e:
    print('ERROR') # \n
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
