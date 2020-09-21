import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title varchar(100) ,author varchar(100) , "
            "isbn INTEGER , year INTEGER )")
        self.conn.commit()

    def insert(self, title, author, isbn, year):
        self.cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title, author, isbn, year))
        self.conn.commit()

    def view(self):
        self.cursor.execute("SELECT * FROM book")
        rows = self.cursor.fetchall()
        self.conn.commit()
        return rows

    def view_entry(self, isbn="", author="", title="", year=""):
        self.cursor.execute("SELECT * FROM book WHERE isbn = ? OR title= ? OR year = ? OR author = ?",
                            (isbn, title, year, author))
        rows = self.cursor.fetchall()
        self.conn.commit()
        return rows

    def update(self, title, author, isbn, year):
        self.cursor.execute("UPDATE book SET title = ?,author = ? ,year = ?  WHERE isbn = ?",
                            (title, author, year, isbn))
        self.conn.commit()

    def delete_selected(self, isbn):
        self.cursor.execute("DELETE FROM book WHERE isbn = ?", (isbn,))
        self.conn.commit()

    def delete(self):
        self.cursor.execute("DELETE FROM book")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# insert("try this one for size", "JHC", 23132, 2008)
# delete()
# update("Hunt for The red october", "TC", 365455, 2008)
