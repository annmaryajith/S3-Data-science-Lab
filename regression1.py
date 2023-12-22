import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

data = pd.read_csv('Salary_Data.csv')
x = data['YearsExperience'].values.reshape(-1, 1)
y = data['Salary'].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
regressor = LinearRegression()
regressor.fit(x_train, y_train)
print(regressor.predict(x_test))
V = regressor.predict(x_train)
r2 = r2_score(y_train, V)
print("\nR squared:", r2)
plt.scatter(x_test, y_test, color="black", label="data points")
plt.plot(x_train, V, color="blue", linewidth=3, label="Regression line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

