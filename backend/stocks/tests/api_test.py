import unittest
# We're transforming the document using the server, not the API, so we're just
# going to convert it here.
from datetime import datetime    

import sys, os   # Needed to import using relative path.
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# Not super happy about using this, but it works.

from api import api

doc1 = {
    "Ticker": "AA",
    "Profit Margin": 0.013,
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
    "Earnings Date": datetime.fromtimestamp(1381264200000 / 1000),
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
    "50-Day Simple Moving Average": 0.052,
    "status": "test"
}

doc2 = {
    "Ticker": "AADR",
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
    "50-Day Simple Moving Average": 0.0158,
    "status": "test"
}

doc3 = {
    "Ticker": "AAN",
    "Profit Margin": 0.06,
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
    "Earnings Date": datetime.fromtimestamp(1382646600000 / 1000),
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
    "50-Day Simple Moving Average": 0.0742,
    "status": "test"
}

# Adding this to an array so it's easier to insert.
documents = [ doc1.copy(), doc2.copy() ]

class TestInsert(unittest.TestCase):

    def test_insert_documents(self):
        """
        Test that will insert into MongoDB.
        """
        result = api.insert_documents(documents)
        # ids should change all the time, so we need to check length instead.
        self.assertTrue("ids" in result, "ids does not exist in result")
        self.assertTrue(len(result["ids"]) > 0, "there are no inserted documents in ids")

            
    def test_insert_duplicate_document(self):
        """
        Test: Insert a duplicate document.
        """
        
        self.assertTrue(api.insert_documents(doc1.copy()))

        docs = api.read_document({ "Ticker": "AA", "status": "test" })
        
        first = next(docs)
        if (docs.alive):
            other = next(docs)
        else:
            self.assertTrue(False, "Duplicate document doesn't exist.")

        self.assertNotEqual(first["_id"], other["_id"])

        first.pop("_id")
        other.pop("_id")

        # Ensure that both dictionaries are the same without ids:
        self.assertDictEqual(first, other)

    # Need to make sure it doesn't enter the same object as well.
    def test_insert_exact_duplicate(self):
        """
        Test: Insert exact same document.
        """
        # Get the first instance of doc1 in db:
        doc = next(api.read_document(doc1.copy()))
        # Insert the document we just got.
        result = api.insert_documents(doc)

        # Not sure what the error is going to be, but I know for sure that
        # there's going to be one relating to duplicate ids.
        self.assertTrue("Error" in result)

class TestRead(unittest.TestCase):

    def test_will_find_w_whole_document(self):
        """
        Test: Find ONE document using whole dictionary.
        """
        original = doc1.copy()
        for doc in api.read_document(doc1):
            del doc["_id"]
            self.assertDictEqual(doc, doc1)
        

    def test_will_find_w_partial_document(self):
        """
        Test: Find ONE document using partial dictionary.
        """
        kv = { "Ticker": doc1["Ticker"], "status": "test" }
        for doc in api.read_document(kv):
            del doc["_id"]
            self.assertDictEqual(doc, doc1)
            
    
    def test_will_find_w_key_value(self):
        """
        Test: Find ONE value using k, v.
        """
        kv = { "Ticker": doc1["Ticker"] }
        docs = api.read_document(list(kv.keys())[0], list(kv.values())[0])
        
        for doc in docs:
            if "status" in doc:
                doc.pop("_id")
                self.assertDictEqual(doc, doc1)



    def test_will_find_many_w_key_value(self):
        """
        Test: Find MANY documents using k, v.
        """
        api.insert_documents(doc1.copy())
        
        docs = api.read_document("Ticker", doc1["Ticker"])
        self.assertGreater(docs.explain()["n"], 1)  # There should be two results

    def test_will_find_many_w_document(self):
        """
        Test: Find MANY documents with document.
        """
        original = doc1.copy()
        docs = api.read_document(original)

        if docs.explain()["n"] == 1:
            self.assertTrue(False, "Didn't find 2 documents.")

        for doc in docs:
            if "status" in doc:
                doc.pop("_id")
                self.assertDictEqual(doc, doc1)

    def test_will_not_find_w_document(self):
        """
        Test: Won't find a document using document.
        """
        kv = { "no_key": "no_value" }
        error = { "Error: No documents found!" : -1 }
        doc = next(api.read_document(kv))
        
        self.assertNotIn("no_key", doc)
        self.assertIn("Error", doc)
        self.assertEqual(doc["Error"], "No documents found!")

    def test_will_not_find_w_key_value(self):
        """
        Test: Won't find a document using k, v.
        """
        kv = { "no_key": "no_value" }
        doc = next(api.read_document(list(kv.keys())[0], list(kv.values())[0]))
        
        self.assertNotIn("no_key", doc)
        self.assertIn("Error", doc)
        self.assertEqual(doc["Error"], "No documents found!")

