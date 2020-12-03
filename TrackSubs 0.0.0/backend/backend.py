import sqlite3


def drop():
    conn=sqlite3.connect("subscription.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE Subscriptions")
    conn.commit()
    conn.close()


def create():
    conn=sqlite3.connect("subscription.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Subscriptions (id INTEGER PRIMARY KEY, service TEXT UNIQUE, type TEXT, amount REAL, status TEXT, start_date DATE, renew_date DATE)")
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("subscription.db")
    cur=conn.cursor()  
    cur.execute("SELECT * from Subscriptions ORDER BY id")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def search(service="", type="", amount="", status="", start_date="", renew_date=""):
    sqlins= "SELECT * FROM Subscriptions WHERE service=? OR type=? OR amount=? OR status=? OR start_date=? OR renew_date=?"
    conn=sqlite3.connect("subscription.db")
    cur=conn.cursor() 
    cur.execute(sqlins, (service, type, amount, status, start_date, renew_date))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def insert(service, type, amount, status, start_date, renew_date):
    sqlins="INSERT INTO Subscriptions VALUES (NULL, ?, ?, ?, ?, ?, ?)"
    conn=sqlite3.connect("subscription.db")
    cur=conn.cursor()
    cur.execute(sqlins, (service, type, amount, status, start_date, renew_date))
    conn.commit()
    conn.close()

def update(id, service, type, amount, status, start_date, renew_date):
    conn=sqlite3.connect("subscription.db")
    cur=conn.cursor()
    cur.execute("UPDATE Subscriptions SET service=?, type=?, amount=?, status=?, start_date=?, renew_date=? WHERE id=?", (service, type, amount, status, start_date, renew_date, id))
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect("subscription.db")
    cur=conn.cursor()   
    cur.execute("DELETE FROM Subscriptions WHERE id=?", (id,))
    conn.commit()
    conn.close()



#drop()
create()
#insert("Netflix", "Monthly", "40.00", "Active", "1/10/2020", "1/11/2020")
#update(1, "FFXIV", "Monthly", "65.00", "Active", "19/10/2020", "20/11/2020")
#delete(2)
print(view())
#print(search(service="Netflix"))