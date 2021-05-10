import getFeaturesFromFile
import getFeaturesWindows
from getFeaturesFromFile import getallfeatures
from PCA import PCA
import numpy as np
import pandas as pd
import glob
import MathUtilities
import matplotlib.pyplot as plt
path = r'C:\Users\CRI User\Documents\GitHub\PythonDFTMotionP3\DataCollection'
files = glob.glob(path + '/*jerk*')
df = pd.DataFrame()
for file in files:
    df = df.append(pd.DataFrame(getFeaturesFromFile.datafromfile(file)), ignore_index=True)
df.columns = ['time', 'accX', 'accY', 'accZ', 'gyrX', 'gyrY', 'gyrZ', 'magX', 'magY', 'magZ']
print(df)
    #getfeatures
    #X,Y =getFeaturesWindows.getFeaturesWindows(data,out)
    #return(X,Y)
data = df['accX']
integral = MathUtilities.integral(df,data)
derivate = MathUtilities.derivData(df,data)
angle = MathUtilities.angle(df,df.accX,df.accZ)
#print('yes',integral)
#print('heh',derivate)
# print('angle',angle)
# print(len(integral))
# print(len(derivate))
#print(df['time'])


#data = rowdata[0:2]
#print('integ',data)

# fig = plt.figure(figsize=(25,10))
# ax1 = fig.add_subplot(1, 3, 1)
# ax2 = fig.add_subplot(1, 3, 2)
# ax3 = fig.add_subplot(1,3,3)
# fig.tight_layout(pad=3)
# ax1.plot(df['time'], integral, label='Integral Acc')
# ax2.plot(df['time'], derivate, label='Derivate Acc')
# ax3.plot(df['time'], angle, label='Angle XZ')
# ax1.set_xlabel('Time (mS)')
# ax1.set_ylabel('Int')
# ax1.set_title('Integral')
# ax1.legend()
# ax2.set_xlabel('Time (mS)')
# ax2.set_ylabel('Int')
# ax2.set_title('Derivate')
# ax2.legend()
# ax3.set_xlabel('Time (mS)')
# ax3.set_ylabel('Value')
# ax3.set_title('Angle')
# plt.show()

X= getFeaturesWindows.getFeaturesWindows(data,1)
dfx = pd.DataFrame(X)
dfx.columns = ['DC','energy','entropyDFT','Deviation']
print(dfx)






































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