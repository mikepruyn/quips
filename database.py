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

        #returns the auto-generated primary key
        new_key = self.conn.execute('SELECT last_insert_rowid()')
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
        key, text, parent = self.conn.execute(query).fetchall()[0]   
        return Quip(text, parent, key)

    def get_any_quip(self):
        query = f'SELECT * FROM Quips ' \
                f'ORDER BY RANDOM() LIMIT 1;'
        key, text, parent = self.conn.execute(query).fetchall()[0]   
        return Quip(text, parent, key)

    def get_all_quip_ids(self):
        return [x[0] for x in list(self.conn.execute('SELECT id FROM Quips').fetchall())]



