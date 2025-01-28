import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pickle

from termcolor import colored as cl
# pip install -U scikit-learn
from sklearn.model_selection import train_test_split

#Models
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import BayesianRidge
from sklearn.linear_model import ElasticNet

from sklearn import ensemble # better models



#Model analysis
from sklearn.metrics import explained_variance_score as evs
from sklearn.metrics import r2_score as r2





#Getting ready data
def data_preperation(file, column_x, column_y):
    data_file = pd.read_csv(file)
    data_file.dropna(inplace=True)
    x_var = data_file[column_x]
    y_var = data_file[column_y]
    x_train, x_test, y_train, y_test = train_test_split(x_var, y_var, test_size=0.2, random_state=0)
    return x_train, x_test, y_train, y_test
    
def model_quality(y_test, results):
    print(cl(f"Dispersion: {evs(y_test, results)}", "red", attrs=["bold"]))
    print(cl(f"Quadratic deviation: {r2(y_test, results)}", "yellow", attrs=["bold"]))
    return

def training_model(model, x_train, y_train):
    model.fit(x_train, y_train)
    return model

def test_model(model, x_test):
    result = model.predict(x_test)
    return result

file1 = "masinmacisanas/data/auto_simple.csv"
col_x1 = ["Volume", "Weight"]
col_y1 = ["CO2"]

file2 = "masinmacisanas/data/auto_imports.csv"
col_x2 = ["wheel-base", "length", "width", "height", "curb-weight", "engine-size", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg"]
col_y2 = ["price"]

file3 = "masinmacisanas/data/sslv.csv"
col_x3 = ["gads", "tilpums", "nobraukums"]
col_y3 = ["cena"]
#Prepare data
x_train, x_test, y_train, y_test = data_preperation(file3, col_x3, col_y3)

#Prepare model
model = ensemble.GradientBoostingRegressor()

model = training_model(model, x_train, y_train)
result = test_model(model, x_test)
print(model_quality(y_test, result))

# file1_x = [2000, 1.6, 500000]
# file1_res = 1000

# results_1 = test_model(model, file1_x)
# print(cl(f"{results_1}"))

