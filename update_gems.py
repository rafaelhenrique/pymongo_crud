import pymongo
good_gems = [76692, 76693, 76694, 76695, 76696, 76636, 76637, 76638, 76639,
             76697, 76698, 76699, 76700, 76701, 76680, 76681, 76682, 76683,
             76684, 76685, 76686, 76687, 76688, 76689, 76690, 76691, 89674,
             89680, 76640, 76641, 76642, 76643, 76644, 76645, 76646, 76647,
             76648, 76649, 76650, 76651, 76652, 76653, 76654, 76655, 76656,
             76657, 93705, 76658, 76659, 76660, 76661, 76662, 76663, 76664]

# establishing connection
connection = pymongo.MongoClient("mongodb://localhost")
# selecting on database
db = connection.wow
# selecting collection
ah_items = db.ah_items

# update all the docs
from time import time
start = time()
result = ah_items.update_many(
    {'item': {"$in": good_gems}},
    {'$set': {'good_gem': True}}
)
print("Finish: ", time() - start)
print("Matched count: ", result.matched_count)
print("Modified count: ", result.modified_count)
