import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")




c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
    {'first': "John", 'last': "Dos", 'pay': "54455"})

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
    {'first': "John", 'last': "Dos", 'pay': "544255"})

c.execute("SELECT * FROM employees WHERE last=:last", {'last': "Dos"})
print(c.fetchall())


conn.close()
#https://api.barcodespider.com/v1/lookup?upc=649528905765&&token=441d95fefd9720c9a560