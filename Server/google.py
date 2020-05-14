import requests
import json

def googlescan(urltoScan):
	api_key='<please insert yours>'
	url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
	payload = {'client': {'clientId': "mycompany", 'clientVersion': "0.1"},
	        'threatInfo': {'threatTypes': ["SOCIAL_ENGINEERING", "MALWARE"],
	                       'platformTypes': ["ANY_PLATFORM"],
	                       'threatEntryTypes': ["URL"],
	                       'threatEntries': [{'url': urltoScan}]}}
	params = {'key': api_key}
	r = requests.post(url, params=params, json=payload,verify=False)
# Print response
	#print(r) 
	return r.json()

