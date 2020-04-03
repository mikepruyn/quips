import sqlite3

class InitDB:
    def __init__(self):
        self.conn = sqlite3.connect('quips.db')
        self.init_db()

    def init_db(self):
        query = '''CREATE TABLE IF NOT EXISTS 'Quips'(
            id INTEGER PRIMARY KEY,
            text TEXT,
            parent INTEGER)'''
        self.conn.execute(query)
        self.conn.commit()

class QuipsDB:
    def __init__(self):
        self.conn = sqlite3.connect('quips.db')

    def add_quip(self, text, parent):
        query = f'INSERT INTO Quips ' \
                f'(text, parent) ' \
                f'VALUES ("{text}","{parent}")'
        self.conn.execute(query)
        self.conn.commit()


    def get_quip(self, parent):
        query = f'SELECT * FROM Quips ' \
                f'WHERE parent == "{parent}" ' \
                f'ORDER BY RANDOM() LIMIT 1;'
        return self.conn.execute(query)



