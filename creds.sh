#!/bin/bash -e

j=$(om -t https://$OPS_MGR_HOST -k -u $OPS_MGR_USR  -p $OPSPW curl -s -p "/api/v0/deployed/director/credentials/director_credentials") &> /dev/null
userid=$(jq -r '.credential.value.identity' <<< $j)
pw=$(jq -r '.credential.value.password' <<< $j)
#om -t https://$OPS_MGR_HOST -k -u $OPS_MGR_USR -p $OPSPW curl -p "/api/v0/deployed/director/credentials/director_credentials" | jq -r '.credential.value.identity, .credential.value.password' 

echo $userid
echo $pw
