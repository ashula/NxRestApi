#
#    Module: nx_create_protection_domain.py
#
#    Ver-0.01: 21Dec2017, Initial implementation from nx_get_protection_domains.py
#
#    $ python ./nx_create_protection_domain.py  VIP PD_name
#
#    return REST api
#
import os
import sys
import traceback
import json
import requests
import get_argv
import read_credentials
import nx_rest_api

def  nx_get_protection_domains(VIP,PD_name):
    SUB_URL = 'api/nutanix/v2.0/protection_domains/'

    payload = {
        "annotations": [
        "Made v.i.a. REST-API"
         ],
        "value": PD_name
    }
    r = requests.Response()
    r = nx_rest_api.rest_api(VIP, SUB_URL, payload, 'post')
    return r


if (__name__=='__main__'):

    argv=get_argv.get_argv(3)
    VIP=argv[1]
    PD_name=argv[2]

    r=nx_get_protection_domains(VIP,PD_name)

    print >> sys.stderr, "Return_code:%d" % r.status_code
    print "%s" % r.text

