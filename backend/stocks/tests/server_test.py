import unittest
import json
from webtest import TestApp
from datetime import datetime

import sys, os  # Needed to import using relative path.
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# Not super happy about using this, but it works.

from server import server  # What we're testing.
from api import api        # For use in Takedown after tests are done.

app = TestApp(server.app)

"""
I'll leave these docs in here instead of reading from a file.
"""

# AA
doc1 = {
    "Profit Margin": 0.013,
    "status": "test",
    "Institutional Ownership": 0.599,
    "EPS growth past 5 years": -0.439,
    "Total Debt/Equity": 0.65,
    "Current Ratio": 1.2,
    "Return on Assets": 0.008,
    "Sector": "Basic Materials",
    "P/S": 0.41,
    "Change from Open": -0.0022,
    "Performance (YTD)": 0.0502,
    "Performance (Week)": -0.0694,
    "Quick Ratio": 0.7,
    "Insider Transactions": 0.1031,
    "P/B": 0.75,
    "EPS growth quarter over quarter": 1.143,
    "Payout Ratio": 0.429,
    "Performance (Quarter)": 0.1058,
    "Forward P/E": 21.35,
    "P/E": 35.96,
    "200-Day Simple Moving Average": 0.0823,
    "Shares Outstanding": 1070,
    "Earnings Date": { "$date": 1381264200000 },
    "52-Week High": -0.0925,
    "P/Cash": 9.46,
    "Change": 0.0033,
    "Analyst Recom": 3.1,
    "Volatility (Week)": 0.0345,
    "Country": "USA",
    "Return on Equity": 0.023,
    "50-Day Low": 0.1579,
    "Price": 9.02,
    "50-Day High": -0.0925,
    "Return on Investment": 0.007,
    "Shares Float": 1068.5,
    "Dividend Yield": 0.0133,
    "EPS growth next 5 years": 0.1747,
    "Industry": "Aluminum",
    "Beta": 2.02,
    "Sales growth quarter over quarter": -0.012,
    "Operating Margin": 0.049,
    "EPS (ttm)": 0.25,
    "PEG": 2.06,
    "Float Short": 0.1129,
    "52-Week Low": 0.1899,
    "Average True Range": 0.3,
    "EPS growth next year": 0.231,
    "Sales growth past 5 years": -0.041,
    "Company": "Alcoa, Inc.",
    "Gap": 0.0056,
    "Relative Volume": 0.6,
    "Volatility (Month)": 0.0336,
    "Market Cap": 9619.3,
    "Volume": 14600992,
    "Gross Margin": 0.163,
    "Short Ratio": 4.51,
    "Performance (Half Year)": 0.0652,
    "Relative Strength Index (14)": 49.61,
    "Insider Ownership": 0.0007,
    "20-Day Simple Moving Average": -0.0192,
    "Performance (Month)": 0.0766,
    "P/Free Cash Flow": 33.17,
    "Institutional Transactions": 0.0252,
    "Performance (Year)": 0.0963,
    "LT Debt/Equity": 0.6,
    "Average Volume": 26728.11,
    "EPS growth this year": -0.673,
    "50-Day Simple Moving Average": 0.052
}

# AADR
doc2 = {
    "status": "test",
    "Sector": "Financial",
    "Change from Open": 0.0055,
    "Performance (YTD)": 0.1809,
    "Performance (Week)": -0.0134,
    "Performance (Quarter)": 0.061,
    "200-Day Simple Moving Average": 0.0693,
    "52-Week High": -0.0194,
    "Change": 0.0064,
    "Volatility (Week)": 0.0072,
    "Country": "USA",
    "50-Day Low": 0.0792,
    "Price": 36.4,
    "50-Day High": -0.0194,
    "Dividend Yield": 0.005,
    "Industry": "Exchange Traded Fund",
    "52-Week Low": 0.2727,
    "Average True Range": 0.31,
    "Company": "WCM/BNY Mellon Focused Growth ADR ETF",
    "Gap": 0.0008,
    "Relative Volume": 0.72,
    "Volatility (Month)": 0.0052,
    "Volume": 6660,
    "Performance (Half Year)": 0.04,
    "Relative Strength Index (14)": 51.91,
    "20-Day Simple Moving Average": -0.0054,
    "Performance (Month)": 0.0183,
    "Performance (Year)": 0.229,
    "Average Volume": 10.07,
    "50-Day Simple Moving Average": 0.0158
}

