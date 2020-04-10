from database import QuipsDB, InitDB
from quip import Quip

db = QuipsDB()

# db.add_quip(Quip('hi'))

# print(db.get_all_quip_ids())

InitDB(reset=True)

first_quip = Quip('first quip!')

print(db.add_quip(first_quip))

# print(db.get_random_child(13))