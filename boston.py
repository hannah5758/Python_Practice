from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

boston = datasets.load_boston()

boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)
print(boston_df)
print(boston_df.isnull().sum())

boston_df['PRICE'] = boston.target

x = np.array(boston_df.RM).reshape(-1,1)
y = np.array(boston_df.PRICE).reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state=5)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

model = LinearRegression()
model.fit(x_train,y_train)

y_train_predicts = model.predict(x_train)
mse = mean_squared_error(y_train, y_train_predicts)
rmse = np.sqrt(mse)

print(f'tr mse : {mse}, rmse : {rmse}')

y_test_predicts = model.predict(x_test)
te_mse = mean_squared_error(y_test, y_test_predicts)
te_rmse = np.sqrt(mse)

print(f'te mse : {te_mse}, rmse : {te_rmse}')

plt.scatter(x_test,y_test,color="black")
plt.plot(x_test,y_test_predicts,color="blue", linewidth=3)

plt.show()

