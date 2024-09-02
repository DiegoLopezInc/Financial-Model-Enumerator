import pandas as pd

class ExcelLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_sheet(self, sheet_name):
        # Check if the sheet name is valid
        if sheet_name not in pd.ExcelFile(self.file_path).sheet_names:
            raise ValueError(f"Sheet '{sheet_name}' not found in the Excel file.")
         # Load the sheet
        sheet = pd.read_excel(self.file_path, sheet_name=sheet_name)
        # Check if the sheet is empty
        if sheet.empty:
            raise ValueError(f"Sheet '{sheet_name}' is empty.")
     
        return sheet