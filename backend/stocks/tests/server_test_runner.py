import unittest
import server_test as test

def test_db_suite():
    suite = unittest.TestSuite()

    suite.addTest(test.Takedown("reset_db"))

    # Create Tests
    suite.addTest(test.TestInsertDocument("test_insert_document"))
    suite.addTest(test.TestInsertDocument("test_insert_duplicate_document_different_object"))
    suite.addTest(test.TestInsertDocument("test_insert_duplicate_document_same_object"))

    # Read Tests
    suite.addTest(test.TestReadDocument("test_read_one_document"))
    suite.addTest(test.TestReadDocument("test_wont_find_document"))

    # Update Tests
    suite.addTest(test.TestUpdateDocument("test_update_one_document"))
    suite.addTest(test.TestUpdateDocument("test_upsert"))
    suite.addTest(test.TestUpdateDocument("test_update_with_error"))

    # Delete Tests
    suite.addTest(test.TestDeleteDocument("test_delete_one_document"))
    suite.addTest(test.TestDeleteDocument("test_will_not_delete_document"))
    suite.addTest(test.Takedown("reset_db"))

    if not test.api.DEBUG:
        suite.addTest(test.TestStockReport("test_find_stocks_by_list"))
        suite.addTest(test.TestTopFiveIndustry("test_find_top_five_stocks_by_med_lab_and_research"))
        suite.addTest(test.TestTopFiveIndustry("test_wont_find_industry"))

    # Takedown

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast = True, verbosity = 2)
    runner.run(test_db_suite())