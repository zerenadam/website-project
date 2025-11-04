import sqlite3

class Database:

    
    def __init__(self):

        self.connection = sqlite3.connect("lost.db")
        self.cursor = self.connection.cursor()


        self.cursor.execute("""CREATE TABLE IF NOT EXISTS items (
                            
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            item TEXT NOT NULL,
                            description TEXT NOT NULL,
                            date TEXT NOT NULL,
                            user TEXT NOT NULL
                            )""")
        self.connection.commit()

    
    def add_item(self, item, description, date, user):

        self.cursor.execute("INSERT INTO items(item, description, date, user) VALUES (?, ?, ?, ?)",
                            (item, description, date, user)
                            )
        self.connection.commit()

    