class TestUpdate(unittest.TestCase):

    def test_update_one_document(self):
        """
        Test: Update document found.
        """
        update = {
            "Change from Open": 1.0055,
            "Performance (YTD)": 1.1809,
            "Performance (Week)": -1.0134,
            "Performance (Quarter)": 1.061
        }

        doc = {
            "Ticker": doc2["Ticker"],
            "status": "test"
        }

        cursor = api.read_document(doc)
        previous = next(cursor)
        cursor.close()
        
        result = api.update_document(doc, update)

        cursor = api.read_document(doc)
        other = next(cursor)
        cursor.close()

        # Ensure that we have the same document:
        self.assertEqual(previous["_id"], other["_id"])

        # This for-loop will test the keys from testAndPop to ensure
        # inequality, then it will pop the keys from both of the dictionaries.
        for k in update.keys():
            self.assertNotEqual(previous[k], other[k])
            # If the above passes, move to the next line.
            previous.pop(k, None)
            other.pop(k, None)

        # previous.pop("_id")
        # other.pop("_id")

        self.assertDictEqual(previous, other)

    def test_update_volume(self):
        """
        Test: Per the rubric, this will just update one ticker's volume.
        """
        update = {
            "Volume": 1000
        }

        doc = {
            "Ticker": doc2["Ticker"],
            "status": "test"
        }

        cursor = api.read_document(doc)
        previous = next(cursor)
        cursor.close()
        
        result = api.update_document(doc, update)

        cursor = api.read_document(doc)
        other = next(cursor)
        cursor.close()

        # Ensure that we have the same document:
        self.assertEqual(previous["_id"], other["_id"])
        self.assertNotEqual(previous["Volume"], other["Volume"])

        previous.pop("Volume")
        other.pop("Volume")

        self.assertDictEqual(previous, other)

    def test_update_none_found_upsert(self):
        """
        Test: Update will upsert a document.
        """        
        original = next(api.read_document("none", "exists"))

        update = {
            "Change from Open": 1.0055,
            "Performance (YTD)": 1.1809,
            "Performance (Week)": -1.0134,
            "Performance (Quarter)": 1.061,
            "status": "test"
        }

        result = api.update_document("none", "exists", update)

        self.assertTrue(result["upserted"])
        

    def test_update_with_error(self):
        """
        Test: Update will fail with assertion error.
        """        
        original = next(api.read_document("none", "exists"))

        # This was giving me issues initially, so it should pop an error from
        # MongoDB.
        update = { "$date": 1381264200000 }

        result = api.update_document("none", "exists", update)

        self.assertIn("Error", result)
        # This is the error I was getting when first building out the API. It
        # should ensure that no document can be inserted with $date as a key.
        self.assertEqual(result["Error"], "The dollar ($) prefixed field '$date' in '$date' is not valid for storage.")

