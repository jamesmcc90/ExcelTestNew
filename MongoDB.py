from pymongo import MongoClient
import csv
import codecs

mongo_client = MongoClient("mongodb+srv://james:McConnell%401990@sandbox.1iqe7.mongodb.net/test?authSource=admin&replicaSet=atlas-u2rtn2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")

db = mongo_client.sample_airbnb
col = db.listingsAndReviews
cursor = col.find()

with codecs.open('C:\\Users\\James\\Desktop\\test.csv', 'w', 'utf-8') as csvfile:
    columns = ["Name", "Summary"]
    writer = csv.writer(csvfile)
    writer.writerows("")
    writer.writerow(columns)

    for data in cursor:

        writer.writerows([[data["name"],
                           data["summary"]
                           ]])
