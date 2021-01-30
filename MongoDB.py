from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://james:McConnell%401990@sandbox.1iqe7.mongodb.net/test?authSource=admin&replicaSet=atlas-u2rtn2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db = client.james
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)
