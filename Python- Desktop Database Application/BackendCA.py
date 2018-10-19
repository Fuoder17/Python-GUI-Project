import sqlite3

def connect():

# Database is created with CAconn= sqlite3.connect("lite.db")
    CAconn = sqlite3.connect("Admitted_Students.db")
    cur = CAconn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Students ( id INTEGER PRIMARY KEY, firstname text, lastname text, email text, student_id integer)")
    CAconn.commit()
    CAconn.close()

# Add Entry Button
# A new connection is needed when the add entry button is clicked
def insert(firstname,lastname,email,student_id):
    CAconn = sqlite3.connect("Admitted_Students.db")
    cur = CAconn.cursor()
    # Tuple of the arguments passed (firstname,lastname,email,student_id)
    cur.execute("INSERT INTO Students VALUES (NULL,?,?,?,?)",(firstname,lastname,email,student_id))
    CAconn.commit()
    CAconn.close()
    view()
#View All Button
def view():
    CAconn = sqlite3.connect("Admitted_Students.db")
    cur = CAconn.cursor()
    cur.execute("SELECT * FROM Students")
    # All the value will be stored in the rows variable
    rows = cur.fetchall()
    CAconn.close()
    # This will allow the values to be returned
    return rows

#Search Entry Button
def search(firstname="",lastname="",email="",student_id=""):
    CAconn = sqlite3.connect("Admitted_Students.db")
    cur = CAconn.cursor()
    cur.execute("SELECT * FROM Students WHERE firstname=? OR lastname=? OR email=? OR student_id=?",(firstname,lastname,email,student_id))
    rows = cur.fetchall()
    CAconn.close()
    return rows

#Delete Selected Button
def delete(id):
    CAconn = sqlite3.connect("Admitted_Students.db")
    cur = CAconn.cursor()
    cur.execute("DELETE FROM Students WHERE id=?",(id,))
    CAconn.commit()
    CAconn.close()

#Update Selected Button
def update(id,firstname,lastname,email,student_id):
    CAconn = sqlite3.connect("Admitted_Students.db")
    cur = CAconn.cursor()
    cur.execute("UPDATE Students SET firstname=?,lastname=?,email=?,student_id=? WHERE id=?",(firstname,lastname,email,student_id,id))
    CAconn.commit()
    CAconn.close()

connect()
