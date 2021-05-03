import numpy as np
import math
from getFeature import getFeatures
import scratch
X = []
dataWindow = 8
def getFeaturesWindows(data, out):
    Xtemp = []
    lenDat_ = len(data)
    i = 0
    targetcount = 0
    #Window rolling
    while i < (lenDat_):
        indStart_ = i
        indStop_ = i + dataWindow
        if(indStop_  >= lenDat_) :
            indStop_ = lenDat_ - 1
        #i += math.floor(dataWindow / 2.0)
        #Get Vector
        if lenDat_ - dataWindow < indStart_ + dataWindow:
            break
        else:
            X_ = scratch.getFeatures_Detection(data[indStart_:indStart_ + dataWindow, :])
            targetcount += 1
            i += math.floor(dataWindow / 2.0)
        if Xtemp == []:
            Xtemp = [X_]  # generate data set matrix
        else:
            Xtemp = np.append(Xtemp, [X_], axis=0)  # update data set matrix
        if np.where(np.isnan(Xtemp))[0].size > 0:
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









