from database import QuipsDB, InitDB

db = QuipsDB()

print([list(db.get_quip(-1)) for i in range(6)])

