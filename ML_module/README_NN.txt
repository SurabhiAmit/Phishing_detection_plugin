Folder structure
Parent folder has the following files:
1.get_data.py
2.NN.py
3.NN_API.py
4.datasets.csv
5.A folder named phishing where NN.py outputs gridsearch results


How to run the code?
1. Run get_data.py from a directory where datasets.csv is present. 
2. Run NN.py from the same directory as get_data.py
3. Input the features list in NN_API.py as a list(variable s) to get the final value [1 or -1] and the probability of the final answer

What the code does?
1. get_data.py preprocesses datasets.csv
2. NN.py uses output of get_data.py, performs grid search and trains the best NN model. 
3. NN.py outputs the best model into BestModel.pkl file.
4. NN_API.py gives the prediction and probability

NB: Once BestModel.pkl is created, get_data.py and NN.py are no longer needed. 
Only NN_API.py is used in runtime code and BestModel.pkl should be in the same directory as NN_API.py.
