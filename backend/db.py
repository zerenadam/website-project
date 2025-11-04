import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect("lost.db")
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()

        # create items table 

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS items (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            item_name TEXT NOT NULL,
                            description TEXT,
                            date_reported TEXT NOT NULL,
                            reporter_name TEXT,
                            email TEXT NOT NULL,
                            photo_path TEXT,
                            status TEXT DEFAULT 'pending'
                            )""")
        
        # create claims table

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS claims (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            item_id INTEGER NOT NULL,
                            student_name TEXT NOT NULL,
                            student_email TEXT NOT NULL,
                            message TEXT,
                            status TEXT DEFAULT 'pending',
                            FOREIGN KEY(item_id) REFERENCES items(id) ON DELETE CASCADE
                            )""")
        
        self.connection.commit()

    
    def add_item(self, item_name, description, date, name, email, photo_path):

        self.cursor.execute("INSERT INTO items (item_name, description, date_reported, reporter_name, email, photo_path) VALUES (?, ?, ?, ?, ?, ?)",
                            (item_name, description, date, name, email, photo_path)
                            )
        self.connection.commit()

    def add_claim(self, item_id, student_name, email, message):

        self.cursor.execute("INSERT INTO claims (item_id, student_name, student_email, message) VALUES (?, ?, ?, ?)",
                            (item_id, student_name, email, message)
                            )
        self.connection.commit()

    def approve_item(self, item_id):
        self.cursor.execute("UPDATE items SET status='approved' WHERE id=?", (item_id,))
        self.connection.commit()

    def approve_claim(self, claim_id):
        self.cursor.execute("UPDATE claims SET status='approved' WHERE id=?", (claim_id,))
        self.connection.commit()

    def get_items(self, approved_only=False):

        if approved_only:
            self.cursor.execute("SELECT * FROM items WHERE status='approved'")
        else:
            self.cursor.execute("SELECT * FROM items")
        return self.cursor.fetchall()
