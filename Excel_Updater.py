# Update the Excel file with the new values
# Let's assume 'Revenue' is in the first column and the value to update is in the next column
new_revenue_value = 50000  # Example value to update
df.loc[df['Label'] == 'Revenue', 'Value'] = new_revenue_value

# Save the modified DataFrame back to an Excel file
df.to_excel('updated_financial_model.xlsx', index=False)

