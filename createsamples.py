from pymongo import MongoClient
from random import randint

client = MongoClient(
    "mongodb+srv://james:McConnell%401990@sandbox.1iqe7.mongodb.net/test?authSource=admin&replicaSet=atlas-u2rtn2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db = client.james

names = ['Kitchen', 'Animal', 'State', 'Taste', 'Big', 'City', 'Fish', 'Pizza', 'Goat', 'Salty', 'Sandwich', 'Lazy',
         'Fun']
company_type = ['LLC', 'Inc', 'Company', 'Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 11):
    business = {
        'name': names[randint(0, (len(names) - 1))] + ' ' + names[randint(0, (len(names) - 1))] + ' ' + company_type[
            randint(0, (len(company_type) - 1))],
        'rating': randint(1, 5),
        'cuisine': company_cuisine[randint(0, (len(company_cuisine) - 1))]
    }
    # insert one document into MongoDB
    result = db.reviews.insert_one(business)

    print('Created {0} of 10 as {1}'.format(x, result.inserted_id))
# Step 5: Tell us that you are done
print('finished creating 10 business reviews')

fivestarcount = db.reviews.count_documents({'rating': 3})
print(fivestarcount)

from pymongo import MongoClient

# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient(
    "mongodb+srv://james:McConnell%401990@sandbox.1iqe7.mongodb.net/test?authSource=admin&replicaSet=atlas-u2rtn2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
# Set the db object to point to the business database
db = client.james
# Showcasing the count() method of find, count the total number of 5 ratings
print('The number of 3 star reviews:')
fivestarcount = db.reviews.count_documents({"rating": 3})
print(fivestarcount)
# Now let's use the aggregation framework to sum the occurrence of each rating across the entire data set
print('\nThe sum of each rating occurrence across all data grouped by rating ')
stargroup = db.reviews.aggregate(
    # The Aggregation Pipeline is defined as an array of different operations
    [
        # The first stage in this pipe is to group data
        {'$group':
             {'_id': "$rating",
              "count":
                  {'$sum': 1}
              }
         },
        # The second stage in this pipe is to sort the data
        {"$sort": {"_id": 1}
         }
        # Close the array with the ] tag
    ])
# Print the result
for group in stargroup:
    print(group)

# james -> james.reviews (MongoDB Compass)
from pymongo import MongoClient
from pprint import pprint

client = MongoClient(
    "mongodb+srv://james:McConnell%401990@sandbox.1iqe7.mongodb.net/test?authSource=admin&replicaSet=atlas-u2rtn2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
db = client.business

ASingleReview = db.restaurants.find_one({})
print('A sample document:')
pprint(ASingleReview)

result = db.restaurants.delete_many({"rating": "1"})
