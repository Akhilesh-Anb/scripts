#!/usr/bin/env python
import subprocess
import os
import sys
import re
import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder
import concurrent.futures
import executor
import argparse
import os.path
import time

parser = argparse.ArgumentParser(description='Provide Ops Manager URL.')
parser.add_argument('url', help='provide ops manager url')
parser.add_argument('--setup', '-s', action='store_true', help='configure ops manager for first time')
args = parser.parse_args()
url = args.url

if args.setup:
    urlsetup = url+"/api/v0/setup"
    OPSPW=os.environ["OPSPW"]
    #print(x)
    m = MultipartEncoder(
        fields={'setup[decryption_passphrase]': '%s'%OPSPW, 'setup[decryption_passphrase_confirmation]': '%s'%OPSPW, 'setup[eula_accepted]': 'true', 'setup[identity_provider]' : 'internal', 'setup[admin_user_name]': 'admin', 'setup[admin_password]': '%s'%OPSPW, 'setup[admin_password_confirmation]': '%s'%OPSPW, 'Content-Type': 'application/x-www-form-urlencoded'}
        )
    headers = {'Content-Type': m.content_type}
    r = requests.post(urlsetup, data=m, headers=headers, verify=False)

#urlpost = url+"/api/v0/available_products"

def files_upload(x):
    urlpost = url+"/api/v0/available_products"
    directory='/mnt/netshare/Share/Cloud-Foundary/pcf1.7/products/'
    #print(x)
    m = MultipartEncoder(
        fields={'product[file]': ('filename', open('%s%s'%(directory,x), 'rb'), 'application/zip')}
    )
    headers = {'Authorization' : 'Bearer %s'%accesstoken, 'Content-Type': m.content_type}
    r = requests.post(urlpost, data=m, headers=headers, verify=False)
    #r = requests.get(urlpost,headers=headers,verify=False)
    time.sleep(30)


#if os.path.isfile("/home/ubuntu/.uaac.yml") !=True:
subprocess.call(["uaac", "target", url+"/uaa" ,"--skip-ssl-validation"])
subprocess.call(["uaac", "token", "owner", "get", "opsman" ,"admin" , "-p", os.environ["OPSPW"], "-s", ""])


with open('%s/.uaac.yml'%os.environ["HOME"],'r') as f:
    for line in f:
        if 'access_token' in line:
           line = re.sub("\s+access_token:\s+","", line)
           line = line.strip()
           #print(line)
           accesstoken = line

#urlpost = url+"/api/v0/available_products"
#def files_upload(x):
#    #print(x)
#    m = MultipartEncoder(
#        fields={'product[file]': ('filename', open('/pcf/%s'%x, 'rb'), 'application/zip')}
#    )
#    headers = {'Authorization' : 'Bearer %s'%accesstoken, 'Content-Type': m.content_type}
#    r = requests.post(urlpost, data=m, headers=headers, verify=False)
#    #r = requests.get(urlpost,headers=headers,verify=False)

directory=os.listdir("/mnt/netshare/Share/Cloud-Foundary/pcf1.7/products")
#executor = concurrent.futures.ProcessPoolExecutor(2)
executor = concurrent.futures.ThreadPoolExecutor(6)
futures = [executor.submit(files_upload, x) for x in directory]
concurrent.futures.wait(futures)
