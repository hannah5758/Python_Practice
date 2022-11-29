from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[10,66],[20,85],[30,86],[40,92],[50,96]])
x_test = np.array([[16, 77] , [25, 89]])
Y = np.array([72,81,88,94,100])

model = LinearRegression()
model.fit(X,Y)

y_predicted = model.predict(X)
y_test_predict = model.predict(x_test)
print(y_predicted)
print(y_test_predict)

coef = model.coef_
intercept = model.intercept_
print(f'계수: {coef}, y절편: {intercept}')
temp = X[0][0] * coef[0] + X[0][1] * coef[1] + intercept
print(temp)
