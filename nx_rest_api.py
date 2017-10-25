#
#    Module: nx_rest_api.py
#
#    Nutnaix AHV cluster Imageing tool with NX REST-API
#
#    Ver-0.07: 25Oct2017, separate port address of PRISM from VIP argument.
#    Ver-0.06: 23Oct2017, extend acception of http return code from 200 only to 200..206.
#    Ver-0.05: 10Oct2017, text -> json conversion should be done in nx_rest_api.rest_api().
#    Ver-0.04: 20Oct2017, change file name from nx_get_images.py to nx_rest_api.py
#    Ver-0.03: 20Oct2017, define rest-api() to specify method, from rest_api_get()
#    Ver-0.02: 20Oct2017, define func rest_api_get(), and change __main__ flow to call it.
#    Ver-0.01: 20Oct2017, Initial implementation 
#
#    $ python ./nx_rest_api  <IP>  <sub_url> <body> <method>
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
#      ip: IP address  of target NX cluster. (ex. 172.16.11.109, function supply PRISM port address 9440.)
#      sub_url: sub_url to specify REST-API version and action.
#      payload: parameter in json format.
#      method: method of REST-API, e.g. GET,PUT,DELETE,UPDAYE
#
def rest_api(ip, sub_url, payload, method):
#    print "ip=%s" % ip
#    print "sub_url=%s" % sub_url
#    print "body=%s" % payload
#    print "method=%s" % method
   
    URL='https://'+ip+':9440/'+ sub_url
    print "url=%s" % URL
    
    jpayload=json.dumps(payload)

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
            elif (method == 'post'):
                r = requests.post(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
            elif (method == 'delete'):
                r = requests.delete(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
            elif (method == 'put'):
                r = requests.put(URL,headers=headers,auth=(uid,pwd),verify=False,data=jpayload)
            else:            
                print >> sys.stderr, "Bad method %s. Program Abort!" % method
                exit()
        except requests.exceptions.RequestException as e:
            f_success = False
            
            print >> sys.stderr, "Requests Exception== %s" % e
            print >> sys.stderr, "Credentials: maybe not be reachable to Target!"
            r.status_code = 400
        else:
            if (r.status_code in [200,201,202,203,204,205,206]):
                f_success = True
                print >> sys.stderr,"(%s,%s):Credentials Success" % (uid,pwd)
                break
            else:     # case of Authentication Error.
                f_success = False
                print >> sys.stderr, "(%s,%s):Credentials Fail!x" % (uid,pwd)
                continue
    return r

#######################

if (__name__=='__main__'):
    VIP='172.16.2.109'
    SUB_URL='PrismGateway/services/rest/v2.0/images/'
    
    payload={}

    r = requests.Response()
    r = rest_api(VIP,SUB_URL,payload,'get')

    print r.text

else:
    pass
