import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler


class NN:
    def __init__(self,train,val):
        self._train = train
        self._val= val
   
    def Training(self):

        dataMat = np.array(self._train)
        X=dataMat[:,1:-1]
        y = dataMat[:,0]
        scaler = StandardScaler() 
        scaler.fit(X) 
        X = scaler.transform(X)
        clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(50,20), random_state=1) 
        clf.fit(X, y)
    
        valMat = np.array(self._val)
        X2=valMat[:,1:-2]
        y2 = valMat[:,0]
        scaler = StandardScaler() 
        scaler.fit(X2) 
        X2 = scaler.transform(X2)
        print(clf.score(X2,y2))
        
