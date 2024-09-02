import unittest
from financial_model_enumerator import FinancialModelEnumerator

class TestFinancialModelEnumerator(unittest.TestCase):
    def setUp(self):
        self.enumerator = FinancialModelEnumerator('data/financial_model.xlsx')

    def test_enumerate_cells(self):
        self.enumerator.enumerate_cells('Sheet1')
        # Assuming there's a way to verify the output, e.g., capturing printed output

    def test_identify_key_metrics(self):
        key_metrics = self.enumerator.identify_key_metrics('Sheet1', ['Revenue', 'Expenses'])
        self.assertIn('Revenue', key_metrics)
        self.assertIn('Expenses', key_metrics)

    def test_update_values(self):
        self.enumerator.update_values('Sheet1', 'Revenue', 100000)
        # Assuming there's a method to verify the update
        updated_value = self.enumerator.workbook['Sheet1'].cell(row=key_metrics['Revenue'][0], column=key_metrics['Revenue'][1] + 1).value
        self.assertEqual(updated_value, 100000)

if __name__ == '__main__':
    unittest.main()