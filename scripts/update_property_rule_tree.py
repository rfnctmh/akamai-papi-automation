import requests
from akamai.edgegrid import EdgeGridAuth, EdgeRc
from urllib.parse import urljoin

#edgerc = EdgeRc('~/.edgerc.txt') #C:\Users\{username}\.edgerc
edgerc = EdgeRc('./.edgerc') #D:\Python\.edgerc
section = 'default'
baseurl = 'https://%s' % edgerc.get(section, 'host')
 
session = requests.Session()
session.auth = EdgeGridAuth.from_edgerc(edgerc, section)
propertyVersion = "1"
propertyId = ""
 

path= '/papi/v1/properties/{}/versions/{}/rules'.format(propertyId, propertyVersion)
headers = {
  "Content-Type": "application/json",

  "Accept": "application/vnd.akamai.papirules.*+json",
  "If-Match": "\"\"",
  "PAPI-Use-Prefixes": "true"
}
payload = {
    ...
} 
querystring = {
  "contractId": "",
  "groupId": "",
  "validateMode": "full",
  "validateRules": "true",
  "dryRun": "true"
}  

result = session.put(urljoin(baseurl, path), headers=headers, json=payload, params=querystring)
print(result.status_code)
print(result.json()) 