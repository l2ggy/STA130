import pandas as pd

# Reload the original CSV file to access all columns
file_path = r'UofT\STA130\CP\CSCS_data_anon.csv'
data = pd.read_csv(file_path, low_memory=False)

# List all column names in the dataset
all_columns = data.columns.tolist()
print(all_columns)
