import numpy as np
import math
from getFeature import getFeatures
import scratch
X = []
Xtemp = []
L = 42
dataWindow = 23
stride = dataWindow / 2


def getFeaturesWindows(data, out):
    Xtemp = []

    lenDat_ = len(data)
    i = 0
    targetcount = 0
    while i < lenDat_:
        indStart_ = i
        indStop_ = i + dataWindow
        if(indStop_  >= lenDat_) :
            indStop_ = lenDat_ - 1
        i += math.floor(dataWindow / 2.0)
        #X_ = getFeatures(data[indStart_:indStart_ + dataWindow, :])
        X_ = scratch.getFeatures_Detection(data[indStart_:indStart_ + dataWindow, :])
        targetcount += 1
        if Xtemp == []:
            Xtemp = [X_]  # generate data set matrix
        else:
            Xtemp = np.append(Xtemp, [X_], axis=0)  # update data set matrix
        if np.where(np.isnan(Xtemp))[0].size > 0:
            break

        if len(Xtemp[:]) > 1000:
            if X == []:
                X = Xtemp
                Xtemp = []
            else:
                X = np.append(X, Xtemp, axis=0)
                Xtemp = []

    if out == 1:
        Y =np.ones((targetcount))
    if out == 0:
        Y =np.zeros((targetcount))
    #print(Y)









