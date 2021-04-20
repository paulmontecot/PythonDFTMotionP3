#from MathCurvesUtilities import *
import cmath
import math
import numpy as np
import MathCurvesUtilities


def getFeatures(rowData) :
    # Get data
    n = rowData.shape[0]
    ramp = np.linspace(1,100,num=n)
    time = rowData[:,0]*ramp
    accX = rowData[:,1]*ramp
    accY = rowData[:,2]*ramp
    accZ = rowData[:,3]*ramp
    gyrX = rowData[:,4]*ramp
    gyrY = rowData[:,5]*ramp
    gyrZ = rowData[:,6]*ramp
    magX = rowData[:,7]*ramp
    magY = rowData[:,8]*ramp
    magZ = rowData[:,9]*ramp
    #time = rowData[:,6] - rowData[0,6] # Time origin

    absDFTData = np.empty((n, 10))  # matrix containing DFT data from input data
    absDFTData[:] = np.NaN
    for i in range(n):
        for j in range(10):
            absDFTData[i, j] = np.absolute(DFT(rowData[:, j], i))
    print(absDFTData)
    print(absDFTData)

    def getAllDerivateFeatures(rowData):
        X_ = getFeatures(rowData)
        DFT = MathCurvesUtilities(DFT)
        EntropyDFT = MathCurvesUtilities(EntropyDFT)
        TimeIntegral = MathCurvesUtilities(TimeIntegral)
        IntegralData = MathCurvesUtilities(integraldata)
        DoubleIntegralData = MathCurvesUtilities(DoubleIntegralData)
        derivData = MathCurvesUtilities(derivData)
        doubleDerivData = MathCurvesUtilities(doubleDerivData)

        X_.appendgetFeatures(DFT, EntropyDFT, TimeIntegral, IntegralData, DoubleIntegralData, derivData, doubleDerivData)
