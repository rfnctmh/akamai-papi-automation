import requests
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin

#edgerc = EdgeRc('~/.edgerc.txt') #C:\Users\{username}\.edgerc
edgerc = EdgeRc('./.edgerc') #D:\Python\.edgerc
section = 'default'
baseurl = 'https://%s' % edgerc.get(section, 'host')
 
session = requests.Session()
session.auth = EdgeGridAuth.from_edgerc(edgerc, section)
 
path = '/papi/v1/search/find-by-value'
headers = {
  "Content-Type": "application/json",
 
  "Accept": "application/json",
  "PAPI-Use-Prefixes": "true"
}
payload = {
    "propertyName": "xxx.example.com",   
}  
querystring = {
}  
 
result = session.post(urljoin(baseurl, path), headers=headers, json=payload, params=querystring)
print(result.status_code)
print(result.json()) 