class TestDelete(unittest.TestCase):
    def test_will_not_delete(self):
        """
        Test: Won't find a document to delete.
        """
        result = api.delete_document(doc3.copy())
        
        self.assertIn("Error", result)
    
    def test_will_delete_one_w_document(self):
        """
        Test: Delete one document with document.
        """
        
        # This test may not run last, not sure. Regardless, lets make sure
        # there's something to delete.
        # Update: Using a test runner, so it should run last. Regardless, I'm
        #         going to keep this insertion code in here.
        api.insert_documents(doc3.copy())

        original = next(api.read_document(doc3.copy()))
        result = api.delete_document(doc3.copy())

        self.assertDictEqual(original, result)

        error = next(api.read_document(doc3.copy()))
        
        self.assertEqual(error["Error"], "No documents found!")

    def test_will_delete_one_w_key_value(self):
        """
        Test: Delete one document with k, v.
        """
        api.insert_documents(doc3.copy())

        doc = {
            "Ticker": doc3["Ticker"],
            "status": "test"
        }

        original = next(api.read_document(doc3.copy()))
        result = api.delete_document(doc)

        self.assertDictEqual(original, result)
        
    def test_will_delete_one_w_document_duplicates(self):
        """
        Test: Delete one document with document (duplicates exist).
        """

        api.insert_documents(doc3.copy())
        api.insert_documents(doc3.copy())

        original = next(api.read_document(doc3.copy()))
        result = api.delete_document(doc3.copy())

        self.assertDictEqual(original, result)
        
        # Ensure that there's still at least one document left:
        other = next(api.read_document(doc3.copy()))

        self.assertNotEqual(result["_id"], other["_id"])

        # Remove the ids, it should be the only key different between the two.
        result.pop("_id")
        other.pop("_id")

        # Then ensure that both documents are equal to each other. This means
        # that two was found, but only one remains even though both documents
        # are identical.
        self.assertDictEqual(result, other)

class TestSMA(unittest.TestCase):
    def test_error_first_param(self):
        result = api.find_SMA_50("fail", 20)
        error = { "Error": "First parameter is not a number!"}
        self.assertEqual(error, result)

    def test_error_second_param(self):
        result = api.find_SMA_50(1.0, "fail")
        error = { "Error": "Second parameter is not a number!"}
        self.assertEqual(error, result)

    def test_find_count_correctly(self):
        """
        Used MongoDB to generate this, so it should be the same.

        IMPORTANT: This is the first test that will fail if DEBUG is false,
                   but these tests are contingent on stocks.json being 
                   imported into market.stocks in Mongo. Because some of the
                   next tests will fail, let's put a warning message letting
                   the person running the test know that we don't have the
                   right data to test this.
        """
        result = api.find_SMA_50(0.00, 0.01)
        expected = { "Count": 588 }
        self.assertEqual(expected, result, "Are you sure stocks.json is imported into the markets.stocks collection?")

class TestIndustry(unittest.TestCase):
    def test_error_not_string(self):
        result = api.find_industry(20)
        expected = { "Error": "Parameter requires a string!" }

        self.assertEqual(result, expected)

    def test_find_medical_labs_and_research(self):
        result = api.find_industry("Medical Laboratories & Research")
        expected = {
            "_id": "null",
            "Tickers": [
                "A", "AIQ", "ALR", "BGMD", "BRLI", "CBMX", "CO", "CVD", "DGX",
                "ENZ", "FMI", "GHDX", "HSKA", "ICLR", "IRWD", "LH", "LIFE",
                "LPDX", "MTD", "NDZ", "NEO", "NVDQ", "ONVO", "PKI", "PMD",
                "PRXL", "Q", "RDNT", "RGDX", "ROSG", "SPEX", "TEAR", "TMO",
                "WAT", "WX"
            ]
        }

        self.assertEqual(result, expected)

    def test_no_documents_found(self):
        # This should throw an error.
        result = api.find_industry("none")
        expected = { "Error": "No documents found." }

        self.assertEqual(result, expected)

