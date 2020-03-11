import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model, metrics

data = pd.read_csv (r'C:\Users\ASUS-PC\Desktop\12s0217.csv')
df = pd.DataFrame(data, rows= ['Commodity','Mozzarella'])
print(df)
X = data.data 
y = data.target

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

reg = linear_model.LinearRegression() 
reg.fit(X_train, y_train)

print('Coefficients: \n', reg.coef_)
print('Variance score: {}'.format(reg.score(X_test, y_test)))

plt.style.use('fivethirtyeight')

plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
            color = "green", s = 10, label = 'Train data') 

plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
            color = "blue", s = 10, label = 'Test data') 

plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2)

plt.legend(loc = 'upper right')
plt.title("Residual errors")
plt.show()