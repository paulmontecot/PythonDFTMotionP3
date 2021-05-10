import getFeaturesFromFile
import getFeaturesWindows
import plot
from PCA import PCA
import pandas as pd
import glob
import MathUtilities

#load files
path = r'C:\Users\CRI User\Documents\GitHub\PythonDFTMotionP3\DataCollection'
files = glob.glob(path + '/*smooth*')
df = pd.DataFrame()
for file in files:
    df = df.append(pd.DataFrame(getFeaturesFromFile.datafromfile(file)), ignore_index=True)
df.columns = ['time', 'accX', 'accY', 'accZ', 'gyrX', 'gyrY', 'gyrZ', 'magX', 'magY', 'magZ']
print(df)
data = df['gyrX']
integral = MathUtilities.integral(df,data)
derivate = MathUtilities.derivData(df,data)
angle = MathUtilities.angle(df,df.accX,df.accZ)
print('integral', integral)
print('derivate', derivate)
print('angle', angle)

X= getFeaturesWindows.getFeaturesWindows(angle,1)
dfx = pd.DataFrame(X)
dfx.columns = ['DC','energy','entropyDFT','Deviation']
print(dfx)

plot.plotfeatures(dfx)





































#Create Dataset
# dfx = pd.DataFrame(X)
# dfy = pd.DataFrame(Y)
# dfy.columns = ['target']
# df = pd.concat([dfx,dfy],axis=1)
# print (df)
#
# #X = np.array(X)
# Ureduce = PCA(X)
# # # sio.savemat('../SVMVariable_Detection/Ureduce_Detection.mat', {"Ureduce":Ureduce}) # save Ureduce
# Z = np.dot(Ureduce.T,X.T).T
# Z = np.concatenate((np.ones((len(Y),1)),Z),axis=1)
# print('pca', Z)

#print('z',Z)
#XY.to_csv('myFile.csv', sep = '\t')
#Z.to_csv('FeaturesVectorPC.csv', sep = '\t')