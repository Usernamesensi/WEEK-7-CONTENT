import pandas as pd

df = pd.read_csv("balkirat.csv")  

df.columns = df.columns.str.strip()

print(df.columns)

correct_column_name = "Temperature (°C)"  

min_temp_threshold = df[correct_column_name].quantile(0.05)
max_temp_threshold = df[correct_column_name].quantile(0.95)

df_filtered = df[(df[correct_column_name] >= min_temp_threshold) & (df[correct_column_name] <= max_temp_threshold)]
print(df_filtered.head())