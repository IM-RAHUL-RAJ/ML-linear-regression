# -*- coding: utf-8 -*-
"""linear-regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13KfdYV8RIi2_AE1Fd4lGLQ2AOkBgXlBx
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import mean_squared_error

dataset=pd.read_csv('/content/Salary_Data.csv')
dataset

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
print(x)

print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

x_train

y_train

y_pred=regressor.predict(x_test)
y_pred1=regressor.predict(x_train)

y_pred1

y_pred

plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train))
plt.show()

plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regressor.predict(x_train))
plt.show()

print(regressor.coef_)

print(regressor.intercept_)

