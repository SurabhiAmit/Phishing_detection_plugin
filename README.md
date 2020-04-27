# Phishing_websites_detection
As part of group project for MS in Georgia Tech, my team built a mozilla plugin named "SureFire" to detect if a website is a phishing site using machine learning techniques, crowdsourcing and virusTotal statistics. Python,flask web framework, javascript, and HTML were used to build the plugin.

The machine learning part of the project is included in ML_module folder. Grid search was perfomed on SVM, decison tree, gradient boosting classifier, neural network and LDA, and the model with best hyperparameters was selected for each of the 5 ML techniques employed. The average of prediction probabilities by these 5 methods was used to determine if the site is safe or unsafe(phishing). The API.py details the calculation of average probabilities for final prediction.

https://safebrowsing.googleapis.com/v4/threatMatches:find is used to obtain google crowdsourcing data and https://www.virustotal.com/vtapi/v2/url/scan is used to obatin virustotal data to determine the safety of a website. phishing_serverextract.py in Server folder extracts the required features from a website for the machine learning techniques to determine the site credibility. 

The outputs of machine learning models, google crowdourcing and virustotal API are used to calculate the percentage safety for any website.

To run server:
>python3 mainServer.py

To access UI:
http://localhost:9000

To run phishing scrapping:
>python3 phishing.py

To save to CSV from DB
>python save_csv.py
