import whois
import datetime
import requests
from requests_html import HTMLSession
import urllib.request as urllib2
import re
from urllib.parse import urlparse
from xml.dom import minidom
from lxml import html

def checkDash(url):
  if len(urlparse(url).netloc.split('-')) > 1:
    return 1
  else:
    return -1

def checkDot(url):
  dotPresent = urlparse(url).netloc.split('.')
  if len(dotPresent) > 3:
    return 1
  elif len(dotPresent) == 3:
    return 0
  else:
    return -1

def checkIfHTTPS(url):
  o = urlparse(url)
  hostname = o.netloc
  print(hostname)
  if o.scheme != "https":
    try:
      o=requests.get("https://"+hostname, verify=True, timeout=1)
      return -1
    except Exception as e:
      #print(e)
      if "SSL23_GET_SERVER_HELLO" in str(e) or "Failed to establish a new connection" in str(e):
        return 1
      else:
        return 0
  else:
    return -1

def checkLen(url):
  if len(url) < 54:
    return -1
  elif len(url) >= 54 and len(url) <= 75:
    return 0
  else:
    return 1    

def ageOfTheDomainandDNS(url):
  try:
   details= whois.whois(url)
   now = datetime.datetime.now()
   diff = (now-details.creation_date[0]).days
   if diff >= 180:
    return -1
   return 1 
  except:
    return 1

def find_ele_with_attribute(dom,ele,attribute):
  for subelement in dom.getElementsByTagName(ele):
    if subelement.hasAttribute(attribute):
        return subelement.attributes[attribute].value
  return None

def sitepopularity(host):
  xmlpath='http://data.alexa.com/data?cli=10&dat=snbamz&url='+host
  try:
    xml= urllib2.urlopen(xmlpath)
    dom =minidom.parse(xml)
    rank_host=find_ele_with_attribute(dom,'REACH','RANK')
    if int(rank_host) < 100000:
      return -1
    elif int(rank_host) > 100000:
      return 0
  except:
    return 1

def parseHTMLForRequestURL(url):
  page = requests.get(url)
  webpage = html.fromstring(page.content)
  div = webpage.xpath('//img/@src')
  host= urlparse(url).hostname
  imgcount = 0
  for k in range(0,len(div)):
    try:
    # print(div[k].attrs['src']) 
      if div[k].startswith("/"):
        #print("Here")
        imgcount = imgcount+1
      else:
        o = urlparse(div[k])
        if o.hostname == host:
          imgcount = imgcount+1
    except Exception as e:
      print(e)
      continue

  if len(div) != 0:
    percent = ((len(div)-imgcount)/len(div))*100
    if percent < 22:
      return -1
    elif percent>=22 and percent<61:
      return 0
    else:
      return 1
  else:
    return 0

def parseHTMLForAnchors(url):
  page = requests.get(url)
  webpage = html.fromstring(page.content)
  anchor = webpage.xpath('//a/@href')
  host= urlparse(url).hostname
  anchorcount = 0
  for k in range(0,len(anchor)):
    try:
      if anchor[k].startswith("/"):
        anchorcount = anchorcount+1
      else:
        o = urlparse(anchor[k])
      if o.hostname == host:
        anchorcount = anchorcount+1
    except Exception as e:
      print(e)
      continue
  if len(anchor)!=0:
   percent = ((len(anchor)-anchorcount)/len(anchor))*100
   if percent < 31:
    return -1
   elif percent>=31 and percent<67:
    return 0
   else:
    return 1
  else:
    return 0

def extractandreturn(url):
  try:
    page = requests.get(url,timeout=1,verify=False)
    webpage = html.fromstring(page.content)
    cdash = checkDash(url)
    cdot = checkDot(url)
    chtps = checkIfHTTPS(url)
    clen = checkLen(url)
    creq = parseHTMLForRequestURL(url)
    canc = parseHTMLForAnchors(url)
    cage = ageOfTheDomainandDNS(urlparse(url).hostname)
    cpop = sitepopularity(urlparse(url).hostname)
    return([cdash, cdot, chtps, clen , creq, canc, cage, cpop])
  except Exception as e:
   print("Site down")
