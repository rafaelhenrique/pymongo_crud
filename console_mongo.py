import pymongo
# establishing connection
connection = pymongo.MongoClient("mongodb://localhost")
# selecting on database
db = connection.wow
# selecting collection
ah_items = db.ah_items
import ipdb
ipdb.set_trace()

# On Python:
# ipdb> ah_items.count()
# 41143
# ipdb> ah_items.count({'good_gem': True})
# 87
# ipdb> ah_items.count({'good_gem': {"$ne": True}})
# 41056

# On MongoDB:
# > db.ah_items.count()
# 41143
# > db.ah_items.find({good_gem: true}).count()
# 87
# > db.ah_items.find({good_gem: {$ne: true} }).count()
# 41056
