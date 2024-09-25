import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
advertising = pd.read_csv('Company_data.csv')
advertising.head()
advertising.describe()
advertising.info()
print("Feature values : ")
x = advertising.iloc[:, :-1]
print(x)
print("Target variable values : ")
y = advertising.iloc[:, -1]
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
print("intercept is : ")
print(regressor.intercept_)
print("Co-efficients are : ")
print(regressor.coef_)
y_pred = regressor.predict(x_test)
for(i,j) in zip(y_test,y_pred):
  if i!=j:
    print("Actual values : ",i," Predicted values : ",j)
print("Number of mislabeled points from test data set : ",(y_test !=y_pred).sum())
#MSE,MAE,RMSE and R-Squared are mainly used metrics to evaluate
#the prediction error rates and model performance in regression analysis.
from sklearn import metrics
print("Mean Absolute error :",
metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared error :", metrics.mean_squared_error(y_test,y_pred))

print("Root Mean Squared error :",
np.sqrt(metrics.mean_squared_error(y_test,y_pred)))