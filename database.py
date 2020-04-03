import sqlite3

class InitDB:
    def __init__(self, reset=False):
        self.conn = sqlite3.connect('quips.db')
        if reset:
            self.conn.execute('''DROP TABLE "Quips"''')
            self.conn.commit()

        self.init_db()

    def init_db(self):
        query = '''CREATE TABLE IF NOT EXISTS 'Quips'(
            id INTEGER PRIMARY KEY,
            text TEXT,
            parent INTEGER)'''
        self.conn.execute(query)
        self.conn.commit()

    def reset_db(self):
        
        self.init_db()

class QuipsDB:
    def __init__(self):
        self.conn = sqlite3.connect('quips.db')

    def add_quip(self, quip):
        query = f'INSERT INTO Quips ' \
                f'(text, parent) ' \
                f'VALUES ("{quip.text}","{quip.parent}")'
        self.conn.execute(query)
        self.conn.commit()


    def get_quip(self, parent_id):
        query = f'SELECT * FROM Quips ' \
                f'WHERE parent == "{parent_id}" ' \
                f'ORDER BY RANDOM() LIMIT 1;'
        return self.conn.execute(query)



