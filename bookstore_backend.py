import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    """
    This id is different from IdNo
    id is auto incremented and is used to keep track of total number of books
    It also helps us further in a lot of operations being the PRIMARY KEY...
    """
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER, IdNo INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, IdNo):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, IdNo))
    # NULL ensures that id is also given and it auto increments it
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    data = cur.fetchall()  # return a list of tuples
    conn.close()
    return data

def search(title="", author="", year="", IdNo=""):
    # We'vw initialized them to "" as we want to prevent error when only
    # some of the parameters are given as arguments
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR IdNo=?", (title,author,year,IdNo))
    data = cur.fetchall()
    conn.close()
    return data


def delete(id):
    """
    This is a bit tricky
    As we need to grab the entry from the ListBox as a tuple
    And then we identify it according to the id and then refer to it in
    the database and thereby deleting it, so the parameter is only id
    """
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, IdNo):
    """
    The user selects an entry from ListBox and we would want to display the
    info in the entry widgets and from there user as required would want to
    update any of the cells by pressing the 'update' button.
    """
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, IdNo = ? WHERE id = ?", (title, author, year, IdNo, id))
    conn.commit()
    conn.close()

connect()
# A function call is made so as to ensure that table is created before any other
# operations when it's the first call and NOT EXISTS prevents the error...

# insert("vdsa","aamit", 1998, 23152112)
# print(view())
# print(search(year=1998))
# delete(3)
# update(2, "vssc","amit",2000, 321412312)
# print(search(year=2000))
# print(view())
