# Phishing_websites_detection
A mozilla plugin named "SureFire" to detect if a website is a phishing site using machine learning techniques, crowdsourcing and virusTotal statistics. Python,flask web framework, javascript, and HTML were used to build the plugin. video_demonstration.mp4 has the video presentation for this project.

The machine learning part of the project is included in ML_module folder. Grid search was perfomed on SVM, decison tree, gradient boosting classifier, neural network and LDA, and the model with best hyperparameters was selected for each of the 5 ML techniques employed. The average of prediction probabilities by these 5 methods was used to determine if the site is safe or unsafe(phishing). The API.py details the calculation of average probabilities for final prediction.

https://safebrowsing.googleapis.com/v4/threatMatches:find is used to obtain google crowdsourcing data and https://www.virustotal.com/vtapi/v2/url/scan is used to obatin virustotal data to determine the safety of a website. 

The outputs of machine learning models, google crowdourcing and virustotal API are used to calculate the percentage safety for any website.

To run server:
>python3 mainServer.py

To access UI:
http://localhost:9000

To run phishing scrapping: [extracts the required features from a website for the machine learning techniques to determine the site credibility]
>python3 phishing.py

To save to CSV from DB [saves all extracted features to a CSV file]
>python save_csv.py
