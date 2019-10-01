import json
from bson import json_util
from pymongo import MongoClient, errors
import numbers

DEBUG = False
dbName = ""
colName = ""

# Notes: Might be a good idea to create few models for our 'production' db.
#        This way, we can ensure that the data being inserted into our db
#        matches the format that we want. From the rubric, this doesn't look
#        completely necessary right now though. 


# Supposedly MongoClient constructor won't raise ConnectionFailure or 
# ConfigurationError anymore. More info in the reference:
# https://api.mongodb.com/python/current/api/pymongo/mongo_client.html

client = MongoClient('localhost', 27017)

if DEBUG:
    db = client.db
    dbName = "db"
    collection = db.col
    colName = "col"
else:
    db = client.market
    dbName = "market"
    collection = db.stocks
    colName = "stocks"

# print_docs(Cursor docs)
# @params: Cursor document
# @return: void
# @_nodes: Just a helper method that prints all the documents
#         output by read_document
def print_docs(docs):
    for doc in docs:
        print(doc)

def insert_documents(data):
    """
    Will insert documents into the picked collection.
    
    @params: dictionary or array

    @return: { "ids": [...ids] }
    """
    
    docs = []
    result = { "Error": "Must be a dict or list!" }

    if isinstance(data, dict):
        docs.append(data)
    elif isinstance(data, list):
        # I won't go much into type checking, but this could fail if we get 
        # list and it's not full of dictionaries.
        docs = data

    # Since we're not using d, this won't even be tried...I don't think.
    try:
        res = collection.insert_many(docs)
        # If the list is empty, this will throw an exception and the method
        # will return.
        ids = []
        for data in res.inserted_ids:
            ids.append(data)

        result = { "ids": ids }
        
    except Exception as e:
        result = { "Error": ("%s" % e) }
            
    return result
    
def read_document(k, v = None):
    """
    Will find documents in the db using k, v or a dictionary.

    @params: { k, v } or dictionary

    @return: Cursor
    """
    try:
        docsFound = 0
        if v is None:
            results = collection.find(k)    
        else:
            results = collection.find({ k : v })
            
        docsFound = results.count()
    
        if docsFound < 1:
            error = [{ "Error": "No documents found!", "alive": False }]
            results = iter(error)

    except Exception as e:
        results = iter([{ "Error": ("%s" % e), "alive": False }])

    return results

# update_document(string lk, Type lv, Dict document)
# Will update a single document (rubric says 'a document' not documents).
# @params: k, v, document # lookup key and value, and replacing document
# @return: JSON of insert, else Mongo error     
def update_document(k, v, document = None):
    """
    Will update a single document, can upsert if necessary.

    @params: { k, v } or document and data for update

    @return: JSON of insert or MongoDB error.
    """
    if document is None:
        doc = k
        document = v
    else:
        doc = { k: v }
        
    try:
        # Leaving this as update_one() because we're interested in upserting
        # as well. find_one_and_update() requires, well, to find one.
        update = collection.update_one(
            doc,
            { "$set" : document },
            upsert = True
        )

        result = next(read_document(k, v))

        # We'll attach some diagnostics into the payload going back to the
        # client.
        if update.upserted_id:
            result.update({ "upserted": True })

    # I tried the abort() method like you suggested, but ultimately I was
    # thinking that the server should take care of HTTP error responses,
    # while this API should only concern itself with contacting the db.
    # I'm not sure which is faster, but this *feels* like a best practice.
    except Exception as e:
        result = { "Error": ("%s" % e) }
        
    return result

def delete_document(k, v = None):
    """
    Will only delete the first document found.

    @params: { k, v } or dictionary

    @return: JSON of deleted document or MongoDB error.
    """
    try:
        cursor = read_document(k, v)

        result = next(cursor)

        # May need this for diagnostic, not sure:
        response = collection.delete_one({ "_id": result["_id"] })
        
    except Exception as e:
        result = { "Error": ("%s" % e) }
    
    return result

# _Notes: For the next few functions, we'll largely be using aggregation via
#         PyMongo. I don't think it's necessary to create an aggregation method
#         because I'll end up passing in a pipline anyway, and it's just a
#         single call to PyMongo. If I have extra time, I'll refactor/optimize
#         where I can; but being honest, I don't think it'll be here.
# Update: I suppose I could write a generic aggregation method, but the problem
#         will be $group and $project. I'll keep it this way for now.

