#!flask/bin/python
from flask import Flask, jsonify, request, render_template
from ML_module import API
import virusTotal
import google
import phishing_serverextract
import json

app = Flask(__name__)

@app.route('/')
def start():
  return render_template('webui.html')

@app.route('/scanurl', methods=['POST'])
def get_tasks():
  url = request.json['url']
  googleSafety = -1
  virusSafety = -1
  mlSafety = -1
  finalMLScore = 0
  virusResult = virusTotal.scan(url)
  print(virusResult["status"])
  if virusResult["status"] == True:
    print("Virus said Yes")
    virusSafety = 1.0

  print(json.dumps(virusResult))

  googleResult = google.googlescan(url)
  if "matches" in googleResult:
    print("Google said Yes")
    googleSafety = 1.0
  print(json.dumps(googleResult))
 
  features= phishing_serverextract.extractandreturn(url)

  print(json.dumps(features))
  mlresult = API.getMLScore(features)["final answer"]
  print("ML Score is:"+str(mlresult))
  finalMLScore =  float(googleSafety*0.4+virusSafety*0.4+mlresult*0.2)
  print("Final Score is",finalMLScore)
  returnObject = {"finalSureFireScore":finalMLScore,"url":url, "ML":{"final_prob":API.getMLScore(features)["final_probability"],"final_result":mlresult,"NN_Ans":API.getMLScore(features)["NN_ans"],"SVM_Ans":API.getMLScore(features)["SVM_ans"],"DT_ans":API.getMLScore(features)["DT_ans"],"Boosting_ans":API.getMLScore(features)["Boosting_ans"]},"Google":googleResult,"VirusTotal":virusResult}
  return jsonify(returnObject)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9000)

