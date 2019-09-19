# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:06:42 2019

@author: maily
"""
import os
import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_log_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR 
from sklearn.neural_network import multilayer_perceptron
from sklearn.linear_model import ridge_regression

data_path = "..\data"
df = pd.read_csv(os.path.join(data_path,"Train.csv"))
all_columns = df.columns.tolist()
categorical_vars = ["weather_type","weather_description"]

df.loc[df["is_holiday"] == "None","is_holiday"] = 0
df.loc[df["is_holiday"] != 0,"is_holiday"] = 1

#df = pd.get_dummies(df, columns = categorical_vars)
#df = df.loc[:,['date_time','is_holiday','air_pollution_index','humidity','wind_speed',
#               'wind_direction', 'visibility_in_miles', 'dew_point', 'temperature',
#               'rain_p_h', 'snow_p_h', 'clouds_all', 'traffic_volume']]
df = df.loc[:,['date_time',"weather_type","weather_description",'traffic_volume']]
df["date_time"] = pd.to_datetime(df["date_time"])
df["hour"] = df["date_time"].dt.hour
df["weekday"] = df["date_time"].dt.weekday
df["week"] = df["date_time"].dt.week
df["month"] = df["date_time"].dt.month
df["year"] = df["date_time"].dt.year
df = pd.get_dummies(df,columns = ["hour","weekday","week","month","weather_type","weather_description"])
df_X = df.loc[:, df.columns != 'date_time']
df_X = df_X.loc[:, df_X.columns != 'traffic_volume']
df_Y = df["traffic_volume"]

train_X, test_X, train_Y, test_Y = train_test_split(df_X, df_Y, test_size = 0.33, shuffle = True)
model = RandomForestRegressor()
model = multilayer_perceptron.MLPRegressor()
model.fit(train_X,train_Y)
max(0,100-math.sqrt(mean_squared_log_error(train_Y, model.predict(train_X))) )
max(0,100- math.sqrt(mean_squared_log_error(test_Y, model.predict(test_X))) )
plt.boxplot(df["traffic_volume"])
