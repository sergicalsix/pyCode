import sqlite3


#table
#c.execute("""CREATE TABLE customers (
 ## first_name text,
#    last_name text,
#    email text
 #   )    """)#docstring
#DATATYPE NULL INTEGER REAL TEXT BLOB music vedio

#c.execute("INSERT INTO customers VALUES('John', 'ELE','a@email.com')")
#many_customers = [
#("Wes","Brown","wes@brwon.com"),
#("Dan","Pas","Dan@pas.com")
#]
#c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)

## READ QUERY(order)

def show_all():
    #conn = sqlite3.connect(":memory:") #save data
    conn = sqlite3.connect("customer.db") #create db

    ##Create Table!!

    #cursor input object
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
#c.execute("SELECT * FROM customers WHERE last_name LIKE 'F%'"")
#c.execute("SELECT * FROM customers WHERE last_name = 'Pas'")
#c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

# Commit command
    conn.commit()

# Close connaction
    conn.close()

def add_one(first, last , mail):
    conn = sqlite3.connect("customer.db") #create db
    #cursor input object
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first),(last),(mail))
    
    