#
#    Nutnaix AHV cluster Imageing tool with NX REST-API
#
#    Ver-0.03: 20Oct2017, define rest-api() to specify method, from rest_api_get()
#    Ver-0.02: 20Oct2017, define func rest_api_get(), and change __main__ flow to call it.
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

#
#  def rest_api(ip,sub_url,body,method)
#
#      ip: IP address and PORT of target NX cluster. (ex. 172.16.11.109:9440)
#      sub_url: sub_url to specify REST-API version and action.
#      body: parameter in json format.
#      method: method of REST-API, e.g. GET,PUT,DELETE,UPDAYE
#
def rest_api(ip, sub_url, body, method):
    URL='https://'+ip+'/'+ sub_url

    headers={'Content-Type': 'application/json; charset=utf-8'}

    credentials_list = read_credentials.read_credentials('CREDENTIALS_LIST.txt') 
    num_credentials = len(credentials_list)
    
    print >> sys.stderr, "%d" % num_credentials
    
    i = 0
    while (i < num_credentials):
        uid = credentials_list[i]
        pwd = credentials_list[i+1]
        i+=2
        print >> sys.stderr, "(%s,%s)" % (uid,pwd)
        r = requests.Response()
        try:
            if (method == 'get'):
                r = requests.get(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
            elif (method == 'put'):
                r = requests.put(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
            elif (method == 'delete'):
                r = requests.delete(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
            elif (method == 'update'):
                r = requests.update(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
            else:
            
                print >> sys.syserr, "Bad method %s." % method
                exit()
        except:
            f_success = False
            print >> sys.stderr, "Credentials: maybe not reachable to Target!"
            r.status_code = 400
        else:
            if (r.status_code ==200):
                f_success = True
                print >> sys.stderr,"(%s,%s):Credentials Success" % (uid,pwd)
                break
            else:
                f_success = False
                print >> sys.stderr, "(%s,%s):Credentials Fail!x" % (uid,pwd)
                continue
    return r

#######################

if (__name__=='__main__'):
    VIP='172.16.11.109:9440'
    SUB_URL='PrismGateway/services/rest/v2.0/images/'
    
    payload={}
    jpayload=json.dumps(payload)

    r = requests.Response()
    r = rest_api(VIP,SUB_URL,jpayload,'get')

    print r.text

