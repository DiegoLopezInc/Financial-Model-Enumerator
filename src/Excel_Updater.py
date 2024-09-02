import pandas as pd

class DataUpdater:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_excel(file_path)

    def update_value(self, label, new_value):
        self.df.loc[self.df['Label'] == label, 'Value'] = new_value

    def save(self, new_file_path):
        self.df.to_excel(new_file_path, index=False)