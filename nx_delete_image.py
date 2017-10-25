#
#    module nx_delete_image.py
#
#    Ver-0.03: 25Oct2017, VIP, IMAGE_NAME is passwd through argv.
#    Ver-0.02: 25Oct2017, defined nx_delete_image() return values.
#    Ver-0.01: 25Oct2017, Initial Implementation
#
#    Return the number of deleted images.  (0 means there is no  image specified by name.
#
import sys
import os
import get_argv
import nx_rest_api
import nx_get_images
import nx_get_image_uuid

def nx_delete_image(VIP,IMAGE_NAME):
    SUB_URL="PrismGateway/services/rest/v2.0/images"
    SUB_URL_UUID=''
    body = '{}'
#  e.x.  image_uuid = '90a0068f-238a-452d-8b79-dd69743d9603'
    JSON=r.json()
    image_uuid_list= nx_get_image_uuid.get_image_uuid(JSON,IMAGE_NAME)
    print >>sys.stderr, "UUID_LIST: %s" % image_uuid_list

    n = len(image_uuid_list)
    # i=1
    for uuid in image_uuid_list:
        print >> sys.stderr, "UUID:%s is going to be deleted!!" % uuid
        SUB_URL_UUID=SUB_URL+'/'+uuid
        # print >> sys.stderr, "SUB_URL_UUID: %s" % SUB_URL_UUID
        nx_rest_api.rest_api(VIP,SUB_URL_UUID,body,'delete')
     #   i+=1

    return n

if (__name__=='__main__'):
#    VIP = '172.16.2.109'
#    IMAGE_NAME='xCOS69_ISO'

    argv=get_argv.get_argv(3)
    VIP=argv[1]
    IMAGE_NAME=argv[2]

    r=nx_get_images.nx_get_images(VIP)
    n=nx_delete_image(VIP,IMAGE_NAME)

    print >> sys.stderr, "%d images with name %s are removed!." % (n,IMAGE_NAME)