# AAN
doc3 = {
    "Profit Margin": 0.06,
    "status": "test",
    "Institutional Ownership": 0.98,
    "EPS growth past 5 years": 0.204,
    "Total Debt/Equity": 0.12,
    "Return on Assets": 0.074,
    "Sector": "Services",
    "P/S": 1.02,
    "Change from Open": 0,
    "Performance (YTD)": 0.0658,
    "Performance (Week)": 0.0488,
    "Insider Transactions": 0.206,
    "P/B": 1.89,
    "EPS growth quarter over quarter": -0.263,
    "Payout Ratio": 0.038,
    "Performance (Quarter)": 0.0949,
    "Forward P/E": 14.02,
    "P/E": 17.11,
    "200-Day Simple Moving Average": 0.0653,
    "Shares Outstanding": 76.1,
    "Earnings Date": { "$date": 1382646600000 },
    "52-Week High": -0.023,
    "P/Cash": 10.88,
    "Change": 0.0013,
    "Analyst Recom": 2.8,
    "Volatility (Week)": 0.0177,
    "Country": "USA",
    "Return on Equity": 0.116,
    "50-Day Low": 0.1508,
    "Price": 30.15,
    "50-Day High": -0.002,
    "Return on Investment": 0.138,
    "Shares Float": 67.11,
    "Dividend Yield": 0.0023,
    "EPS growth next 5 years": 0.08,
    "Industry": "Rental & Leasing Services",
    "Beta": 1.04,
    "Sales growth quarter over quarter": 0.019,
    "Operating Margin": 0.108,
    "EPS (ttm)": 1.76,
    "PEG": 2.14,
    "Float Short": 0.0601,
    "52-Week Low": 0.2264,
    "Average True Range": 0.49,
    "EPS growth next year": 0.0926,
    "Sales growth past 5 years": 0.098,
    "Company": "Aaron's, Inc.",
    "Gap": 0.0013,
    "Relative Volume": 1.71,
    "Volatility (Month)": 0.0171,
    "Market Cap": 2291.4,
    "Volume": 1190872,
    "Gross Margin": 0.832,
    "Short Ratio": 5.28,
    "Performance (Half Year)": 0.0517,
    "Relative Strength Index (14)": 71.11,
    "Insider Ownership": 0.005,
    "20-Day Simple Moving Average": 0.043,
    "Performance (Month)": 0.0617,
    "Institutional Transactions": 0.0172,
    "Performance (Year)": 0.0255,
    "LT Debt/Equity": 0.12,
    "Average Volume": 763.14,
    "EPS growth this year": 0.573,
    "50-Day Simple Moving Average": 0.0742
}

class TestInsertDocument(unittest.TestCase):
    def test_insert_document(self):
        """
        Test: Will insert one document into collection.
        """
        resp = app.post_json("/stocks/api/v1.0/createStock/AA", doc1.copy())

        self.assertEqual(resp.status, "201 Created")  # Should respond 201
        

    def test_insert_duplicate_document_different_object(self):
        """
        Test: Will insert one document into collection.
        """

        first = app.post_json('/stocks/api/v1.0/createStock/AA', doc1.copy())  # First
        resp = app.post_json('/stocks/api/v1.0/createStock/AA', doc1.copy())   # Duplicate
        
        self.assertEqual(first.status, "201 Created")  # Should respond 201
        self.assertEqual(resp.status, "201 Created")   # Should respond 201
        
        # Let's remove the _ids that are generated for Mongo:
        first = first.json
        first.pop("_id")

        resp = resp.json
        resp.pop("_id")

        # With the _ids gone, these should now be the same.
        self.assertDictEqual(first, resp)

    def test_insert_duplicate_document_same_object(self):
        """
        Test: Will insert one document into collection (duplicate).
        """
        first = app.post_json('/stocks/api/v1.0/createStock/AA', doc1, expect_errors=True)
        resp = app.post_json('/stocks/api/v1.0/createStock/AA', first.json, expect_errors=True)
        
        expected = { "Error 400": "Document wasn't inserted!" }

        # This should return a 404 because the read fails.
        self.assertEqual(resp.status, "400 Bad Request")
        self.assertEqual(resp.json, expected)

class TestReadDocument(unittest.TestCase):
    def test_read_one_document(self):
        """
        Test: Will find the first document that matches the data dictionary
              shown below.
        """
        resp = app.get('/stocks/api/v1.0/getStock/AA')

        self.assertEqual(resp.status, "200 OK")

    def test_wont_find_document(self):
        """
        Test: Will not find a document, should return 404 error.
        """
        resp = app.get('/stocks/api/v1.0/getStock/NONE', expect_errors=True)
        expected = { "Error": "No documents found!", "alive": False }
        
        self.assertEqual(resp.status, "404 Not Found")
        self.assertEqual(resp.json, expected)

