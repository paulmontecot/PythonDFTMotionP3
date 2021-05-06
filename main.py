import getFeaturesFromFile
from getFeaturesFromFile import getallfeatures
from PCA import PCA
import numpy as np
import pandas as pd
import glob
import MathUtilities
path = r'C:\Users\CRI User\Documents\GitHub\PythonDFTMotionP3\DataCollection'
files = glob.glob(path + '/*.dat')
df = pd.DataFrame()
for file in files:
    df = df.append(pd.DataFrame(getFeaturesFromFile.datafromfile(file)), ignore_index=True)
df.columns = ['time', 'accX', 'accY', 'accZ', 'gyrX', 'gyrY', 'gyrX', 'magY', 'magY', 'magZ']
print(df)
    #getfeatures
    #X,Y =getFeaturesWindows.getFeaturesWindows(data,out)
    #return(X,Y)
data = df['accX']
integral = MathUtilities.integral(df,data)
derivate = MathUtilities.derivData(df,data)
print('yes',integral)
print('heh',derivate)

#data = rowdata[0:2]
#print('integ',data)




















Xbad,Ybad = getallfeatures('jerk',0)
Xgood,Ygood = getallfeatures()



















#Create Dataset
dfx = pd.DataFrame(X)
dfy = pd.DataFrame(Y)
dfy.columns = ['target']
df = pd.concat([dfx,dfy],axis=1)
print (df)

#X = np.array(X)
Ureduce = PCA(X)
# # sio.savemat('../SVMVariable_Detection/Ureduce_Detection.mat', {"Ureduce":Ureduce}) # save Ureduce
Z = np.dot(Ureduce.T,X.T).T
Z = np.concatenate((np.ones((len(Y),1)),Z),axis=1)
print('pca', Z)

#print('z',Z)
#XY.to_csv('myFile.csv', sep = '\t')
#Z.to_csv('FeaturesVectorPC.csv', sep = '\t')