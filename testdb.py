from database import QuipsDB, InitDB
from quip import Quip

db = QuipsDB()

# db.add_quip(Quip('hi'))

print(db.get_all_quip_ids())