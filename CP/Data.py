import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = r'UofT\STA130\CP\CSCS_data_anon.csv'  # Replace with your file path
data = pd.read_csv(file_path, low_memory=False)

# Displaying the first 100 entries in the "LONELY_ucla_loneliness_scale_score" column
loneliness_scores = data['LONELY_ucla_loneliness_scale_score'].head(100)
print(loneliness_scores)
