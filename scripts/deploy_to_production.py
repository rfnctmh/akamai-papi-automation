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
 

path= '/papi/v1/properties/{}/activations'.format(propertyId)
headers = {
  "Content-Type": "application/json",

  "Accept": "application/json",
  "PAPI-Use-Prefixes": "true"
}
payload = {
    "propertyVersion": 1,
    "network": "Production",
    "note": "調整維護頁",
    "useFastFallback": False,
    "acknowledgeAllWarnings": True,
    "fastPush": True,    
    "notifyEmails": [
        "xxx@example .com."
    ],
    "acknowledgeWarnings": [
        ""
    ]
} 
querystring = {
  "contractId": "",
  "groupId": ""
}  

result = session.post(urljoin(baseurl, path), headers=headers, json=payload, params=querystring)
print(result.status_code)
print(result.json()) 