from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[10],[20],[30],[40],[50]])
Y = np.array([72,81,88,94,100])

model = LinearRegression()
model.fit(X,Y)
print(model.coef_)
print('--------------')
coef = model.coef_[0]
intercept = model.intercept_
print(f'계수:{coef}, y절편:{intercept}')

y_predicted = 10*coef+intercept
print(y_predicted)

y_predicted = model.predict(X)
print(y_predicted)
