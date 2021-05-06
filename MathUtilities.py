import numpy as np
import pandas as pd


def integral(df,data):
    integral = [0]
    for i in range(len(df.index) - 1):
        if i < 40:
            dt_ = df.time[i + 1] - df.time[i]
            integral_ = data[i] * dt_
            integral_ += (data[i + 1] - data[i]) * dt_ / 2.0
            integral.append(integral[i] + integral_)
    return(integral)

def derivData(df,data):
    derivData = [0]
    for i in range(len(df.index) - 1):
        if i == 0:
            derivData[i] = (data[i + 1] - data[i]) / (df.time[i + 1] - df.time[i])
        elif i == len(df.index) - 1:
            derivData[i] = (data[i] - data[i - 1]) / (df.time[i] - df.time[i - 1])
        else:
            derivData[i] = (data[i + 1] - data[i - 1]) / (df.time[i + 1] - df.time[i - 1])
    return(derivData)
