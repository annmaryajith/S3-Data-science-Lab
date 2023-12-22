import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

california_housing = fetch_california_housing()
df = pd.DataFrame(data = california_housing.data, columns=california_housing.feature_names)
df["Target"] = california_housing.target
x = df.drop('Target', axis=1)
y = df['Target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
regressor = LinearRegression()
regressor.fit(x_train, y_train)
v = regressor.predict(x_test)
mse = mean_squared_error(y_test, v)
print("Mean squared error: ", mse)
