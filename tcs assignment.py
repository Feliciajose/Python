import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('gdpWorld.csv')

# Select the features (independent variables) that you want to use for prediction
selected_features = ['population', 'infant mortality', 'literacy', 'phones per 1000', 'arable', 'birth-rate']

X = data[selected_features]
y = data['GDP']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression Model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_pred = linear_model.predict(X_test)

# Random Forest Regression Model (Non-linear)
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

# Evaluate the models using Mean Squared Error (MSE)
linear_mse = mean_squared_error(y_test, linear_pred)
rf_mse = mean_squared_error(y_test, rf_pred)

# Compare the two models
print("Linear Model MSE:", linear_mse)
print("Random Forest Model MSE:", rf_mse)

# Plot the actual vs. predicted GDP for both models
plt.scatter(y_test, linear_pred, label='Linear Model', color='blue')
plt.scatter(y_test, rf_pred, label='Random Forest Model', color='red')
plt.xlabel("Actual GDP")
plt.ylabel("Predicted GDP")
plt.legend()
plt.show()
