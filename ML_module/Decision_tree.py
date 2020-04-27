from sklearn.preprocessing import scale
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

file1 = open(r'.\phishing_X.pkl', 'rb')
X_data = pickle.load(file1)
file1.close()
file1 = open(r'.\phishing_Y.pkl', 'rb')
Y_data = pickle.load(file1)
file1.close()
out = './Phishing/'

criterions=['gini','entropy']
leaf_size =[1,2,4,5,8,10,12]
model = DecisionTreeClassifier()
parameters={'min_samples_leaf': leaf_size, 'criterion': criterions}
gs = GridSearchCV(model,parameters, verbose=10, cv=10)
gs.fit(X_data,Y_data)
tmp = pd.DataFrame(gs.cv_results_)
tmp.to_csv(out+'Phishing_GridSearchCV_DT.csv')

#get the best model from Phishing_GridSearchCV.csv
best_model = DecisionTreeClassifier(min_samples_leaf=10, criterion = "entropy")
best_model.fit(X_data, Y_data)
bestModel = open(r'.\BestModel_DT.pkl', 'wb')
pickle.dump(best_model,bestModel)
bestModel.close()
