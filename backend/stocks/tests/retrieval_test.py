import unittest
import sys, os   # Needed to import using relative path.
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from sections import retrieval as r  # Just want to make this easier to write.

class TestGeneral(unittest.TestCase):
    small = 0
    medium = 0
    large = 0
    def test_find_SMA_50_small(self):
        small = r.find_SMA_50(0.00, 0.01)
        expected = { "Count": 588 }
        self.assertEqual(small, expected)
        TestGeneral.small = small["Count"]

    def test_find_SMA_50_medium(self):
        medium = r.find_SMA_50(0.00, 0.10)
        expected = { "Count": 3398 }
        self.assertEqual(medium, expected)
        TestGeneral.medium = medium["Count"]

    def test_find_SMA_50_large(self):
        large = r.find_SMA_50(0.00, 0.25)
        expected = { "Count": 4041 }
        self.assertEqual(large, expected)
        TestGeneral.large = large["Count"]

    def test_find_SMA_ratios_make_sense(self):
        self.assertTrue(TestGeneral.small < TestGeneral.medium < TestGeneral.large)

    def test_find_industry_med_lab_and_research(self):
        result = r.find_industry("Medical Laboratories & Research")
        self.assertTrue("Tickers" in result)
        expected = {
            "Tickers": [
                "A", "AIQ", "ALR", "BGMD", "BRLI", "CBMX", "CO", "CVD", "DGX",
                "ENZ", "FMI", "GHDX", "HSKA", "ICLR", "IRWD", "LH", "LIFE", 
                "LPDX", "MTD", "NDZ", "NEO", "NVDQ", "ONVO", "PKI", "PMD",
                "PRXL", "Q", "RDNT", "RGDX", "ROSG", "SPEX", "TEAR", "TMO", 
                "WAT", "WX"
            ]
        }
        self.assertDictEqual(result, expected)

    def test_find_outstanding_shares_by_healthcare(self):
        result = r.find_outstanding_shares_by_sector("Healthcare")
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
        self.assertDictEqual(result,expected)

    def test_find_outstanding_shares_by_basic_materials(self):
        result = r.find_outstanding_shares_by_sector("Basic Materials")
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
        self.assertDictEqual(result,expected)


# if __name__ == '__main__':
#     unittest.main()