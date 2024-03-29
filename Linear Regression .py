#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#importing the database
dataset=pd.read_csv('~/Desktop/PYTHON/Salary_Data.csv.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values

'''#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()
labelencoder_y=LabelEncoder()
y = labelencoder_y.fit_transform(y)'''

#Train and Test Data
from sklearn.cross_validation import train_test_split 
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=1/3, random_state=0)

'''#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X= StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)'''

#Fitting Simple Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the Test set results
y_pred = regressor.predict(X_test)

#Visualize Training Set
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train) , color='blue')
plt.title('Salary vs Experience(Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#Visualize Test Set
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train) , color='blue')
plt.title('Salary vs Experience(Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()