import requests
import json

def googlescan(urltoScan):
	api_key='AIzaSyA13sB-HOUx8ykIGmiRTJ2X-JL6rddY-o0'
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

#googlescan("https://lubanghitamadadidalamhati.org/myaccount/signin/step1.php?rsjkingdomdisini=session=&c0da7d9c74a503072296f59779a21ebb&dispatch=ab6c0d4b627cbbc78c610d2e83810ec052cd7f4051d17ca84fa25dbbe0f07f752a04d8956c1a9ccea50128534f9bca92797fb5468815b2ca60f71d62")	