#
#    Module: nx_get_images.py
#
#    Ver-0.04: 25Oct2017, separate port address of PRISM from VIP argument. (due to change of rest_api())
#    Ver-0.03: 24Oct2017, define nx_get_images()
#    Ver-0.02: 10Oct2017, text -> json conversion should be done in nx_rest_api.rest_api().
#    Ver-0.01: 20Oct2017, Initial implementation from nx_images.py and nx_rest_api.py
#
#    $ python ./nx_get_images IP sub_url body
#
#    return REST api
#
import os
import sys
import traceback
import json
import requests
import read_credentials
import nx_rest_api

def  nx_get_images(VIP):
#    VIP = '172.16.11.109'
    SUB_URL = 'PrismGateway/services/rest/v2.0/images/'

    payload = {}
    r = requests.Response()
    r = nx_rest_api.rest_api(VIP, SUB_URL, payload, 'get')
    return r


if (__name__=='__main__'):
    VIP = '172.16.2.109'
    r=nx_get_images(VIP)

    print "Return_code:%d" % r.status_code
    print "%s" % r.text

