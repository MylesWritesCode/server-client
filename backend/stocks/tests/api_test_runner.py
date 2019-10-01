import unittest
import api_test as test

def test_db_suite():
    suite = unittest.TestSuite()

    # Insert tests
    suite.addTest(test.TestInsert("test_insert_documents"))
    suite.addTest(test.TestInsert("test_insert_duplicate_document"))
    suite.addTest(test.TestInsert("test_insert_exact_duplicate"))

    # Find tests
    suite.addTest(test.TestRead("test_will_find_w_whole_document"))
    suite.addTest(test.TestRead("test_will_find_w_partial_document"))
    suite.addTest(test.TestRead("test_will_find_w_key_value"))
    suite.addTest(test.TestRead("test_will_find_many_w_key_value"))
    suite.addTest(test.TestRead("test_will_find_many_w_document"))
    suite.addTest(test.TestRead("test_will_not_find_w_document"))
    suite.addTest(test.TestRead("test_will_not_find_w_key_value"))

    # Update tests
    suite.addTest(test.TestUpdate("test_update_one_document"))
    suite.addTest(test.TestUpdate("test_update_volume"))
    suite.addTest(test.TestUpdate("test_update_none_found_upsert"))
    suite.addTest(test.TestUpdate("test_update_with_error"))

    # Delete tests
    suite.addTest(test.TestDelete("test_will_not_delete"))
    suite.addTest(test.TestDelete("test_will_delete_one_w_document"))
    suite.addTest(test.TestDelete("test_will_delete_one_w_key_value"))
    suite.addTest(test.TestDelete("test_will_delete_one_w_document_duplicates"))

    # Run test takedown procedcure:
    suite.addTest(test.Takedown("reset_db"))
    
    # These tests will run if not in debug mode. They're meant to test some
    # find methods, and shouldn't insert/update anything in the db.
    if not test.api.DEBUG:
        # SMA tests
        suite.addTest(test.TestSMA("test_error_first_param"))
        suite.addTest(test.TestSMA("test_error_second_param"))
        suite.addTest(test.TestSMA("test_find_count_correctly"))

        # Industry tests
        suite.addTest(test.TestIndustry("test_error_not_string"))
        suite.addTest(test.TestIndustry("test_find_medical_labs_and_research"))
        suite.addTest(test.TestIndustry("test_no_documents_found"))
        
        # Outstanding Shares tests
        suite.addTest(test.TestSharesWithSector("test_error_not_string"))
        suite.addTest(test.TestSharesWithSector("test_no_industries_found"))
        suite.addTest(test.TestSharesWithSector("test_outstanding_by_healthcare"))
        suite.addTest(test.TestSharesWithSector("test_outstanding_by_basic_materials"))
        
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast = True, verbosity = 2)
    runner.run(test_db_suite())