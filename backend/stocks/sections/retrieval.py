import json
from bson import json_util
from pymongo import MongoClient, errors
import numbers

client = MongoClient('localhost', 27017)
db = client.market
collection = db.stocks

def find_SMA_50(low, high):
    """
    Counts documents where their 50-Day Simple Moving Average is between high
    and low.

    @params: Number low, Number high

    @return: JSON { "count": count } or { "Error": e }
    """
    result = {}
    if not (isinstance(low, numbers.Number)):
        result = { "Error": "First parameter is not a number!"}
    if not (isinstance(high, numbers.Number)):
        result = { "Error": "Second parameter is not a number!"}

    # Let's just exit out of this if any paramter is not a number.
    if "Error" in result:
        return result

    # I think the rubric wants us to specifically use find instead of
    # aggregates, so I'll do that.

    try:
        searchFilter = {
            "50-Day Simple Moving Average": { "$gt": low, "$lt": high },
        }

        # Well, count() is supposedly deprecated. I'm just not going to use it.
        cursor = collection.find(searchFilter).explain()
        
        result = { "Count": cursor["n"] }

    except Exception as e:
        results = { "Error": ("%s" % e) }

    return result


def find_industry(industry):
    result = {}
    # Let's first make sure that we're getting a string:
    if not (isinstance(industry, str)):
        result = { "Error": "Parameter requires a string!" }
        # If it's not, lets just leave the function.
        return result

    try:
        searchFilter = { "Industry": industry }
        project = { "Ticker": 1 }

        cursor = collection.find(searchFilter, project)
        
        if not cursor.alive:
            result = { "Error": "No documents found." }
        
        tickers = []
        for doc in cursor:
            tickers.append(doc["Ticker"])

        result = { "Tickers": tickers }

    except Exception as e:
        result = { "Error": ("%s" % e) }
        
    return result

def find_outstanding_shares_by_sector(sector):
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
        # search = db.command("aggregate", "stocks", pipeline=pipeline, explain=True)
        
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
    return 1

main()