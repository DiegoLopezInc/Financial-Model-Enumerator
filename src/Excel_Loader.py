import pandas as pd

class ExcelLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_sheet(self, sheet_name):
        return pd.read_excel(self.file_path, sheet_name=sheet_name)