#
#    Module: nx_get_vms.py
#
#    Ver-0.01: 07Nov2017, initial nx_get_networks.py from nx_get_image.py Ver-0.05.
#    Ver-0.05: 25Oct2017, get VIP through arguments.
#    Ver-0.04: 25Oct2017, separate port address of PRISM from VIP argument. (due to change of rest_api())
#    Ver-0.03: 24Oct2017, define nx_get_images()
#    Ver-0.02: 10Oct2017, text -> json conversion should be done in nx_rest_api.rest_api().
#    Ver-0.01: 20Oct2017, Initial implementation from nx_images.py and nx_rest_api.py
#
#    $ python ./nx_get_networks.py  VIP 
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

def  nx_get_networks(VIP):
#    SUB_URL = 'PrismGateway/services/rest/v2.0/networks/'
    SUB_URL = 'api/nutanix/v2.0/networks/'

    payload = {}
    r = requests.Response()
    r = nx_rest_api.rest_api(VIP, SUB_URL, payload, 'get')
    return r


if (__name__=='__main__'):
#    VIP = '172.16.2.109'

    argv=get_argv.get_argv(2)
    VIP=argv[1]

    r=nx_get_networks(VIP)

    print >> sys.stderr, "Return_code:%d" % r.status_code
    print "%s" % r.text

