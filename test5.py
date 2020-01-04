import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from weather_pred_4 import a as wdata


dataset = pd.read_csv('Road_14.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values


dataset2 = pd.read_csv('Sig_Timer.csv')
a = dataset2.iloc[:, :-1].values
b = dataset2.iloc[:, 1].values

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.01, random_state = 0)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)

regressor.fit(X, y)
regressor2 = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor2.fit(a, b)

y_pred = regressor.predict(wdata)
b_pred = regressor2.predict(y_pred.reshape(-1,1))


plt.title('Traffic Elapsed Time (Regression Model)')
plt.xlabel('Timestamp')
plt.ylabel('Time Taken')
plt.scatter(X[:, 0],y, color='red' )
plt.plot(wdata[:, 0], y_pred, color='blue')
plt.show()


plt.title('Traffic Elapsed Time (Regression Model)')
plt.xlabel('Time taken')
plt.ylabel('Traffic Signal Timer')
plt.plot(a, b, color='blue')
plt.scatter(y_pred, b_pred, color='red')
plt.show()





