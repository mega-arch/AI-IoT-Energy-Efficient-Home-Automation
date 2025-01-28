# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Sample dataset for ambient light intensity and predicted light intensity
data = {
    'Ambient_Light_Intensity': [100, 200, 300, 400, 500, 600, 700],
    'Optimal_Light_Intensity': [50, 100, 150, 200, 250, 300, 350]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Features and target
X = df['Ambient_Light_Intensity'].values.reshape(-1, 1)  # Input: Ambient Light Intensity
y = df['Optimal_Light_Intensity'].values  # Output: Optimal Light Intensity

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the optimal light intensity
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plot the predictions
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Predicted Data')
plt.title('Ambient Light vs. Optimal Light Intensity')
plt.xlabel('Ambient Light Intensity')
plt.ylabel('Optimal Light Intensity')
plt.legend()
plt.show()
