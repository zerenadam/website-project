import sqlite3

class Database:


    def __init__(self):

        self.connection = sqlite3.connect("lost.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

        # main table w items
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT NOT NULL,
                description TEXT NOT NULL,
                date TEXT NOT NULL,
                user TEXT NOT NULL,
                photo_path TEXT,
                approved INTEGER DEFAULT 0
            )
        """)

        # claims table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS claims (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_id INTEGER,
                student_name TEXT NOT NULL,
                message TEXT,
                FOREIGN KEY(item_id) REFERENCES items(id)
            )
        """)
        self.connection.commit()



    def add_item(self, item, description, date, user, photo_path=None):
        self.cursor.execute("""
            INSERT INTO items (item, description, date, user, photo_path)
            VALUES (?, ?, ?, ?, ?)
        """, (item, description, date, user, photo_path))
        self.connection.commit()

 
    def get_items(self, search_term=""):
        term = f"%{search_term}%"
        self.cursor.execute("""
            SELECT id, item, description, date, user, photo_path
            FROM items
            WHERE approved=1 AND (item LIKE ? OR description LIKE ?)
            ORDER BY id DESC
        """, (term, term))
        return self.cursor.fetchall()

 
    def add_claim(self, item_id, student_name, message):
        self.cursor.execute("""
            INSERT INTO claims (item_id, student_name, message)
            VALUES (?, ?, ?)
        """, (item_id, student_name, message))
        self.connection.commit()


    def get_all_items(self):
        self.cursor.execute("SELECT * FROM items ORDER BY id DESC")
        return self.cursor.fetchall()


    def approve_item(self, item_id):
        self.cursor.execute("UPDATE items SET approved=1 WHERE id=?", (item_id,))
        self.connection.commit()

