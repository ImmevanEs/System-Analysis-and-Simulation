# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:31:29 2023

Small data set example 

@author: immev
"""

# ---- Importing data sets  ----

import csv
import pandas as pd
import scipy.optimize
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("PowerVsSpeed.csv")
data.columns 
x_blue = list(data.X_blue)
y_blue = list(data.Y_blue)
x_red = list(data.X_red)
y_red = list(data.Y_red)
x_green = list(data.X_green)
y_green = list(data.Y_green)
x_purple = list(data.X_purple)
y_purple = list(data.Y_purple)

x_b = list()
sum_blue = 0
for i in range(len(x_blue)):
    if x_blue[i] > 1.25 and x_blue[i] < 32.5:
        x_b.append(x_blue[i])
        sum_blue = sum_blue + y_blue[i]
avg_blue = sum_blue/len(x_b)  
        
x_r = list()
sum_red = 0
for i in range(len(x_red)):
    if x_red[i] > 2.0 and x_red[i] < 21.25:
        x_r.append(x_red[i])
        sum_red = sum_red + y_red[i]
avg_red = sum_red/len(x_r)  
        
x_g = list()
sum_green = 0
for i in range(len(x_green)):
    if x_green[i] > 2.00 and x_green[i] < 16.25:
        x_g.append(x_green[i])
        sum_green = sum_green + y_green[i]
avg_green = sum_green/len(x_g)  
        
x_p = list()
sum_purple = 0
for i in range(len(x_purple)):
    if x_purple[i] > 2.5 and x_purple[i] < 12.5:
        x_p.append(x_purple[i])
        sum_purple = sum_purple + y_purple[i]
avg_purple = sum_purple/len(x_p)  

speeds = np.linspace(0.6, 1.5, 4)
powers = [avg_blue, avg_red, avg_green, avg_purple]
def parabola(x, a, b, c):
    return a*x**2 + b*x + c

fit_params, pcov = scipy.optimize.curve_fit(parabola, speeds, powers)
for fit_param in zip(fit_params):
    print(fit_param)

powers_fit = parabola(speeds, fit_params[0], fit_params[1], fit_params[2])
plt.plot(speeds, powers_fit,marker="o")


