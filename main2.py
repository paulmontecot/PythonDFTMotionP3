import getFeaturesFromFile
import getFeaturesWindows
import plot
from PCA import PCA
import pandas as pd
import glob
import MathUtilities
import os, fnmatch
datatype = 'accX'
directory = r'C:\Users\CRI User\Documents\GitHub\PythonDFTMotionP3\data'
path = r'C:\Users\CRI User\Documents\GitHub\PythonDFTMotionP3\data'
pattern = "*jerk*"

def runcode():
    #set up empty Dataframes
    dfbad = pd.DataFrame()
    dfgood = pd.DataFrame()
    #Go thru the files and extract them depending on the pattern
    for filename in os.listdir(directory):
        if fnmatch.fnmatch(filename, pattern):
            #get Data
            df = pd.DataFrame()
            df = df.append(pd.DataFrame(getFeaturesFromFile.datafromfile(path + '\\' + filename)), ignore_index=True)
            df.columns = ['time', 'accX', 'accY', 'accZ', 'gyrX', 'gyrY', 'gyrZ', 'magX', 'magY', 'magZ']
            #Select and set up Data
            data = df[datatype]
            integral = MathUtilities.integral(df, data)
            derivate = MathUtilities.derivData(df, data)
            angle = MathUtilities.angle(df, df.accX, df.accZ)
            #Get Features by Window
            Xbad,Ybad = getFeaturesWindows.getFeaturesWindows(angle, 1)
            #Create DataFrame with Bad Examples
            dfxbad = pd.DataFrame(Xbad)
            dfxbad.columns = ['DC', 'energy', 'entropyDFT', 'Deviation']
            dfybad = pd.DataFrame(Ybad)
            dfybad.columns = ['target']
            dfbad = dfbad.append(pd.concat([dfxbad,dfybad],axis=1))
        else:
            #get Data
            df = pd.DataFrame()
            df = df.append(pd.DataFrame(getFeaturesFromFile.datafromfile(path + '\\' + filename)), ignore_index=True)
            df.columns = ['time', 'accX', 'accY', 'accZ', 'gyrX', 'gyrY', 'gyrZ', 'magX', 'magY', 'magZ']
            #Select and set up Data
            data = df[datatype]
            integral = MathUtilities.integral(df, data)
            derivate = MathUtilities.derivData(df, data)
            angle = MathUtilities.angle(df, df.accX, df.accZ)
            #Get Features by Window
            Xgood, Ygood = getFeaturesWindows.getFeaturesWindows(angle, 0)
            #Create DataFrame with Bad Examples
            dfxgood = pd.DataFrame(Xgood)
            dfxgood.columns = ['DC', 'energy', 'entropyDFT', 'Deviation']
            dfygood = pd.DataFrame(Ygood)
            dfygood.columns = ['target']
            dfgood = dfgood.append(pd.concat([dfxgood, dfygood], axis=1))
    #Create Final DataFrame
    dfinal = pd.concat([dfgood, dfbad], axis=0)
    print (dfinal)
    plot.plotfeatures(dfinal)

runcode()
