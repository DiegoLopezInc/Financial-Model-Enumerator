import unittest
from data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_sheet(self):
        loader = DataLoader('data/financial_model.xlsx')
        df = loader.load_sheet('Sheet1')
        self.assertIsNotNone(df)

if __name__ == '__main__':
    unittest.main()