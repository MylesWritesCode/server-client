import unittest
import manipulation_test as test

def test_db_suite():
    suite = unittest.TestSuite()

    # Setup
    # suite.addTest(test.Setup("setup"))

    # Insert tests
    suite.addTest(test.TestInsert("test_insert_documents"))
    suite.addTest(test.TestInsert("test_insert_single_document"))
    suite.addTest(test.TestInsert("test_insert_documents_no_list"))

    # Update tests
    suite.addTest(test.TestUpdate("test_update_will_fail_first_param"))
    suite.addTest(test.TestUpdate("test_update_will_fail_second_param"))
    suite.addTest(test.TestUpdate("test_update_document"))
    
    # Update Volume tests
    suite.addTest(test.TestUpdateVolume("test_update_volume"))
    
    # Delete by Ticker tests
    suite.addTest(test.TestDelByTicker("test_delete_by_ticker"))

    # Delete tests
    suite.addTest(test.TestDelete("test_will_fail_parameter"))
    suite.addTest(test.TestDelete("test_will_delete_some_test_documents"))
    suite.addTest(test.TestDelete("test_will_delete_all_test_documents"))
    
    # Run test takedown procedcure:
    suite.addTest(test.Takedown("reset_db"))
        
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast = True, verbosity = 2)
    runner.run(test_db_suite())