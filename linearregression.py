import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([64,75,68,73,78,82,76,85,71,88]).reshape(-1,1)
y = np.array([17,27,15,24,39,44,30,48,19,47])

regressor = LinearRegression()
regressor.fit(x, y)
slope = regressor.coef_[0]
intercept = regressor.intercept_
print(f"Slope(Coefficient): {slope}")
print(f"Intercept: {intercept}")