class TestUpdateDocument(unittest.TestCase):
    def test_update_one_document(self):
        """
        Test: Will update first document found.
        """
        # I need to insert a specific test ticker:
        original = app.post_json('/stocks/api/v1.0/createStock/AATEST', doc1.copy()).json

        update = {
            "Profit Margin": 1.0,
            "Institutional Ownership": 2.0,
            "EPS growth past 5 years": 3.0,
            "Total Debt/Equity": 4.0,
            "Current Ratio": 5.0
        }

        resp = app.put_json('/stocks/api/v1.0/updateStock/AATEST', update)

        self.assertEqual(resp.status, "200 OK")
        
        updated = resp.json

        for key in update.keys():
            self.assertNotEqual(original[key], updated[key])
            # If the above doesn't fail, it'll continue to the next line:
            original.pop(key)
            updated.pop(key)

        # Let's get rid of the _ids so we can compare them:
        original.pop("_id")
        updated.pop("_id")

        # Now, make sure that everything else is the same
        self.assertDictEqual(original, updated)

    def test_upsert(self):
        """
        Test: Will upsert into found document.
        """
        # We know this ticker doesn't exist, so let's try to upsert it.
        resp = app.put_json('/stocks/api/v1.0/updateStock/ABTEST', doc1.copy())

        self.assertEqual(resp.status, "201 Created")
        self.assertTrue(resp.json["upserted"])

    def test_update_with_error(self):
        """
        Test: This should throw an error and return 404.
        """
        # We know there's only one of these so far:
        app.post_json('/stocks/api/v1.0/createStock/ABTEST', doc1.copy())
        update = { "$none": 1381264200000 }

        resp = app.put_json('/stocks/api/v1.0/updateStock/ABTEST', update, expect_errors=True)
        self.assertEqual(resp.status, "400 Bad Request")

        expected = { "Error": "The dollar ($) prefixed field '$none' in '$none' is not valid for storage." }        
        self.assertIn("Error", resp.json)
        self.assertEqual(resp.json, expected)

class TestDeleteDocument(unittest.TestCase):
    def test_delete_one_document(self):
        """
        Test: Will delete the first document found.
        """
        # In theory, this is the one:
        firstFound = app.get('/stocks/api/v1.0/getStock/AATEST')
        resp = app.delete('/stocks/api/v1.0/deleteStock/AATEST')

        self.assertEqual(resp.status, "200 OK")
        self.assertEqual(resp.json, firstFound.json)
        

    def test_will_not_delete_document(self):
        """
        Test: Won't find a document and won't delete anything.
        """
        resp = app.delete('/stocks/api/v1.0/deleteStock/AATESTS', expect_errors=True)
        expected = { 'Error': "'_id'" }

        self.assertEqual(resp.status, "404 Not Found")
        self.assertEqual(resp.json, expected)

class TestStockReport(unittest.TestCase):
    def test_find_stocks_by_list(self):
        """
        Test: Will test the response sent to stockReport route as  shown in
              the rubric.
        """
        data = { "list": [ "AA", "BA", "T" ] }
        resp = app.post_json('/stocks/api/v1.0/stockReport', data)
        self.assertTrue("Stocks" in resp)
        tickers = []
        expected = data["list"]
        
        for stock in resp.json["Stocks"]:
            tickers.append(stock["Ticker"])

        self.assertListEqual(tickers, expected)

class TestTopFiveIndustry(unittest.TestCase):
    def test_find_top_five_stocks_by_med_lab_and_research(self):
        """
        Test: Will return a list of the top five industries in medical lab and
              research.
        """
        resp = app.get('/stocks/api/v1.0/industryReport/Medical%20Laboratories%20%26%20Research')
        expected = { 'Tickers': [ 'A', 'AIQ', 'ALR', 'BGMD', 'BRLI' ] }
        self.assertEqual(resp.status, "200 OK")
        self.assertDictEqual(resp.json, expected)

    def test_wont_find_industry(self):
        """
        Test: Won't find any industry.
        """
        resp = app.get('/stocks/api/v1.0/industryReport/NONE%20EXIST', expect_errors=True)
        expected = { "Error": "No documents found." }

        self.assertEqual(resp.status, "404 Not Found")
        self.assertDictEqual(resp.json, expected)

class Takedown(unittest.TestCase):
    def reset_db(self):
        """
        Takedown: Remove all test documents from prod db.
        """
        docs = api.read_document("status", "test")
        for doc in docs:
            api.delete_document(doc)

        error = { "Error": "No documents found!", "alive": False }
        result = next(api.read_document("status", "test"))

        self.assertEqual(error, result, "Test documents still exist!")