import json
from bson import json_util
import bottle
from bottle import hook, route, run, request, error, response, Bottle
from datetime import datetime

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from api import api

# OPTIMIZATION: Enable CORS because we're running the server off the same
#               computer as the Angular server. In production, the DB would be
#               on a different instance than the client server.
_allow_origin = '*'
_allow_methods = 'PUT, GET, POST, DELETE, OPTIONS'
_allow_headers = 'Authorization, Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

print("Server is running...\n")
# app = Bottle()
app = bottle.app()

def set_headers(response):
    response.set_header('Access-Control-Allow-Origin', _allow_origin)
    response.set_header('Access-Control-Allow-Methods', _allow_methods)
    response.set_header('Access-Control-Allow-Headers', _allow_headers)
    return response

# Helper to print errors:
def print_error(e):
    print("Error: ", e)

# Another helper to return JSON:
def get_json(document):
    return json.loads(json.dumps(document, indent=4, default=json_util.default))

# And one more helper to remove unnecessary apostrophes:
def transform_document(query):
    # Again, gotta hardcode this. I don't want to change the curl because I'm
    # expecting something similar to stocks.json to be requested.
    # Note: I'm opting to not copy the query into here. Just seems like a
    #       waste to make another object when we're only transforming one k,v
    #       pair.
    # data = query

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

    # return data

@app.route("/stocks/api/v1.0/createStock/<symbol>", method="POST")
def create(symbol = ""):
    """
    Adds a document to the collection.

    @params: Symbol from route, JSON payload.

    @return: JSON of created document or error.

    @h_resp: 201 Created, 400 Bad Request makes sense to me as well.
    """
    status = 200
    try:
        res = { "Ticker": symbol }
        # data = request.json

        # This needs to be done. I need to convert the date from UNIX Epoch
        # to ISODate.
        # req = transform_document(request.json)
        req = request.json
        transform_document(req)

        # Neato, I found this .update() method that'll join my data:
        res.update(req)
        
        result = api.insert_documents(res)

        if "ids" in result:
            status = 201

        else:
            status = 400
            res = { "Error 400": "Document wasn't inserted!" }

        return bottle.HTTPResponse(status = status, body = get_json(res))

    except Exception as e:
        print_error(e)

@app.route("/stocks/api/v1.0/getStock/<symbol>", method="GET")
def read(symbol = ""):
    """
    Reads a document from the collection.

    @params: Query string from URL.

    @return: JSON of first found document or error.

    @h_resp: 200 OK, 404 Not Found
    """
    status = 200
    try:
        # read_document sends the whole cursor, let's just retrieve the first
        # document in the queue for now.
        res = next(api.read_document({ "Ticker": symbol }))

        # read_document returns a hardcoded error if a document isn't found,
        # so I'll look for it here:
        if "Error" in res:
            status = 404

        return bottle.HTTPResponse(status = status, body = get_json(res))
    
    except Exception as e:
        print_error(e)

@app.route("/stocks/api/v1.0/updateStock/<symbol>", method="PUT")
def update(symbol = ""):
    """
    Updates a document with given parameters

    @params: Symbol from route, JSON payload
    
    @return: JSON of updated document or error.
    
    @http_res: 200 OK, 404 Not Found, 201 Created
    """
    status = 200
    try:
        req = request.json
        transform_document(req)  # If there's a date, it'll get fixed.
        
        res = api.update_document("Ticker", symbol, req)

        # First, check for errors:
        if "Error" in res:
            status = 400
            
        # If there isn't an error, then check if there was an upsert:
        if "upserted" in res:
            status = 201
    
    except Exception as e:
        print_error(e)

    return bottle.HTTPResponse(status = status, body = get_json(res))

# @app.route("/stocks/api/v1.0/deleteStock/<symbol>", method="GET")
@app.route("/stocks/api/v1.0/deleteStock/<symbol>", method="DELETE")
def delete(symbol = ""):
    """
    Deletes a document with given parameters

    @params: Symbol from route.
    
    @return: I guess the JSON object that was deleted.
    
    @h_resp: 200 OK, 404 Not Found
    """
    status = 200
    try:
        req = { "Ticker": symbol }
        res = api.delete_document(req)
        
        if "Error" in res:
            status = 404
            # Again, api is more descriptive, so I'll just send that error.
    
    except Exception as e:
        print_error(e)

    return bottle.HTTPResponse(status = status, body = get_json(res))

@app.route("/stocks/api/v1.0/allStocks", method=["OPTIONS", "GET"])
def get_all_stocks():
    """
    OPTIMIZATION:
    Get all stocks within the db, return as large JSON array. An aside, this
    will probably become a huge return, so it may be better to paginate this.
    
    @params: None

    @return: Array of all stocks in collection.
    """
    status = 200
    try:
        # We're sure to get a list from the JSON request, which will be an
        # array of all the stocks that we need to look through.
        data = {}
        stocks = []
        for doc in api.read_document({}):
            stocks.append(doc)

        data = { "Stocks": stocks }
        
    except Exception as e:
        status = 404
        data = { "Error: ": e }

    # So, this would work if I was just sending a JSON response. The problem is
    # I want to send an HTTPResponse. I can't find a better way to do this, so
    # I'll probably wrap setting headers in some utility function.

    # NOTE: Using @hook('after_request) doesn't seem to work unless, as
    #       mentioned above, I'm sending just a straight JSON response back.

    # return get_json(data)
    
    res = bottle.HTTPResponse(status = status, body = get_json(data))
    return set_headers(res)

    

@app.route("/stocks/api/v1.0/stockReport", method="POST")
def stock_report():
    """
    Select and present specific stock summary information.
    
    @params: JSON containing list.
    
    @return: Array containing all stocks found.
    
    @h_resp: 200 OK, 404 Not Found
    """
    status = 200

    try:
        # We're sure to get a list from the JSON request, which will be an
        # array of all the stocks that we need to look through.
        req = request.json["list"]
        
        data = {}
        stocks = []

        for stock in req:
            # There might be multiple responses:
            for doc in api.read_document({ "Ticker": stock }):
                # Let's append every single doc in the cursor.
                stocks.append(doc)
            
        data = { "Stocks": stocks }
    
    except Exception as e:
        status = 404
        data = { "Error: ": e }
    
    res = bottle.HTTPResponse(status = status, body = get_json(data))
    return set_headers(res)


@app.route("/stocks/api/v1.0/industryReport/<industry>", method="GET")
def industry_report(industry = ""):
    """
    Report a portfolio of five top stocks by industry.
    
    @params: Industry from route.
    
    @return: Array containing top 5 stocks by industry. Note: I'm not sure how to
             arrange this, so I'll assume it means top five found, not top five
             in some metric.
    
    @h_resp: 200 OK, 404 Not Found
    """
    status = 200
    try:
        res = api.find_industry(industry)
        
        if "Error" in res:
            status = 404
        else:
            res = { "Tickers": res["Tickers"][:5] }

    except Exception as e:
        status = 404
        print_error("e")
        
    return bottle.HTTPResponse(status = status, body = get_json(res))

@app.route("/stocks/api/v1.0/portfolio/<company>", method="GET")
def portfolio(company = ""):
    """
    Retrieves all stocks under one company
    
    @params: Company from route.
    
    @return: JSON payload with a list of stocks.
    
    @h_resp: 200 OK, 404 Not Found
    """
    status = 200
    try:
        res = { "Company": company }
        
        data = api.read_document(res)

    except Exception as e:
        print_error(e)
        
    return bottle.HTTPResponse(status = status, body = get_json(res))

if __name__ == "__main__":
    run(app, host="localhost", port=8080)