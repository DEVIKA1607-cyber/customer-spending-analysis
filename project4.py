import numpy as np
from sklearn.linear_model import LinearRegression

# Input data (age)
age = np.array([20, 25, 30, 35, 40]).reshape(-1, 1)

# Output data (spending)
spending = np.array([2000, 3000, 4000, 5000, 6000])

# Model
model = LinearRegression()
model.fit(age, spending)

# Prediction
predicted_spending = model.predict([[28]])

print("Predicted Spending:", predicted_spending)
