import pymongo

# establishing connection
connection = pymongo.MongoClient("mongodb://localhost")
# selecting on database
db = connection.wow
# selecting collection
ah_items = db.ah_items

# update all the docs
from time import time
start = time()
result = ah_items.delete_many({'good_gem': {"$ne": True}})
print("Finish: ", time() - start)
print("Deleted count: ", result.deleted_count)
