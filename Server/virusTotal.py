import requests
from lxml import etree
import time

def scan(urlToScan):

  apikey = '01e0d87744ca2b58bfb8776db341b51282e0bec4b278b9f833172d1421ea2d58'
  url = 'https://www.virustotal.com/vtapi/v2/url/scan'
  params = {'apikey': apikey, 'url': urlToScan}
  response = requests.post(url, data=params)
  initScan = response.json()

  finalResult = []
  malic = False
  
  while finalResult == []:
    resultUrl = initScan["permalink"]
    resultRes = requests.get(url=resultUrl)

    tree = etree.HTML(resultRes.content)
    for i in range(1, 100):
      urlScanner = tree.xpath("/html/body/div[1]/div[4]/div[3]/div[1]/div/div/table/tbody/tr["+str(i)+"]/td[1]/text()")
      result = tree.xpath("/html/body/div[1]/div[4]/div[3]/div[1]/div/div/table/tbody/tr["+str(i)+"]/td[2]/text()")
      if len(urlScanner) == 0:
        break
      if result[0] == "Malicious site" or result[0] == "Phishing site":
        print(result)
        malic = True
      finalResult.append({"scanner" : urlScanner[0], "result": result[0]})
  
  sendData = {"status":malic, "result":finalResult}
  return sendData
