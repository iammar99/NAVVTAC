import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# ===============| 1.) MTCARS |===============

# ---------| OLS Method |---------

mtcars = sm.datasets.get_rdataset("mtcars").data

X_mtcars = mtcars[["hp","wt","qsec","drat"]]
Y_mtcars = mtcars["mpg"]

x_mtcars = sm.add_constant(X_mtcars)
model_mtcars = sm.OLS(Y_mtcars,x_mtcars).fit()
print(model_mtcars.summary())



# ---------| Linear Regression Method |---------

lr_mtcars = LinearRegression()
lr_mtcars.fit(X_mtcars,Y_mtcars)
print(lr_mtcars.coef_)
print(lr_mtcars.intercept_)



# ===============| 2.) IRIS |===============

# ---------| OLS Method |---------

iris = sm.datasets.get_rdataset("iris").data

X_iris = iris[["Sepal.Width","Petal.Width","Sepal.Length"]]
Y_iris = iris["Petal.Length"]

x_iris = sm.add_constant(X_iris)
model_iris = sm.OLS(Y_iris,x_iris).fit()
print(model_iris.summary())



# ---------| Linear Regression Method |---------

lr_iris = LinearRegression()
lr_iris.fit(X_iris,Y_iris)
print(lr_iris.coef_)
print(lr_iris.intercept_)





# ===============| 3.) Diamonds  |===============

# ---------| OLS Method |---------

diamonds = sns.load_dataset("diamonds")

diamonds_encoded = pd.get_dummies(diamonds, drop_first=True)
X_diamonds = diamonds_encoded.drop("price", axis=1)
Y_diamonds = diamonds_encoded["price"]

x_diamonds = sm.add_constant(X_diamonds)

model_diamonds = sm.OLS(Y_diamonds, x_diamonds.astype(float)).fit()

print(model_diamonds.summary())

# ---------| Linear Regression Method |---------

X_diamonds = diamonds[["carat","cut","color","clarity"]]
Y_diamonds = diamonds["price"]
lr_iris = LinearRegression()
lr_iris.fit(X_diamonds,Y_diamonds)
print(lr_iris.coef_)
print(lr_iris.intercept_)


