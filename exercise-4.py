Challenge starts on line 14

### This is all you need to get information from Meraki or webex teams. You get your token out of band
TOKEN = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'  ### Authentication
URL="https://api.meraki.com/api/v0/organizations/549236/networks/L_646829496481105433/devices"  # URL
HDR={'X-Cisco-Meraki-API-Key': TOKEN}   #### This is the meraki header needed, - HEADER
NETWORKS=requests.get(URL,headers=HDR)  ### do you see how easy this is, you have the URL, the authentication, and the header. Now we just do a request.

########### Thats it. The below lines really format it so you can read it
NET_JSON=json.loads(NETWORKS.text)
print(json.dumps(NET_JSON,indent=2))


## the above prints model, firmware, lattitude, so its basically worthless. We want 
## Model, firmware, and an IP address. 
## You need to choose an IP from the above list.
## Hint, if you choose the WRONG IP key from above list (wan1Ip, etc...) your code will error out. because not all devices have a Wan Ip... you know?
meraki_list=NET_JSON
for device in meraki_list:
	print(device['model'],device['firmware'],device['lat'])
