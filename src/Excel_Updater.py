import pandas as pd

class ExcelUpdater:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_excel(file_path)

    def update_value(self, label, new_value):
        # Check if the label exists in the DataFrame
        if label in self.df.columns:
            self.df.loc[self.df['Label'] == label, 'Value'] = new_value
        else:
            print(f"Label '{label}' not found in the DataFrame.")

    def copy_cell_styles(self, new_file_path):
        # Copy cell styles from the original Excel file to the new Excel file
        with pd.ExcelWriter(new_file_path, engine='openpyxl') as writer:
            for sheet_name in self.df.columns:
                # if value is Nan, skip and go to the next row
                for index, row in self.df.iterrows():
                    if pd.isna(row['Value']):
                        continue
                    # if value is a string, copy the cell style
                    if isinstance(row['Value'], str):
                        self.df.to_excel(writer, sheet_name=sheet_name, index=False)

    def save(self, new_file_path):
        self.df.to_excel(new_file_path, index=False)