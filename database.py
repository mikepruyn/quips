import sqlite3
from quip import Quip

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

class QuipsDB:
    def __init__(self):
        self.conn = sqlite3.connect('quips.db')

    def add_quip(self, quip):
        query = f'INSERT INTO Quips ' \
                f'(text, parent) ' \
                f'VALUES ("{quip.text}","{quip.parent}")'
        self.conn.execute(query)
        self.conn.commit()

        #returns the auto-generated primary key(id)
        new_key = self.conn.execute('SELECT last_insert_rowid() FROM Quips').fetchall()[0][0]
        return new_key

    def get_quip(self, id):
        query = f'SELECT * FROM Quips ' \
                f'WHERE id == "{id}" ' \
                f'ORDER BY RANDOM() LIMIT 1;'
        key, text, parent = self.conn.execute(query).fetchall()[0]   
        return Quip(text, parent, key)


    def get_random_child(self, parent_id):
        query = f'SELECT * FROM Quips ' \
                f'WHERE parent == "{parent_id}" ' \
                f'ORDER BY RANDOM() LIMIT 1;'
        result = self.conn.execute(query).fetchall()
        if len(result) == 0:
            return -1

        key, text, parent = result[0]   
        return Quip(text, parent, key)

    def has_child(self, quip):
        query = f'SELECT * FROM Quips ' \
                f'WHERE parent == "{quip.id}" '
        result = self.conn.execute(query).fetchall()
        return len(result) > 0
            

   



