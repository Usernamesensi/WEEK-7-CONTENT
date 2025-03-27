import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("balkirat.csv")  
df.columns = df.columns.str.strip()  

correct_column_name = "Temperature (°C)"
humidity_column_name = "Humidity (%)"

min_temp_threshold = df[correct_column_name].quantile(0.05)
max_temp_threshold = df[correct_column_name].quantile(0.95)
df_filtered = df[(df[correct_column_name] >= min_temp_threshold) & (df[correct_column_name] <= max_temp_threshold)]

X = df_filtered[correct_column_name].values.reshape(-1, 1)  
y = df_filtered[humidity_column_name].values  

model = LinearRegression()
model.fit(X, y)

test_temps = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
predicted_humidity = model.predict(test_temps)

plt.scatter(X, y, color='blue', label="Filtered Data")  
plt.plot(test_temps, predicted_humidity, color='red', label="Trend Line") 
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Temperature vs Humidity (Filtered Data)")
plt.legend()
plt.show()