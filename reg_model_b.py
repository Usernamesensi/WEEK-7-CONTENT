import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("balkirat2.csv", encoding="utf-8")

X = df[["Temperature (°C)"]]  
y = df["Humidity (%)"]  

model = LinearRegression()
model.fit(X, y)

print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")

plt.scatter(X, y, color="blue", label="Actual Data")

X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred = model.predict(X_range)

plt.plot(X_range, y_pred, color="red", label="Regression Line")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.legend()
plt.title("Temperature vs Humidity (Linear Regression)")
plt.show()