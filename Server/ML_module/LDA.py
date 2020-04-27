from sklearn.preprocessing import scale
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

file1 = open(r'.\phishing_X.pkl', 'rb')
X_data = pickle.load(file1)
file1.close()
file1 = open(r'.\phishing_Y.pkl', 'rb')
Y_data = pickle.load(file1)
file1.close()
out = './Phishing/'

solvers=['svd','lsqr','eigen']
components=[2,3,4]
model = LinearDiscriminantAnalysis()
parameters={'n_components': components, 'solver': solvers}
gs = GridSearchCV(model,parameters, verbose=10, cv=10)
gs.fit(X_data,Y_data)
tmp = pd.DataFrame(gs.cv_results_)
tmp.to_csv(out+'Phishing_GridSearchCV_LDA.csv')

#get the best model from Phishing_GridSearchCV.csv
best_model = LinearDiscriminantAnalysis(n_components=2, solver='svd')
best_model.fit(X_data, Y_data)
bestModel = open(r'.\BestModel_LDA.pkl', 'wb')
pickle.dump(best_model,bestModel)
bestModel.close()
