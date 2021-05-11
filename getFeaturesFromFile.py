import glob
import os
import numpy as np
import getFeaturesWindows
dataWindow = 30
def datafromfile(file):
    #get data
        curFile = open(file,"r")
        dataFile = curFile.read().split("\n")
        rowData = np.empty((1, 10))  # [time, accX, accY, accZ, gyrX, gyrY, gyrX, magY, magY, magZ]
        rowData[:] = np.NaN
        if len(dataFile)>= dataWindow:
            for j in range(1,len(dataFile)):
                data = dataFile[j].split(",")
                if (len(data)==10):
                    rowData = np.append(rowData, [[float(data[0]), float(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5]),float(data[6]),float(data[7]),float(data[8]),float(data[9])]], axis=0)
            rowData = rowData[1:, :]
            return(rowData)
            curFile.close()

