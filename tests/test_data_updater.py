import unittest
from data_updater import DataUpdater

class TestDataUpdater(unittest.TestCase):
    def test_update_value(self):
        updater = DataUpdater('data/financial_model.xlsx')
        updater.update_value('Revenue', 100000)
        updater.save('data/updated_financial_model.xlsx')
        # Assuming there's a method to verify the update
        updated_value = updater.get_value('Revenue')
        self.assertEqual(updated_value, 100000)

if __name__ == '__main__':
    unittest.main()