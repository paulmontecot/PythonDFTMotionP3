#from MathCurvesUtilities import *
import cmath
import math
import numpy as np

def fetFeature(rowData) :
    # Get data
    n = rowData.shape[0]
    ramp = np.linspace(1,100,num=n)
    time = rowData[:,0]*ramp
    accX = rowData[:,0]*ramp
    accY = rowData[:,1]*ramp
    accZ = rowData[:,2]*ramp
    gyrX = rowData[:,3]*ramp
    gyrY = rowData[:,4]*ramp
    gyrZ = rowData[:,5]*ramp
    magX = rowData[:,6]*ramp
    magY = rowData[:,7]*ramp
    magZ = rowData[:,8]*ramp
    #time = rowData[:,6] - rowData[0,6] # Time origin

    absDFTData = np.empty((n, 8))  # matrix containing DFT data from input data
    absDFTData[:] = np.NaN
    for i in range(n):
        for j in range(8):
            absDFTData[i, j] = np.absolute(DFT(rowData[:, j], i))
    print
    absDFTData
    print
    absDFTData.shape