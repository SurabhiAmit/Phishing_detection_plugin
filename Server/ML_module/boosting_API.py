from sklearn.preprocessing import scale
import pickle
from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
import sys

#set s to the required input list
s=[-1,1,1,1,-1,-1,-1,-1]
X=np.array([s],dtype=np.int)
file1 = open(r'.\BestModel_Boosting.pkl', 'rb')
best_mlp = pickle.load(file1)
file1.close()

val = best_mlp.predict(X)
print(val[0])
prob= best_mlp.predict_proba(X)
print(prob)
