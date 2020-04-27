from sklearn.preprocessing import scale
import pickle
from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV


file1 = open(r'.\phishing_X.pkl', 'rb')
X_data = pickle.load(file1)
file1.close()
file1 = open(r'.\phishing_Y.pkl', 'rb')
Y_data = pickle.load(file1)
file1.close()
out = './Phishing/'
mlp = MLPClassifier(activation='relu', max_iter=2000, early_stopping=True, random_state=5)
alphas = [0.1,0.2,0.001,0.01,0.0001]
#31+2=33/2=16 or 17 (hidden layer node count)

architectures = [(17, 50), (50,), (17,), (25, 25), (100, 25, 100)]
parameters={'alpha': alphas, 'hidden_layer_sizes': architectures}
grid = GridSearchCV(mlp,parameters, verbose=10, cv=10)
grid.fit(X_data,Y_data)
results = pd.DataFrame(grid.cv_results_)
results.to_csv(out+'Phishing_GridSearchCV_NN.csv')

#get the best model from Phishing_GridSearchCV.csv
best_mlp = MLPClassifier(activation='relu', max_iter=2000, early_stopping=True, random_state=5, alpha =0.001, hidden_layer_sizes=(17,))
best_mlp.fit(X_data, Y_data)
bestModel = open(r'.\BestModel_NN.pkl', 'wb')
pickle.dump(best_mlp,bestModel)
bestModel.close()