def find_SMA_50(low, high):
    """
    Will return the number of stocks that exist between two numbers.

    @params: low, high
    
    @return: Count of stocks found in JSON. Note: It's going to be in JSON
             because I want to return errors as well, if the parameters aren't
             numbers.
    """
    result = {}
    if not (isinstance(low, numbers.Number)):
        result = { "Error": "First parameter is not a number!"}
    if not (isinstance(high, numbers.Number)):
        result = { "Error": "Second parameter is not a number!"}

    # Let's just exit out of this if any paramter is not a number.
    if "Error" in result:
        return result

    # Okay, so assuming low and high are both numbers, we should then search
    # for all documents with "50-Day Simple Moving Average" valued between
    # high and low. Let's use an aggregation pipeline for this.
    pipeline = [
        {
            "$project": {
                "_id": 0,
                "Ticker": 1,
                "50-Day Simple Moving Average": 1
            }
        },
        {
            "$match": {
                "50-Day Simple Moving Average": {
                    "$gt": low,
                    "$lt": high
                }
            }
        },
        {
            "$group": {
                "_id": "null",
                "count": { "$sum": 1 }
            }
        }
    ]

    try:
        search = collection.aggregate(pipeline)
        if search.alive:
            result = { "Count": next(search)["count"] }
        else:
            result = { "Error": "No documents found." }

    except Exception as e:
        result = { "Error": ("%s" % e) }

    return result

def find_industry(industry):
    """
    Will return a list of ticker symbols within an industry.
    
    @params: industry
    
    @return: Array of all tickers in the industry.
    """
    result = {}
    # Let's first make sure that we're getting a string:
    if not (isinstance(industry, str)):
        result = { "Error": "Parameter requires a string!" }
        # If it's not, lets just leave the function.
        return result

    # Now that we know we have a string, let's put together a list of tickers
    # that reside within the industry. We'll use the aggregation framework
    # again.
    pipeline = [
        {
            "$project": {
            "_id": 0,
            "Ticker": 1,
            "Industry": 1
            }
        },
        {
            "$match": {
            "Industry": industry
            }
        },
        {
            "$group": {
            "_id": "null",
            "Tickers": { "$push": "$Ticker" }
            }
        }
    ]

    try:
        result = collection.aggregate(pipeline)
        if not result.alive:
            result = iter([{ "Error": "No documents found." }])

    except Exception as e:
        result = iter([{ "Error": ("%s" % e) }])
        
    return next(result)
    
def find_outstanding_shares_by_sector(sector):
    """
    Find the outstanding shares for a sector grouped by industry.
    
    @params: sector
    
    @return: List with JSON objects
    """
    result = {}

    if not (isinstance(sector, str)):
        result = { "Error": "Parameter requires a string!" }
        # If it's not, lets just leave the function.
        return result

    pipeline = [
        {
            "$project": {
            "_id": 0,
            "Sector": 1,
            "Industry": 1,
            "Shares Outstanding": 1
            }
        },
        {
            "$match": {
            "Sector": sector
            }
        },
        {
            "$group": {
                "_id": "$Industry",
                "Total Outstanding Shares": { "$sum": "$Shares Outstanding" }
            }
        }
    ]

    try:
        search = collection.aggregate(pipeline)

        # I'm a little conflicted; I could just return the entire cursor or an
        # error if the cursor isn't alive (i.e. if !search.alive), but maybe a
        # single list will be better. Or maybe it would be better if I built a
        # dictionary using industry as the key and shares as the value. Idk. 
        # I'll do it as a list for now.

        docs = []

        if not search.alive:
            result = { "Error": "No industries found!" }
        else:
            for doc in search:
                docs.append(doc)

            result = { "shares": docs }

    except Exception as e:
        result = { "Error: ": e }

    return result

def main():
    if DEBUG:
        print("---- WARNING!: IN DEBUG MODE ----")
        print("-- COLLECTION WILL BE DROPPED! --\n")
        # collection.drop()

    print("        DB: %s" % dbName)
    print("Collection: %s\n" % colName)

main()