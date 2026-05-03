## NAME  : D DEVIKA
## REG NO: 212224100010


## Title

Car Price Prediction using Machine Learning

## About

This project predicts the price of a car based on its manufacturing year using Linear Regression. It demonstrates how data analytics can be used to understand trends and make predictions.

## Algorithm

## Step 1: Start

Begin the execution of the program.

## Step 2: Import Libraries

Import required Python libraries:

NumPy for numerical operations

LinearRegression from sklearn for model building

## Step 3: Define Dataset

Create input dataset (customer age)

Create output dataset (spending amount)

## Step 4: Preprocess Data

Convert input data into array format

Reshape the input data into 2D array for model compatibility

## Step 5: Create Model

Initialize the Linear Regression model

## Step 6: Train Model

Fit the model using input (age) and output (spending) data

The model learns the relationship between variables

## Step 7: Input New Data

Provide a new value (example: age = 28)

## Step 8: Predict Output

Use the trained model to predict customer spending

## Step 9: Display Result

Print the predicted spending value

## Step 10: Stop

End the execution of the program

## Code

import numpy as np
from sklearn.linear_model import LinearRegression

year = np.array([2010, 2012, 2015, 2018, 2020]).reshape(-1, 1)
price = np.array([200000, 250000, 300000, 400000, 500000])

model = LinearRegression()
model.fit(year, price)

predicted_price = model.predict([[2022]])

print("Predicted Car Price:", predicted_price)

## Screenshot

<img width="1920" height="1200" alt="Screenshot (201)" src="https://github.com/user-attachments/assets/0f5a72e9-7b53-4941-81f5-05c8af34ec20" />


## Conclusion

This project demonstrates how Machine Learning can be used to predict car prices based on year. It shows the importance of data in making future predictions.
