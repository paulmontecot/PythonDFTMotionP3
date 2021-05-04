from getFeaturesFromFile import getallfeatures
from PCA import PCA
import numpy as np
import pandas as pd
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