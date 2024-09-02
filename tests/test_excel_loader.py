import unittest
from excel_loader import ExcelLoader

class TestExcelLoader(unittest.TestCase):
    def test_load_sheet(self):
        loader = ExcelLoader('data/financial_model.xlsx')
        df = loader.load_sheet('Sheet1')
        self.assertIsNotNone(df)

if __name__ == '__main__':
    unittest.main()