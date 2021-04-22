import numpy as np
import math
from getFeature import getFeatures
import scratch

L = 42
dataWindow = 23
stride = dataWindow / 2


def getFeaturesWindows(data, out):

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
        return(X_)
    #print(targetcount)
    #print(X_)
 #       if Xtemp == []:
 #           Xtemp = [X_]  # generate data set matrix
  #      else:
  #          Xtemp = np.append(Xtemp, [X_], axis=0)
  #      if np.where(np.isnan(Xtemp))[0].size > 0:
  #          break
  #      if len(Xtemp[:]) > 1:
 #           if X==[]:
  #              X = Xtemp
 #               Xtemp = []
 #           else :
 #               X = np.append(X,Xtemp,axis=0)
 #               Xtemp = []


 #   if Xtemp!=[]:
 #       if X==[]:
 #           X = Xtemp
 #           Xtemp = []
  #      else :
 #           X = np.append(X,Xtemp,axis=0)
 #           Xtemp = []
 #   Y = np.append(Y,np.zeros(targetcount)))  # update output vector with Y=0 examples






