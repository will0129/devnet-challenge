#### Modify Code After line 22 - 
import requests
from requests.auth import HTTPBasicAuth
import json

### Get a token, specific to DNAC,
DNAC='sandboxdnac.cisco.com'
DNAC_USER='devnetuser'
DNAC_PASSWORD='Cisco123!'
INTENT_API = "https://sandboxdnac.cisco.com/dna/intent/api/v1/"
url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD),verify=False)
# print(resp.text)      #<<<<<<<<<<< You should see your token)
token = resp.json()['Token']   # We set our token. 
## Token = Authentication, 
url = INTENT_API+"network-device"   # we set our new URL to get devices
hdr={'x-auth-token': token}         #we set our header. this is the token format for DNAC.
resp = requests.get(url, headers=hdr,verify=False)
dnac_list = resp.json()
print(json.dumps(dnac_list,indent=2))

### MODIFY HERE!!!
## Modify the below to replace "roleSource" with the appropriate 
### Json key for the platform ((( Based on output)))
 ## like, asr 1002, etc. 

######## Flag

print ('Device     Version      Platform')
for device in dnac_list['response']:
	print(device['hostname'],device['softwareVersion'],device['roleSource'])

