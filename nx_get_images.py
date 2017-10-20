#
#    Nutnaix AHV cluster Imageing tool with NX REST-API
#
#    Ver-0.01: 20Oct2017, Initial implementation 
#
#    $ python ./nx_rest_api  IP sub_url body
#
#    return REST api
#
import os
import sys
import traceback
import json
import requests
import read_credentials

def rest_api(vip, sub_url, body):
    i=0
    while (i<num_credentials):
        pass

if (__name__=='__main__'):
    VIP='172.16.11.109:9440'
    SUB_URL='PrismGateway/services/rest/v2.0/images/'
    URL='https://'+VIP+'/'+SUB_URL
    
    headers={'Content-Type': 'application/json; charset=utf-8'}
    payload={}
    jpayload=json.dumps(payload)

    credentials_list = read_credentials.read_credentials('CREDENTIALS_LIST.txt') 
    num_credentials = len(credentials_list)
    print >> sys.stderr, "%d" % num_credentials

#    f_success = True
    i = 0
    while (i < num_credentials):
        uid = credentials_list[i]
        pwd = credentials_list[i+1]
        i+=2
        print >> sys.stderr, "(%s,%s)" % (uid,pwd)
        try:
            r = requests.get(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
        except:
            f_success = False
            print sys.stderr, "Credentials: maybe not reachable to Target!"
            # print "Return Code:%s." % r.status_code
        else:
            if (r.status_code ==200):
                f_success = True
                print sys.stderr,"(%s,%s):Credentials Success" % (uid,pwd)
                break
            else:
                f_success = False
                print sys.stderr, "(%s,%s):Credentials Fail!x" % (uid,pwd)
                continue
    
    if (f_success == True):
        print >> sys.stderr, "Retrun_code %s" % r.status_code
        f = open('result.json','w')
        print >> f, r.json()
        f.close()
    else:
        print >> sys.stderr, "end with REST-API failure."

else:
    pass
