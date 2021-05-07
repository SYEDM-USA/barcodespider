import os
import sqlite3


#Connect to the database
conn = sqlite3.connect('prices.db')

#Create a cursor
cur = conn.cursor()

#
#cur.execute("""CREATE TABLE UPCPRICE (
#                title text,
#                upc text,
#                price text,
#                currency text
#            )""")

#cur.execute("INSERT INTO UPCPRICE VALUES ('test thingy', '123456789', '50.00', 'USD')")

title = "aero"
upc = "123456"
price = "34.78"
currency = "USD"

#cur.execute("INSERT INTO UPCPRICE VALUES ('{}', '{}', '{}', '{}')".format(title,upc,price,currency))

conn.commit()


x = str(input("Enter UPC code: "))

def get_by_upc(myupc):
    cur.execute("SELECT * FROM UPCPRICE WHERE upc=:myupc",{'myupc':myupc})
    return cur.fetchall()

print(get_by_upc(x))

conn.close()