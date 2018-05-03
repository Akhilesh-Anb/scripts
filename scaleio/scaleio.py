#!/usr/bin/env python
import json
import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt import SSLAdapter
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import os
import ssl
import logging
import time
import sys
import pprint
import urllib3
import csv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url=os.environ["GATEWAY"]
user=os.environ["API_USER"]
password=os.environ["API_PW"]
resp = requests.get("https://"+url+"/api/login", auth=(user, password), verify=False)
d=resp.json()
token=d
#print token

#r = requests.get(url+"/api/instances", auth=( user, token), verify=False)
#pprint.pprint(r.json())

r = requests.post("https://"+url+"/api/instances/querySelectedStatistics", auth=( user, token), verify=False, json={"selectedStatisticsList":[
  {"type": "System", "allIds": "",
     "properties": ["capacityAvailableForVolumeAllocationInKb","unusedCapacityInKb","spareCapacityInKb","capacityInUseInKb","protectedCapacityInKb","thinCapacityInUseInKb","capacityLimitInKb","thickCapacityInUseInKb","maxCapacityInKb"]}
  ]})
#pprint.pprint(r.json())

capacity=r.json()
availc=capacity['System']['capacityAvailableForVolumeAllocationInKb']
usedc=capacity['System']['capacityInUseInKb']
totalc=capacity['System']['maxCapacityInKb']
protc=capacity['System']['protectedCapacityInKb']
sparec=capacity['System']['protectedCapacityInKb']
thickc=capacity['System']['thickCapacityInUseInKb']
thinc=capacity['System']['thinCapacityInUseInKb']
unusedc=capacity['System']['unusedCapacityInKb']

print availc
print usedc
print totalc
print protc
print sparec
print thickc
print thinc
print unusedc



availc=int(availc)
usedc=int(usedc)
totalc=int(totalc)
protc=int(protc)
sparec=int(sparec)
thickc=int(thickc)
thinc=int(thinc)
unusedc=int(unusedc)

availc=(availc/(1024*1024))
usedc=(usedc/(1024*1024))
totalc=(totalc/(1024*1024))
protc=(protc/(1024*1024))
sparec=(sparec/(1024*1024))
thickc=(thickc/(1024*1024))
thinc=(thinc/(1024*1024))
unusedc=(unusedc/(1024*1024))

availc=str(availc)
usedc=str(usedc)
totalc=str(totalc)
protc=str(protc)
sparec=str(sparec)
thickc=str(thickc)
thinc=str(thinc)
unusedc=str(unusedc)

with open("scaleio-capacity.csv", "w") as cap:
   cap.write("stie,az,total capacity,Available for Allocation,Unused capacity,Spare capacity,Protected Capacity,Used Thick capacity,Used thin capacity\n")

with open ("scaleio-capacity.csv", "a") as cap:
    cap.write("homelab,AZ1,"+totalc+","+availc+","+unusedc+","+sparec+","+protc+","+thickc+","+thinc+"\n")
    cap.write("\n")
