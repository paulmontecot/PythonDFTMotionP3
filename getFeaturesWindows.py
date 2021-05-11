import numpy as np
import math
import GetDFT
from getFeature import getFeatures
import scratch
X = []
dataWindow = 8
def getFeaturesWindows(data, out):
    print('activate')
    Xtemp = []
    X_ = []
    lenDat_ = len(data)
    i = 0
    targetcount = 0
    #Window rolling
    while i < (lenDat_-1):
        indStart_ = i
        indStop_ = indStart_ + dataWindow
        if(indStop_  >= lenDat_) :
            indStop_ = lenDat_ - 1
        if (indStop_ - indStart_ >= 2):
            X_ = GetDFT.getDFT(data[indStart_:indStop_])
            targetcount += 1
            i += math.floor(dataWindow / 2.0)
        if Xtemp == []:
            Xtemp = [X_]  # generate data set matrix
        else:
            Xtemp = np.append(Xtemp, [X_], axis=0)  # update data set matrix
        if np.where(np.isnan(Xtemp))[0].size > 0:
            print('break')
            break
    #get Categories (1/0)
    if out == 1:
        Y = np.ones(targetcount)
    if out == 0:
        Y = np.zeros(targetcount)
    return (Xtemp,Y)
    #Empty Vector
    if len(Xtemp[:]) > 1000:
        if X == []:
            X = Xtemp
            Xtemp = []
        else:
            X = np.append(X, Xtemp, axis=0)
            Xtemp = []









