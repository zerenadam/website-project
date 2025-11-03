import sqlite3


class Database:


    def __init__(self):

        self.connection = sqlite3.connect("lost.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS items(id, desc, date, user)")


    def add_item(self):
        pass

    
