#
#    Module: nx_create=pd.py
#
#    Ver-0.01: 18Nov2017, Initial implementation from nx_create_image.py Ver-0.03
#    Ver-0.01,23Oct2017, Initial implementation.
#
#    VIP: IP address with PRISM PORT ADDRESS for target AHV cluster.
#    IMG_NAME: Image Name.
#    ISO_URL: url of iso imiage.
#    STORAGE_CONTAINER: Storage Container Name that VM IMAGE will be located.
#         This container must be created prior to create VM image.
#
#
#    Please be careful belows.
#    (1) NUTANIX PRISM REST-API allows duplicated named VM images.
#       e.g. VM name is NOT unique.
#    (2) Although successful api return code 201["Created"], it takes some minutes
#        to show invoked task working in PRISM task window.
#
import sys
import requests
import get_argv
import nx_rest_api


def  nx_create_pd(VIP, PD_NAME):
#    VIP = '172.16.11.109:9440'
    SUB_URL = '/PrismGateway/services/rest/v2.0/protection_domains/'

  # body template for URL POST
  #{
  #   "annotations": [
  #   "PD made by REST-API"
  #   ],
  #   "value": "TestPD002"
  #}

    payload = {
      "annotations": [
          "PD made by REST-API"
      ],
      "value": PD_NAME
    }

    r = requests.Response()
    r = nx_rest_api.rest_api(VIP, SUB_URL, payload, 'post')
    return r

if (__name__=="__main__"):
    # VIP="172.16.8.109:9440"

    argv=get_argv.get_argv(3)
    VIP=argv[1]+":9440"

    PD_NAME=argv[2]

    r=nx_create_pd(VIP,PD_NAME)

    print >> sys.stderr, "Protection Domain %s created." % PD_NAME
    print >> sys.stderr, r

