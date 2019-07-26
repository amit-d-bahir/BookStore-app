import sqlite3

class Database :


    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        """
        This id is different from IdNo
        id is auto incremented and is used to keep track of total number of books
        It also helps us further in a lot of operations being the PRIMARY KEY...
        """
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, author TEXT, year INTEGER, IdNo INTEGER)")
        self.conn.commit()

    def insert(self, title, author, year, IdNo):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, IdNo))
        # NULL ensures that id is also given and it auto increments it
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        data = self.cur.fetchall()  # return a list of tuples
        return data

    def search(self, title="", author="", year="", IdNo=""):
        # We'vw initialized them to "" as we want to prevent error when only
        # some of the parameters are given as arguments
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR IdNo=?", (title,author,year,IdNo))
        data = self.cur.fetchall()
        # print (data)
        return data


    def delete(self, id):
        """
        This is a bit tricky
        As we need to grab the entry from the ListBox as a tuple
        And then we identify it according to the id and then refer to it in
        the database and thereby deleting it, so the parameter is only id
        """
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, IdNo):
        """
        The user selects an entry from ListBox and we would want to display the
        info in the entry widgets and from there user as required would want to
        update any of the cells by pressing the 'update' button.
        """
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, IdNo = ? WHERE id = ?", (title, author, year, IdNo, id))
        self.conn.commit()

    """
    But we have got a problem here
    which is that our database is now open as we have not
    closed it anywhere in our script
    So, to solve this problem we use __del__
    Which deletes the object when we close it i.e the window of our app
    and which also closes the database
    """

    def __del__(self):
        self.conn.close()
