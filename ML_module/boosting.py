from sklearn.preprocessing import scale
import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier

file1 = open(r'.\phishing_X.pkl', 'rb')
X_data = pickle.load(file1)
file1.close()
file1 = open(r'.\phishing_Y.pkl', 'rb')
Y_data = pickle.load(file1)
file1.close()
out = './Phishing/'
model = GradientBoostingClassifier(random_state=6, max_depth=2, validation_fraction=0.05)
alphas =[0.1,0.01,0.05,0.2,0.001]
tree_count=[50, 100, 150, 200, 400]
parameters={'learning_rate': alphas, 'n_estimators': tree_count}
gs = GridSearchCV(model,parameters, verbose=10, cv=10)
gs.fit(X_data,Y_data)
tmp = pd.DataFrame(gs.cv_results_)
tmp.to_csv(out+'Phishing_GridSearchCV_Boosting.csv')

#get the best model from Phishing_GridSearchCV.csv
best_model = GradientBoostingClassifier(learning_rate=0.2, n_estimators=400, random_state=6, max_depth=2,validation_fraction=0.05)
best_model.fit(X_data, Y_data)
bestModel = open(r'.\BestModel_Boosting.pkl', 'wb')
pickle.dump(best_model,bestModel)
bestModel.close()


