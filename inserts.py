import json
import requests
import pymongo

############## PART 1 - Insert One ######################

# establishing connection
connection = pymongo.MongoClient("mongodb://localhost")

# selecting on database
db = connection.wow

# selecting collection
last_url = db.last_url

# drop collection if exists
last_url.drop()

# get url from server
discover_ah = requests.get(
    "http://us.battle.net/api/wow/auction/data/goldrinn")
# parse the json into python dict
parsed = json.loads(discover_ah.content.decode('utf-8'))

# Insert one \o/
result = last_url.insert_one(parsed)
print("Inserted id: ", result.inserted_id)

############## PART 2 - Insert Many ######################

# selecting collection
ah_items = db.ah_items

# drop collection if exists
ah_items.drop()

# get url from server
ah_url = parsed.get("files")[0].get("url")
all_items_ah = requests.get(ah_url)

# parse the json into python dict
parsed = json.loads(all_items_ah.content.decode('utf-8'))

# qty of auctions
print("Qty Auctions: ", len(parsed.get("auctions")))

from time import time
start = time()
# Insert many \o/
result = ah_items.insert_many(parsed.get("auctions"))
print("Finish: ", time() - start)
print("Inserted {} new ids".format(len(result.inserted_ids)))
