import json
from bson import json_util
from pymongo import MongoClient, errors
import numbers
import pprint
from datetime import datetime

pp = pprint.PrettyPrinter(indent = 2)

client = MongoClient('localhost', 27017)
db = client.market
collection = db.stocks

def read_file(path):
    """
    Will read a file using a string path.
    """
    if not (isinstance(path, str)):
        return "Error: Path must be a string!"

    s = ""
    try:
        f = open(path, "r")  # Read from file.
        s = f.read()         # This should be a string.
        f.close()            # We no longer need the file.
    except Exception as e:
        s = ("Error: %s" % e)

    return s

def load_json(s):
    """
    Will return the string as a formatted dictionary or list via JSON.
    """
    return json.loads(s)

def transform_document(query):
    # Again, gotta hardcode this. I don't want to change the curl because I'm
    # expecting something similar to stocks.json to be requested.
    # Note: I'm opting to not copy the query into here. Just seems like a
    #       waste to make another object when we're only transforming one k,v
    #       pair.
    
    # Might as well check all this. If earnings date isn't even in the query, 
    # just leave the function.
    if "Earnings Date" in query:
        # Because we're getting "$date" as a key as well, we should remove it
        # completely by replacing it with an ISO formatted date.
        if "$date" in query["Earnings Date"]:
            time = query["Earnings Date"]["$date"]
            # This needs to be divided by 1000 because JS returns the timestamp in ms,
            # while datetime expects the timestamp in seconds.
            query["Earnings Date"] = datetime.fromtimestamp(time / 1000)

def insert_documents(data):
    """
    This will insert documents from our file into the collection.
    Note: All the documents have "status": "test" as a kv pair, so it should
          make removing them easy.
    """
    docs = []
    result = { "Error": "Must be a dict or list!" }

    if isinstance(data, dict):
        docs.append(data)
    elif isinstance(data, list):
        # I won't go much into type checking, but this could fail if we get a
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

def find_document(search):
    """
    Using this to find documents to verify that other methods work.
    """
    if not isinstance(search, dict):
        return { "Error": "Search criteria must be in a dictionary!" }

    try:
        result = collection.find_one(search)
        
    except Exception as e:
        result = { "Error": ("%s" % e) }

    return result

def update_document(search, data):
    """
    This will take a dict search and dict data, then will update the correct
    document in the db with data.
    Note: I'll just make this update one.
    """
    if not isinstance(search, dict):
        return { "Error": "First parameter must be a dictionary." }
    if not isinstance(data, dict):
        return { "Error": "Second parameter must be a dictionary." }

    try:
        # If I use find_one_and_update, then it will automatically return
        # the document as it was before the update. This would make comparing
        # the before and after documents much easier.
        result = collection.find_one_and_update(search, { "$set": data })
        
    except Exception as e:
        result = { "Error": ("%s" % e) }

    return result

def delete_documents(search):
    """
    The rubric says to delete *documents* instead of document, so I think I'll
    use the delete_many function.
    """
    # Again, we must type check:
    if not isinstance(search, dict):
        return { "Error": "Search critera must be a dictionary." }

    try:
        result = collection.delete_many(search).raw_result

    except Exception as e:
        result = { "Error": ("%s" % e) }

    return result

# Of course, I'm not sure how strict the rubric will be for this. While in 
# practice we can use the above functions for anything the rubric is asking,
# I feel it's better to make it explicitly clear that this is exactly what
# it's looking for. The next few functions will do just that:

# insert_document is already created exactly as the rubric states.

def update_volume(ticker, volume):
    """
    This function will look for a ticker then update its volume.
    """
    search = { "Ticker": ticker }
    volume = { "Volume": volume }

    return update_document(search, volume)

def delete_by_ticker(ticker):
    """
    This function will look for a specific ticker, then delete all of them.
    """
    search = { "Ticker": ticker }
    return delete_documents(search)

def main():
    # data = json.loads(read_file("data.json"))
    return 1

main()