class TestSharesWithSector(unittest.TestCase):
    def test_error_not_string(self):
        result = api.find_outstanding_shares_by_sector(20)
        expected = { "Error": "Parameter requires a string!" }

        self.assertEqual(result, expected)

    def test_no_industries_found(self):
        result = api.find_outstanding_shares_by_sector("none")
        expected = { "Error": "No industries found!" }

        self.assertEqual(result, expected)

    def test_outstanding_by_healthcare(self):
        result = api.find_outstanding_shares_by_sector("Healthcare")
        expected = {
            "shares": [
                { "_id": "Medical Practitioners", "Total Outstanding Shares": 19.24 },
                { "_id": "Medical Instruments & Supplies", "Total Outstanding Shares": 3512.9199999999983 },
                { "_id": "Drug Manufacturers - Other", "Total Outstanding Shares": 3792.9299999999994 },
                { "_id": "Health Care Plans", "Total Outstanding Shares": 3280.2200000000003 },
                { "_id": "Home Health Care", "Total Outstanding Shares": 193.44 },
                { "_id": "Specialized Health Services", "Total Outstanding Shares": 1923.1 },
                { "_id": "Biotechnology", "Total Outstanding Shares": 13893.719999999994 },
                { "_id": "Hospitals", "Total Outstanding Shares": 1246.4600000000003 },
                { "_id": "Drug Delivery", "Total Outstanding Shares": 1730.4500000000003 },
                { "_id": "Medical Appliances & Equipment", "Total Outstanding Shares": 8336.599999999999 },
                { "_id": "Drugs - Generic", "Total Outstanding Shares": 1608.1800000000003 },
                { "_id": "Long-Term Care Facilities", "Total Outstanding Shares": 524.15 },
                { "_id": "Drug Manufacturers - Major", "Total Outstanding Shares": 26805.450000000004 },
                { "_id": "Diagnostic Substances", "Total Outstanding Shares": 506.85 },
                { "_id": "Drug Related Products", "Total Outstanding Shares": 309.06 },
                { "_id": "Medical Laboratories & Research", "Total Outstanding Shares": 2495.2200000000003 }
            ]
        }

        self.assertEqual(result, expected)

    def test_outstanding_by_basic_materials(self):
        result = api.find_outstanding_shares_by_sector("Basic Materials")
        expected = {
            "shares": [
                { "_id": "Copper", "Total Outstanding Shares": 2057.18 },
                { "_id": "Oil & Gas Pipelines", "Total Outstanding Shares": 9837.399999999998 }, 
                { "_id": "Synthetics", "Total Outstanding Shares": 323.25 }, 
                { "_id": "Independent Oil & Gas", "Total Outstanding Shares": 16417.190000000006 },
                { "_id": "Oil & Gas Equipment & Services", "Total Outstanding Shares": 7209.119999999998 },
                { "_id": "Aluminum", "Total Outstanding Shares": 2464.68 },
                { "_id": "Chemicals - Major Diversified", "Total Outstanding Shares": 5227.03 },
                { "_id": "Nonmetallic Mineral Mining", "Total Outstanding Shares": 906.8599999999999 },
                { "_id": "Oil & Gas Drilling & Exploration", "Total Outstanding Shares": 23897.049999999996 },
                { "_id": "Major Integrated Oil & Gas", "Total Outstanding Shares": 28000.93 },
                { "_id": "Agricultural Chemicals", "Total Outstanding Shares": 2890.41 },
                { "_id": "Oil & Gas Refining & Marketing", "Total Outstanding Shares": 4408.25 },
                { "_id": "Silver", "Total Outstanding Shares": 1730.3899999999999 },
                { "_id": "Industrial Metals & Minerals", "Total Outstanding Shares": 21226.47 },
                { "_id": "Specialty Chemicals", "Total Outstanding Shares": 3442.2300000000005 },
                { "_id": "Gold", "Total Outstanding Shares": 12628.110000000004 },
                { "_id": "Steel & Iron", "Total Outstanding Shares": 10221.039999999999 }
            ]
        }

        self.assertEqual(result, expected)

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


# if __name__ == '__main__':
#     unittest.main()