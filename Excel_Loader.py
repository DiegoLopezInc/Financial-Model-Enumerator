import pandas as pd

# Load the Excel file
excel_file = 'financial_model.xlsx'
df = pd.read_excel(excel_file, sheet_name='Sheet1')  # Specify the sheet name

# print the dataframe
print(df)
