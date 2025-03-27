import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = np.loadtxt("balkirat.csv", delimiter=",", skiprows=1)  
X = data[:, 0].reshape(-1, 1)  
y = data[:, 1]  

model = LinearRegression()
model.fit(X, y)

test_temps = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
predicted_humidity = model.predict(test_temps)

plt.scatter(X, y, color='blue', label="Actual Data")  
plt.plot(test_temps, predicted_humidity, color='red', label="Trend Line")  
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Temperature vs Humidity (Trend Analysis)")
plt.legend()
plt.show()