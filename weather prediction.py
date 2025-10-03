import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv("weather.csv")

# Drop missing values
data = data.dropna()

# Features (X) - select useful numeric columns
X = data[['MinTemp', 'MaxTemp', 'Humidity9am', 'Humidity3pm', 
          'Pressure9am', 'Pressure3pm', 'WindSpeed9am', 'WindSpeed3pm']]

# Target (y) - predict afternoon temperature
y = data['Temp3pm']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Plot Actual vs Predicted
plt.scatter(y_test, y_pred, color="blue", alpha=0.5)
plt.xlabel("Actual Temp3pm")
plt.ylabel("Predicted Temp3pm")
plt.title("Weather Prediction (Multiple Linear Regression)")
plt.show()

# Example prediction
new_data = pd.DataFrame([[15, 25, 70, 50, 1012, 1010, 10, 15]],
                        columns=['MinTemp', 'MaxTemp', 'Humidity9am', 'Humidity3pm', 
                                 'Pressure9am', 'Pressure3pm', 'WindSpeed9am', 'WindSpeed3pm'])

predicted_temp = model.predict(new_data)
print(f"Predicted Temp3pm: {predicted_temp[0]:.2f}°C")
