import unittest
import retrieval_test as test

def test_db_suite():
    suite = unittest.TestSuite()

    # General Tests
    suite.addTest(test.TestGeneral("test_find_SMA_50_small"))
    suite.addTest(test.TestGeneral("test_find_SMA_50_medium"))
    suite.addTest(test.TestGeneral("test_find_SMA_50_large"))
    suite.addTest(test.TestGeneral("test_find_SMA_ratios_make_sense"))
    suite.addTest(test.TestGeneral("test_find_industry_med_lab_and_research"))
    suite.addTest(test.TestGeneral("test_find_outstanding_shares_by_healthcare"))
    suite.addTest(test.TestGeneral("test_find_outstanding_shares_by_basic_materials"))
        
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast = True, verbosity = 2)
    runner.run(test_db_suite())