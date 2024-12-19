import requests
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin

#edgerc = EdgeRc('~/.edgerc.txt') #C:\Users\{username}\.edgerc
edgerc = EdgeRc('./.edgerc') #D:\Python\.edgerc
section = 'default'
baseurl = 'https://%s' % edgerc.get(section, 'host')
 
session = requests.Session()
session.auth = EdgeGridAuth.from_edgerc(edgerc, section)
propertyId = ""
 

path= '/papi/v1/properties/{}/versions'.format(propertyId)
headers = {
  
  "Accept": "application/json",
  "PAPI-Use-Prefixes": "true"
} 
querystring = {
  "contractId": "",
  "groupId": "",
  "offset": "0",
  "limit": "2"
} 
 
result = session.get(urljoin(baseurl, path), headers=headers, params=querystring)
print(result.status_code)
print(result.json()) 