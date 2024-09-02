from data_loader import DataLoader
from data_updater import DataUpdater
from financial_model_enumerator import FinancialModelEnumerator

def main():
    file_path = 'data/financial_model.xlsx'
    new_file_path = 'data/updated_financial_model.xlsx'

    # Load data
    loader = DataLoader(file_path)
    df = loader.load_sheet('Sheet1')
    print(df)

    # Enumerate cells
    enumerator = FinancialModelEnumerator(file_path)
    enumerator.enumerate_cells('Sheet1')
    key_metrics = enumerator.identify_key_metrics('Sheet1', ['Revenue', 'Expenses'])
    print(key_metrics)

    # Update values
    updater = DataUpdater(file_path)
    updater.update_value('Revenue', 100000)
    updater.save(new_file_path)

if __name__ == "__main__":
    main()