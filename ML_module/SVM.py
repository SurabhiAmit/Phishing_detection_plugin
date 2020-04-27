from sklearn.preprocessing import scale
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
file1 = open(r'.\phishing_X.pkl', 'rb')
X_data = pickle.load(file1)
file1.close()
file1 = open(r'.\phishing_Y.pkl', 'rb')
Y_data = pickle.load(file1)
file1.close()
out = './Phishing/'

model = SVC()
kernels= ['rbf','linear','poly','sigmoid']
degrees=[1,3,5,7,10,15]
parameters={'kernel': kernels, 'degree': degrees}
gs = GridSearchCV(model,parameters, verbose=10, cv=10)
gs.fit(X_data,Y_data)
tmp = pd.DataFrame(gs.cv_results_)
tmp.to_csv(out+'Phishing_GridSearchCV_SVM.csv')

#get the best model from Phishing_GridSearchCV.csv
best_model = SVC(kernel ='rbf', degree=1, probability=True)
best_model.fit(X_data, Y_data)
bestModel = open(r'.\BestModel_SVM.pkl', 'wb')
pickle.dump(best_model,bestModel)
bestModel.close()

