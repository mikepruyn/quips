from database import QuipsDB

db = QuipsDB()

db.add_quip('hi', 1)
db.add_quip('hello', 1)
db.add_quip('hiya', 2)
db.add_quip('helloya', 2)

print(list(db.get_quip(2)))

