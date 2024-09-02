from excel_loader import ExcelLoader
from excel_updater import ExcelUpdater
from financial_model_enumerator import FinancialModelEnumerator
# TODO: Fix the issue with the tests not being found
# from ..tests import run_tests

def main():
    file_path = 'data/financial_model.xlsx'
    new_file_path = 'data/updated_financial_model.xlsx'

    # Load data
    loader = ExcelLoader(file_path)
    df = loader.load_sheet('Sheet1')
    print("Data loaded successfully")

    # Enumerate cells
    enumerator = FinancialModelEnumerator(file_path)
    enumerator.enumerate_cells('Sheet1')
    key_metrics = enumerator.identify_key_metrics('Sheet1', ['Revenue', 'Expenses'])
    print("Key metrics identified successfully")

    # Copy cell styles
    updater = ExcelUpdater(file_path)
    updater.copy_cell_styles(new_file_path)
    print("Cell styles copied successfully")

    # Update values
    updater = ExcelUpdater(file_path)
    updater.update_value('Revenue', 100000)
    updater.save(new_file_path)
    print("Values updated successfully")

    # Run tests
    # TODO: Fix the issue with the tests not being found
    # run_tests()
    # print("Tests passed successfully")

if __name__ == "__main__":
    main()