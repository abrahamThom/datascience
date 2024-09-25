import numpy as np
import pandas as pd
student = pd.read_csv('student_scores.csv')
print(student.head())
student.describe()
student.info()
import matplotlib.pyplot as plt
Xax = student.iloc[:,0]
Yax = student.iloc[:,1]
plt.scatter(Xax,Yax)
plt.xlabel("No. of hours")
plt.ylabel("Score")
plt.title("Student scores")
plt.show()
x = student.iloc[:,:-1]
y = student.iloc[:,1]
print('x values : ')
print(x)
print('y values : ')
print(y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
print(x_train)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
print('INTERCEPT = ',regressor.intercept_)
print('CO-EFFICIENT = ',regressor.coef_)
y_pred = regressor.predict(x_test)
for(i,j) in zip(y_test,y_pred):
 if i == j:
     continue
 print("Actual value : ",i,"Predicted value : ",j)
print("Number of mislabeled points from test data set : ", (y_test != y_pred).sum())