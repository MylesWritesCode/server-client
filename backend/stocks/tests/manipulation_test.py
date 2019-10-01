import unittest
# We're transforming the document using the server, not the API, so we're just
# going to convert it here.
from datetime import datetime    

import sys, os   # Needed to import using relative path.
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# Not super happy about using this, but it works.

from sections import manipulation as m  # Just want to make this easier to write.

data = m.load_json(m.read_file("sections/data.json"))

for doc in data:
    m.transform_document(doc)

class TestInsert(unittest.TestCase):
    def test_insert_documents(self):
        """
        This test will insert every single document in our data list into the
        db. 
        """
        result = m.insert_documents(data)
        # If this is true, then that means that we have at least one inserted
        # _id in our returned list.
        
        self.assertTrue("ids" in result, "ids does not exist in result")
        self.assertTrue(len(result["ids"]) > 0, "length is not greater than 0")
            
    def test_insert_single_document(self):
        """
        We should also make sure that exactly one document can be inserted into
        our db.
        """
        # Will insert first document in data array.
        result = m.insert_documents(data[0])
        expected = { "Error": "batch op errors occurred" }
        self.assertFalse("ids" in result)
        self.assertEqual(result, expected)
        
    def test_insert_documents_no_list(self):
        """
        The exception should catch if we try to insert an empty list into our
        db.
        """
        result = m.insert_documents([])
        expected = { "Error": "documents must be a non-empty list" }
        self.assertEqual(result, expected)

class TestUpdate(unittest.TestCase):
    def test_update_will_fail_first_param(self):
        result = m.update_document(1, { "k": "v" })
        expected = { "Error": "First parameter must be a dictionary." }
        self.assertEqual(result, expected)

    def test_update_will_fail_second_param(self):
        result = m.update_document({ "k": "v" }, 1)
        expected = { "Error": "Second parameter must be a dictionary." }
        self.assertEqual(result, expected)

    def test_update_document(self):
        """
        Test will update one document, and should return the raw result.
        """
        u_data = { "Volume": 1000 }
        result = m.update_document({ "status": "test" }, u_data)
        updated = m.find_document({ "_id": result["_id"] })

        self.assertNotEqual(updated["Volume"], result["Volume"])
        updated.pop("Volume")
        result.pop("Volume")

        self.assertDictEqual(updated, result)

class TestUpdateVolume(unittest.TestCase):
    def test_update_volume(self):
        """
        Will update *only* the TEST ticker.
        """
        original = m.update_volume("TEST", 10)
        updated = m.find_document({ "Ticker": "TEST" })

        self.assertNotEqual(original["Volume"], updated["Volume"])
        original.pop("Volume")
        self.assertEqual(updated["Volume"], 10)
        updated.pop("Volume")

        # Finally, ensure that both documents are the same without the change.
        self.assertEqual(original, updated)

class TestDelByTicker(unittest.TestCase):
    def test_delete_by_ticker(self):
        original = m.find_document({ "Ticker": "TEST" })
        result = m.delete_by_ticker("TEST")
        expected = { "ok": 1, "n": 1 }

        self.assertDictEqual(result, expected)

        # Also, there shouldn't be another ticker named TEST in the db:
        deleted = m.delete_by_ticker(original)
        expected = { "ok": 1, "n": 0 }
        
        self.assertDictEqual(deleted, expected)
        

class TestDelete(unittest.TestCase):
    def test_will_fail_parameter(self):
        """
        Function will fail after reading the sent variable.
        """
        result = m.delete_documents(1)
        expected = { "Error": "Search critera must be a dictionary." }

        self.assertEqual(result, expected)
    
    def test_will_delete_some_test_documents(self):
        search = { "Ticker": "AA", "status": "test" }
        result = m.delete_documents(search)
        expected = {'ok': 1, 'n': 1}
        
        self.assertDictEqual(result, expected)

    def test_will_delete_all_test_documents(self):
        search = { "status": "test" }
        result = m.delete_documents(search)
        expected = expected = {'ok': 1, 'n': 9}
        
        self.assertDictEqual(result, expected)
    
    

class Takedown(unittest.TestCase):
    def reset_db(self):
        """
        This should be taken care of in delete testing, but I'll just be
        explicit about clearing the db of test documents.
        """
        m.delete_documents({ "status": "test" })

        result = m.find_document({ "status": "test" })
        self.assertTrue(result is None)

# if __name__ == '__main__':
#     unittest.main()