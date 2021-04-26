from getFeaturesFromFile import getallfeatures
from PCA import PCA
import numpy as np
#tag = "jerk"
#out = 1


# Xgood, Ygood = getallfeatures('smooth',1)
# Xbad, Ybad = getallfeatures('jerk',0)
#print('là aussi',getallfeatures('jerk',1))
X =getallfeatures('jerk',0)
X = np.array(X)

Ureduce = PCA(X)
print('type',type(Ureduce))
print('type',type(X))
# sio.savemat('../SVMVariable_Detection/Ureduce_Detection.mat', {"Ureduce":Ureduce}) # save Ureduce
Z = np.dot(Ureduce.T,X.T).T
Z = np.concatenate((np.ones((len(Y),1)),Z),axis=1)

print('z',Z)
#XY.to_csv('myFile.csv', sep = '\t')
#Z.to_csv('FeaturesVectorPC.csv', sep = '\t')