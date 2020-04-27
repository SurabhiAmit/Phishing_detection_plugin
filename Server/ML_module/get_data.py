import pickle
import warnings
import numpy as np
from sklearn.preprocessing import scale


#PhishingWebsites
with warnings.catch_warnings():
    warnings.simplefilter("ignore",category=DeprecationWarning)
training_data = np.genfromtxt('dataset1.csv', delimiter=',', dtype=np.int32)
X = np.delete(training_data, -1, axis =1)
Y = training_data [:,-1]
X_train = scale(X)
Y_train= Y
n_samples, n_features = X.shape
n_classes = len(np.unique(Y))

print("n_classes: %d, \t n_samples %d, \t n_features %d"
      % (n_classes, n_samples, n_features))

#code reference: https://stackoverflow.com/questions/1047318/easiest-way-to-persist-a-data-structure-to-a-file-in-python
#X values
afile = open(r'phishing_X.pkl', 'wb')
pickle.dump(X_train, afile)
afile.close()
#Y_values
afile = open(r'phishing_Y.pkl', 'wb')
pickle.dump(Y_train, afile)
afile.close()