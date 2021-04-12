import glob
import os
import numpy as np
import getFeaturesWindows
import getFeature
dataWindow = 30
ld = 8
tag = "jerkorder"
out = 1
def datafromfile(tag):
    path = (r"C:\Users\CRI Paris\PycharmProjects\DFTMotionFeatures\DataCollection\Movuino-recording-"+tag+".dat")
    for i in glob.glob(path):
        curFile = open(i,"r")
        dataFile = curFile.read().split("\n")

        rowData = np.empty((1, 7))  # [accX, accY, accZ, gyrX, gyrY, gyrZ, time]
        rowData[:] = np.NaN

        if len(dataFile)>= dataWindow:
            for j in range(1,len(dataFile)):
                data = dataFile[j].split(",")
                if (len(data)==ld):
                    rowData = np.append(rowData, [[float(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5]), float(data[6]),float(data[7])]], axis=0)
            rowData = rowData[1:, :]
            return(rowData)

                    #print(rowData)
#datafromfile(tag)
def getallfeatures(tag,out):
    datafromfile(tag)
    data = datafromfile(tag)
    #print(data)
    X=getFeaturesWindows.getFeaturesWindows(data,out)
    print(X)
    #return(getFeaturesWindows.getFeaturesWindows(data,out))
getallfeatures(tag,out)

