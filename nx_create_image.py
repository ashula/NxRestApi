#
#    module nx_create_image_url()
#
#    Ver-0.02: 25Oct2017, separate port address of PRISM from VIP argument. (due to change of rest_api())
#    Ver-0.01,23Oct2017, Initial implementation.
#
#    VIP: IP address for target AHV cluster.
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
import nx_rest_api

def nx_create_image_url(VIP,IMG_NAME,IOS_URL,STORAGE_CONTAINER):
    sub_url= "/PrismGateway/services/rest/v2.0/images/"

    body = {
        "name":IMG_NAME,
        "Imagne_type":"DISK_IMAGE",
        "image_import_spec":{
        "url":ISO_URL,
        "storage_container_name":STORAGE_CONTAINER
        }}

    print body
    r=nx_rest_api.rest_api(VIP,sub_url,body,'post')
    return r

if (__name__=="__main__"):
    VIP="172.16.2.109"
    IMG_NAME="xCOS69_ISO"
    ISO_URL= "http://ftp.riken.jp/Linux/centos/6.9/isos/x86_64/CentOS-6.9-x86_64-bin-DVD1.iso"
    STORAGE_CONTAINER="xCTR11x"

    r=nx_create_image_url(VIP,IMG_NAME,ISO_URL,STORAGE_CONTAINER)

    print >> sys.stderr, r

