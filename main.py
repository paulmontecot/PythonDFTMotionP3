from getFeaturesFromFile import getallfeatures
#tag = "jerk"
#out = 1


Xgood, Ygood = getallfeatures('smooth',1)
Xbad, Ybad = getallfeatures('jerk',0)


Ureduce = PCA(X)
# sio.savemat('../SVMVariable_Detection/Ureduce_Detection.mat', {"Ureduce":Ureduce}) # save Ureduce
Z = np.dot(Ureduce.T,X.T).T
Z = np.concatenate((np.ones((len(Y),1)),Z),axis=1)